#!/usr/bin/env python3
"""
Bidirectional Link Generator for AI Knowledge Domain

This script automatically:
1. Scans directories for markdown files
2. Updates README.md with links to content files
3. Adds back-references from content files to README.md

Usage:
    python scripts/link_knowledge_articles.py [--dry-run]
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from urllib.parse import quote

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


def extract_first_heading(filepath: Path) -> str:
    """Extract the first heading from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Skip YAML frontmatter
                if line.strip().startswith('---'):
                    continue
                # Skip back-reference links
                if line.strip().startswith('*[← Back to'):
                    continue
                # Find first heading (# or ##)
                if line.strip().startswith('#'):
                    # Remove markdown heading syntax
                    title = re.sub(r'^#+\s*', '', line.strip())
                    # Remove special characters for cleaner titles
                    title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)
                    title = title.replace('{:', '').strip()
                    return title
        # If no heading found, use filename
        return filepath.stem.replace('-', ' ').replace('_', ' ').title()
    except Exception as e:
        print(f"Warning: Could not extract heading from {filepath}: {e}")
        return filepath.stem.replace('-', ' ').replace('_', ' ').title()


def get_directory_title(readme_path: Path) -> str:
    """Extract the title from the README.md file."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            in_yaml = False
            for line in f:
                if line.strip() == '---':
                    in_yaml = not in_yaml
                    continue
                if not in_yaml:
                    # Look for the main heading
                    if line.strip().startswith('# '):
                        title = line.replace('#', '').strip()
                        return title
    except Exception as e:
        print(f"Warning: Could not extract title from {readme_path}: {e}")
    return "Knowledge Base"


def scan_directory(directory: Path) -> List[Path]:
    """Scan directory for markdown files (excluding README.md)."""
    md_files = []
    
    for item in directory.iterdir():
        # Skip directories, README, and hidden files
        if item.is_dir() or item.name == 'README.md' or item.name.startswith('.'):
            continue
        
        # Include .md files and files without extension (like 'imperative vs declarative')
        if item.suffix == '.md' or (item.suffix == '' and item.is_file()):
            # Check if it's likely a text file
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    f.read(100)  # Try reading first 100 chars
                md_files.append(item)
            except (UnicodeDecodeError, PermissionError):
                # Skip binary or inaccessible files
                continue
    
    return sorted(md_files, key=lambda x: x.name.lower())


def url_encode_filename(filename: str) -> str:
    """URL encode filename for markdown links."""
    return quote(filename)


def generate_readme_section(files: List[Path]) -> str:
    """Generate the Knowledge Articles section for README.md."""
    if not files:
        return ""
    
    lines = [
        "",
        "## Knowledge Articles",
        "",
        "### Core Topics",
        ""
    ]
    
    for file in files:
        title = extract_first_heading(file)
        encoded_name = url_encode_filename(file.name)
        lines.append(f"- [{title}]({encoded_name})")
    
    lines.append("")
    
    return "\n".join(lines)


def has_back_reference(filepath: Path) -> bool:
    """Check if file already has a back-reference."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_lines = ''.join([f.readline() for _ in range(5)])
            return '*[← Back to' in first_lines
    except Exception:
        return False


def has_frontmatter(filepath: Path) -> bool:
    """Check if file already has Jekyll frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line == '---'
    except Exception:
        return False


def add_frontmatter_and_back_reference(filepath: Path, readme_title: str, parent_title: str, dry_run: bool = False) -> bool:
    """Add Jekyll frontmatter and back-reference to the file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has proper frontmatter with parent
        if content.startswith('---') and f'parent: {parent_title}' in content[:500]:
            print(f"  ✓ {filepath.name} already has proper frontmatter")
            return False
        
        # If has frontmatter but wrong parent, or back-reference without frontmatter
        if content.startswith('*[← Back to'):
            # Remove existing back-reference
            lines = content.split('\n')
            # Remove lines until we get past the back-reference separator
            while lines and (lines[0].startswith('*[← Back to') or lines[0].strip() == '---' or lines[0].strip() == ''):
                lines.pop(0)
            content = '\n'.join(lines).lstrip()
        elif content.startswith('---'):
            # Has frontmatter but wrong parent - need to update
            # Extract existing frontmatter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # Keep content after frontmatter
                content = parts[2].lstrip()
        
        # Extract title (first heading from cleaned content)
        title = extract_first_heading(filepath)
        
        # Create frontmatter
        frontmatter = f"""---
layout: default
title: {title}
parent: {parent_title}
---

"""
        
        # Create back-reference  
        back_ref = f"*[← Back to {readme_title}](README.md)*\n\n---\n\n"
        
        # Combine: frontmatter + back-reference + content
        new_content = frontmatter + back_ref + content
        
        if dry_run:
            print(f"  [DRY RUN] Would add frontmatter and back-reference to {filepath.name}")
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ Added frontmatter and back-reference to {filepath.name}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error processing {filepath.name}: {e}")
        return False


def add_back_reference(filepath: Path, readme_title: str, dry_run: bool = False) -> bool:
    """Add back-reference to README.md at the top of the file."""
    if has_back_reference(filepath):
        print(f"  ✓ {filepath.name} already has back-reference")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        back_ref = f"*[← Back to {readme_title}](README.md)*\n\n---\n\n"
        new_content = back_ref + content
        
        if dry_run:
            print(f"  [DRY RUN] Would add back-reference to {filepath.name}")
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ Added back-reference to {filepath.name}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error adding back-reference to {filepath.name}: {e}")
        return False


def update_readme(readme_path: Path, new_section: str, dry_run: bool = False) -> bool:
    """Update README.md with the new Knowledge Articles section."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the existing Knowledge Articles section
        pattern = r'\n## Knowledge Articles\n.*?(?=\n---\n|\n## |\Z)'
        
        # Check if section exists
        if re.search(pattern, content, re.DOTALL):
            # Replace existing section
            new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
            action = "Updated"
        else:
            # Add before the final separator
            final_separator_pattern = r'\n---\n\n\*Explore specific topics'
            if re.search(final_separator_pattern, content):
                new_content = re.sub(
                    final_separator_pattern, 
                    new_section + '\n---\n\n*Explore specific topics',
                    content
                )
            else:
                # Append at the end if no clear insertion point
                new_content = content.rstrip() + '\n' + new_section
            action = "Added"
        
        if dry_run:
            print(f"  [DRY RUN] Would {action.lower()} Knowledge Articles section in README.md")
        else:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ {action} Knowledge Articles section in README.md")
        
        return True
    except Exception as e:
        print(f"  ✗ Error updating README.md: {e}")
        return False


def get_parent_title(directory: Path) -> str:
    """Get the parent title for Jekyll navigation."""
    dir_name = directory.name
    parent_map = {
        '00-framework': 'Framework',
        '01-systems-infrastructure': 'Systems & Infrastructure',
        '02-modeling-intelligence': 'Modeling & Intelligence',
        '03-product-strategy': 'Product & Strategy',
        '04-people-organization': 'People & Organization',
        '05-meta-learning': 'Meta-Learning'
    }
    return parent_map.get(dir_name, dir_name)


def process_directory(directory: Path, dry_run: bool = False) -> Dict[str, int]:
    """Process a single directory."""
    stats = {'files_found': 0, 'readme_updated': 0, 'refs_added': 0}
    
    print(f"\n📁 Processing: {directory}")
    
    readme_path = directory / 'README.md'
    if not readme_path.exists():
        print(f"  ⚠ No README.md found, skipping")
        return stats
    
    # Get directory title and parent
    dir_title = get_directory_title(readme_path)
    parent_title = get_parent_title(directory)
    
    # Scan for markdown files
    md_files = scan_directory(directory)
    stats['files_found'] = len(md_files)
    
    if not md_files:
        print(f"  ℹ No markdown files found")
        return stats
    
    print(f"  Found {len(md_files)} markdown file(s)")
    
    # Generate and update README section
    new_section = generate_readme_section(md_files)
    if update_readme(readme_path, new_section, dry_run):
        stats['readme_updated'] = 1
    
    # Add frontmatter and back-references to content files
    for file in md_files:
        if add_frontmatter_and_back_reference(file, dir_title, parent_title, dry_run):
            stats['refs_added'] += 1
    
    return stats


def main():
    """Main execution function."""
    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be modified\n")
    
    # Get project root (assuming script is in scripts/ folder)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Define directories to process
    directories = [
        project_root / '00-framework',
        project_root / '01-systems-infrastructure',
        project_root / '02-modeling-intelligence',
        project_root / '03-product-strategy',
        project_root / '04-people-organization',
        project_root / '05-meta-learning',
    ]
    
    total_stats = {'files_found': 0, 'readme_updated': 0, 'refs_added': 0}
    
    print("🚀 Starting Bidirectional Link Generator")
    print(f"📂 Project Root: {project_root}")
    
    for directory in directories:
        if directory.exists():
            stats = process_directory(directory, dry_run)
            for key in total_stats:
                total_stats[key] += stats[key]
    
    # Print summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"Total markdown files found: {total_stats['files_found']}")
    print(f"README files updated: {total_stats['readme_updated']}")
    print(f"Back-references added: {total_stats['refs_added']}")
    
    if dry_run:
        print("\n⚠️  This was a dry run. Run without --dry-run to apply changes.")
    else:
        print("\n✅ All updates completed successfully!")


if __name__ == '__main__':
    main()

