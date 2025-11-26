# Quick Start: Managing Knowledge Article Links

This guide shows you how to maintain bidirectional links between your README files and knowledge articles.

## What Was Set Up

✅ **Bidirectional Linking System:**
- All knowledge articles now link back to their README.md
- All README.md files have a "Knowledge Articles" section listing the articles
- Automated script to maintain these links as you add new content

## Adding New Articles

### Step 1: Create Your Article

Create a new markdown file in any domain directory:

```markdown
# Your Article Title

Your content here...
```

**Important:** Make sure your article has at least one heading (`#` or `##`) at the top. The script uses this as the link text.

### Step 2: Run the Link Script

```bash
# Preview what will change (recommended first run)
python scripts/link_knowledge_articles.py --dry-run

# Apply the changes
python scripts/link_knowledge_articles.py
```

### Step 3: Verify

The script will automatically:
- ✓ Add your article to the domain's README.md
- ✓ Add a back-reference link at the top of your article
- ✓ URL-encode any special characters in filenames

## Current Organization

Your knowledge base is organized into domains:

```
00-framework/          - Meta concepts about the framework itself
01-systems-infrastructure/  - Engineering and deployment
02-modeling-intelligence/   - Models, training, and AI concepts
03-product-strategy/        - Product and business aspects
04-people-organization/     - Team and organizational topics
05-meta-learning/          - Learning and skill development
```

## Examples

### Before Running Script

**Your new file:** `01-systems-infrastructure/understanding docker containers.md`

```markdown
# Understanding Docker Containers

Docker containers are...
```

### After Running Script

**README.md gets updated:**
```markdown
## Knowledge Articles

### Core Topics

- [Understanding Docker Containers](understanding%20docker%20containers.md)
- [Other Article](other-article.md)
...
```

**Your file gets a back-reference:**
```markdown
*[← Back to Systems & Infrastructure](README.md)*

---

# Understanding Docker Containers

Docker containers are...
```

## Handling Special Cases

### Files Without .md Extension

The script handles files like `imperative vs declarative` (no extension).
No special action needed - it works automatically.

### Files with Spaces in Names

Filenames with spaces are automatically URL-encoded:
- `my article.md` → `my%20article.md` in links
- Links will work correctly

### Updating Existing Links

If you rename a file or change its title:

1. Rename/edit the file
2. Run the script again: `python scripts/link_knowledge_articles.py`
3. The script will update all links automatically

### Removing an Article

1. Delete the markdown file
2. Run the script: `python scripts/link_knowledge_articles.py`
3. The script will remove it from README.md automatically

## Troubleshooting

### "Script doesn't find my file"

**Check:**
- ✓ File is in a domain directory (not in a subdirectory like `foundational/`)
- ✓ File has `.md` extension or is a text file
- ✓ File doesn't start with `.` (hidden)

### "Links aren't working on GitHub/Jekyll"

**Solution:**
The script URL-encodes filenames, which is correct. If links still don't work:
- Check for unsupported characters in filenames
- Consider renaming files to use hyphens instead of spaces

### "Back-reference looks wrong"

The back-reference format is:
```markdown
*[← Back to Domain Title](README.md)*

---
```

If it's missing or malformed:
1. Manually remove any existing back-reference
2. Run the script again

## Best Practices

### File Naming

✅ **Good:**
- `how-to-deploy-models.md`
- `attention mechanisms explained.md`
- `understanding-transformers.md`

❌ **Avoid:**
- Files with special characters: `what's-this?.md`
- Very long filenames
- Names without clear meaning

### Article Structure

Start each article with a clear heading:

```markdown
# Article Title

Brief introduction...

## Section 1
...
```

This helps the script extract a good title for the link.

### Commit Workflow

```bash
# 1. Create/edit articles
vim 01-systems-infrastructure/new-article.md

# 2. Run link script
python scripts/link_knowledge_articles.py

# 3. Review changes
git diff

# 4. Commit everything together
git add .
git commit -m "Add new article on [topic]"
```

## Script Options

```bash
# Dry run (preview changes without modifying files)
python scripts/link_knowledge_articles.py --dry-run

# Normal run (apply changes)
python scripts/link_knowledge_articles.py
```

## When to Run the Script

Run the script whenever you:
- ✓ Add a new article
- ✓ Rename an article
- ✓ Delete an article
- ✓ Change an article's main heading
- ✓ Want to verify all links are up to date

## Advanced: Subdirectories

Currently, the script only processes files in the root of each domain directory.

If you want to organize articles in subdirectories (like `foundational/`, `intermediate/`, `advanced/`), you'll need to either:

1. Keep a flat structure (current approach)
2. Modify the script to recursively scan subdirectories
3. Create separate README files in each subdirectory

The current flat structure is simpler and works well for most use cases.

---

**Need help?** Check `scripts/README.md` for more details about the automation script.

