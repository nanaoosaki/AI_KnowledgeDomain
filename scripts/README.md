# Knowledge Domain Automation Scripts

This directory contains automation scripts for maintaining the AI Knowledge Domain.

## Available Scripts

### `link_knowledge_articles.py`

Automatically creates bidirectional links between README.md files and knowledge articles.

**What it does:**
1. Scans each domain directory for markdown files
2. Extracts titles from the first heading in each file
3. Updates README.md with a "Knowledge Articles" section containing links to all files
4. Adds back-reference links at the top of each article pointing back to README.md

**Usage:**

```bash
# Preview changes without modifying files
python scripts/link_knowledge_articles.py --dry-run

# Apply changes
python scripts/link_knowledge_articles.py
```

**Features:**
- URL-encodes filenames with spaces automatically
- Handles files without .md extension (like 'imperative vs declarative')
- Skips binary files and directories
- Won't duplicate back-references if they already exist
- Provides detailed progress output

**Requirements:**
- Python 3.7+
- No external dependencies (uses only standard library)

## Creating New Articles

When you create a new markdown file in any domain directory:

1. Write your article with at least one heading (`#` or `##`)
2. Run the link script: `python scripts/link_knowledge_articles.py`
3. The script will automatically:
   - Add your article to the README.md
   - Add a back-reference link at the top of your article

## Directory Structure

The script processes these directories:
- `00-framework/`
- `01-systems-infrastructure/`
- `02-modeling-intelligence/`
- `03-product-strategy/`
- `04-people-organization/`
- `05-meta-learning/`

Each directory should have a `README.md` file.

## Troubleshooting

**Script doesn't find my file:**
- Ensure your file has a `.md` extension or is a text file
- Check that it's not hidden (doesn't start with `.`)
- Verify it's not in a subdirectory (script only processes files in the root of each domain)

**Links aren't working:**
- The script URL-encodes filenames, which is correct for markdown
- If links still don't work, check for special characters in filenames

**Back-reference already exists:**
- The script won't duplicate back-references
- If you need to update the reference, manually remove the old one first

## Future Enhancements

Potential improvements for this tooling:

- [ ] Generate a site-wide index/table of contents
- [ ] Create cross-domain reference linking
- [ ] Auto-generate tags/categories from content
- [ ] Build a knowledge graph visualization
- [ ] Add support for subdirectories (foundational/intermediate/advanced)
- [ ] Generate frontmatter automatically for Jekyll
- [ ] Link validation and broken link detection

