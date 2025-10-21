# GitHub Pages Setup Instructions

## Quick Setup Steps

1. **Go to your repository**: https://github.com/nanaoosaki/AI_KnowledgeDomain

2. **Click the "Settings" tab** (top right of the repo)

3. **In the left sidebar, scroll down and click "Pages"**

4. **Under "Build and deployment"**:
   - **Source**: Select **"GitHub Actions"** from the dropdown
   - (NOT "Deploy from a branch")

5. **Click "Save"** if there's a save button

6. **Wait 2-3 minutes** for the first build

7. **Visit your site**: https://nanaoosaki.github.io/AI_KnowledgeDomain

## What You'll See

**Before (GitHub repo view)**:
- Plain markdown files
- GitHub's default styling
- No navigation sidebar

**After (GitHub Pages site)**:
- Beautiful dark-themed documentation
- Searchable navigation sidebar
- Organized by domains
- Mobile-responsive
- Professional documentation layout

## Check Build Status

After enabling Pages, check if the build is working:

1. Go to the **"Actions"** tab in your repo
2. Look for **"Deploy Jekyll site to Pages"** workflow
3. It should show:
   - Green checkmark ✓ = Success
   - Yellow circle = Building
   - Red X = Failed (let me know if this happens)

## Troubleshooting

If the site doesn't work after 5 minutes:

1. Check Actions tab for errors
2. Make sure Source is set to "GitHub Actions" (not branch)
3. Verify the workflow file exists: `.github/workflows/pages.yml`

## Your Site URL

Once enabled:
**https://nanaoosaki.github.io/AI_KnowledgeDomain**

This is completely different from the repository URL!

