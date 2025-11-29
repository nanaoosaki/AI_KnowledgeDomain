---
layout: default
title: How to Deploy a Static Next.js Site on GitHub Pages for Free
parent: Product & Strategy
---

*[← Back to AI Product & Strategy](README.md)*

---

# How to Deploy a Static Next.js Site on GitHub Pages for Free

A complete step-by-step guide to deploying your Next.js application to GitHub Pages at no cost, with custom domain support.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Configure Next.js for Static Export](#step-1-configure-nextjs-for-static-export)
3. [Step 2: Create GitHub Actions Workflow](#step-2-create-github-actions-workflow)
4. [Step 3: Add Required Files](#step-3-add-required-files)
5. [Step 4: Push to GitHub](#step-4-push-to-github)
6. [Step 5: Enable GitHub Pages](#step-5-enable-github-pages)
7. [Step 6: Configure Custom Domain (Optional)](#step-6-configure-custom-domain-optional)
8. [Troubleshooting](#troubleshooting)
9. [Common Issues](#common-issues)

---

## Prerequisites

Before you begin, make sure you have:

- ✅ A Next.js application (version 13+)
- ✅ A GitHub account
- ✅ Git installed on your computer
- ✅ Node.js and npm/pnpm installed
- ✅ Basic knowledge of command line

---

## Step 1: Configure Next.js for Static Export

### 1.1 Update `next.config.mjs` (or `next.config.js`)

Add `output: 'export'` to enable static site generation:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',  // ← This is the key setting!
  
  // Recommended settings for GitHub Pages
  typescript: {
    ignoreBuildErrors: true,  // Optional: skip TS errors during build
  },
  images: {
    unoptimized: true,  // Required: GitHub Pages doesn't support Next.js Image Optimization
  },
  
  // Only needed if deploying to a subdirectory (e.g., username.github.io/repo-name)
  // basePath: '/your-repo-name',
  // assetPrefix: '/your-repo-name',
}

export default nextConfig
```

### 1.2 Update `package.json` Scripts

Make sure you have these scripts:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

---

## Step 2: Create GitHub Actions Workflow

GitHub Actions will automatically build and deploy your site whenever you push changes.

### 2.1 Create Directory Structure

```bash
mkdir -p .github/workflows
```

### 2.2 Create Workflow File

Create `.github/workflows/nextjs.yml`:

```yaml
name: Deploy Next.js to GitHub Pages

on:
  # Trigger on push to main branch
  push:
    branches: ["main"]
  
  # Allow manual trigger from Actions tab
  workflow_dispatch:

# Sets permissions for GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Prevent concurrent deployments
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Build job
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Install dependencies
        run: npm ci

      - name: Build with Next.js
        run: npm run build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./out

  # Deploy job
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**Key Points:**
- Runs on every push to `main` branch
- Uses `npm ci` for faster, reliable installs
- Builds Next.js app with `npm run build`
- Next.js exports static files to `out/` directory
- Uploads `out/` directory to GitHub Pages

---

## Step 3: Add Required Files

### 3.1 Create `.nojekyll` File

Create `public/.nojekyll` (empty file):

```bash
touch public/.nojekyll
```

**Why?** This tells GitHub Pages to skip Jekyll processing, which would ignore files starting with `_` (like Next.js's `_next` directory).

### 3.2 Add `.gitignore` (if not present)

Create or update `.gitignore`:

```
# Dependencies
node_modules
.pnp
.pnp.js

# Testing
coverage

# Next.js
.next/
out/
build
dist

# Production
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Environment
.env
.env*.local

# Vercel
.vercel

# TypeScript
*.tsbuildinfo
next-env.d.ts

# OS
.DS_Store
Thumbs.db
```

---

## Step 4: Push to GitHub

### 4.1 Initialize Git (if new project)

```bash
git init
git add .
git commit -m "Initial commit with GitHub Pages configuration"
```

### 4.2 Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click **"New repository"**
3. Name it (e.g., `my-nextjs-site`)
4. **Don't** initialize with README (you already have files)
5. Click **"Create repository"**

### 4.3 Push to GitHub

```bash
# Add remote
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to main branch
git branch -M main
git push -u origin main
```

---

## Step 5: Enable GitHub Pages

### 5.1 Configure GitHub Pages Settings

1. Go to your repository on GitHub
2. Click **"Settings"** (top right)
3. Click **"Pages"** in left sidebar
4. Under **"Build and deployment"**:
   - **Source**: Select **"GitHub Actions"**
   - (This should be auto-detected after pushing your workflow file)

### 5.2 Wait for Deployment

1. Go to **"Actions"** tab in your repository
2. You should see a workflow running
3. Wait for green checkmark ✓ (usually 2-5 minutes)

### 5.3 Access Your Site

Your site will be live at:
- `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

For example:
- `https://nanaoosaki.github.io/v0-nana-wang-personal-site/`

---

## Step 6: Configure Custom Domain (Optional)

Want to use your own domain like `mydomain.com` instead of `username.github.io`?

### 6.1 Create CNAME File

Create two `CNAME` files:

**Root `CNAME`:**
```bash
echo "yourdomain.com" > CNAME
```

**Public `CNAME`:**
```bash
echo "yourdomain.com" > public/CNAME
```

Both files should contain just your domain name:
```
yourdomain.com
```

### 6.2 Configure DNS Settings

Go to your domain registrar (GoDaddy, Namecheap, Porkbun, etc.) and add these DNS records:

**For root domain (yourdomain.com):**

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

**For www subdomain (www.yourdomain.com):**

| Type | Name | Value |
|------|------|-------|
| CNAME | www | YOUR-USERNAME.github.io |

### 6.3 Enable Custom Domain in GitHub

1. Go to repository **Settings** → **Pages**
2. Under **"Custom domain"**, enter: `yourdomain.com`
3. Click **"Save"**
4. Check **"Enforce HTTPS"** (wait for DNS to propagate first)

### 6.4 Wait for DNS Propagation

- DNS changes take 5 minutes to 48 hours (usually 10-30 minutes)
- Check status at: [https://www.whatsmydns.net/](https://www.whatsmydns.net/)
- Once propagated, GitHub will show: **"✓ DNS check successful"**

### 6.5 Push CNAME Files

```bash
git add CNAME public/CNAME
git commit -m "Add custom domain configuration"
git push
```

---

## Troubleshooting

### Issue: "Module not found" errors

**Solution:** Check your imports use relative paths, not absolute paths that depend on server-side resolution.

### Issue: Images not loading

**Solution:** 
1. Make sure `images: { unoptimized: true }` is in `next.config.mjs`
2. Use `Image` from `next/image` with `fill` prop or explicit width/height
3. Images should be in `public/` directory

### Issue: 404 on page refresh

**Solution:** This is normal for static sites. Users must navigate through your app, not refresh on subpages. Consider:
- Using hash routing: `#/about`
- Creating a 404.html that redirects to index.html

### Issue: CSS not loading

**Solution:** 
1. Check that `.nojekyll` file exists in `public/`
2. Verify `output: 'export'` is in `next.config.mjs`
3. Clear browser cache: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)

### Issue: Site shows old version

**Solution:**
1. Check GitHub Actions completed successfully (green ✓)
2. Hard refresh: `Ctrl + Shift + R`
3. Wait 1-2 minutes for CDN to update
4. Try incognito/private browsing mode

### Issue: Custom domain not working

**Solution:**
1. Verify DNS records are correct
2. Wait for DNS propagation (use whatsmydns.net)
3. Check that `CNAME` file is in both root and `public/`
4. Verify GitHub Pages shows "DNS check successful"

---

## Common Issues

### Server-Side Features Won't Work

GitHub Pages serves **static files only**. These Next.js features won't work:

❌ **Not Supported:**
- API Routes (`/pages/api/*`)
- Server-Side Rendering (SSR) with `getServerSideProps`
- Incremental Static Regeneration (ISR)
- Middleware
- Image Optimization (without `unoptimized: true`)

✅ **Supported:**
- Static Site Generation (SSG) with `getStaticProps`
- Client-Side Rendering (CSR)
- Static pages and components
- Client-side data fetching
- CSS/Tailwind
- React hooks

### Base Path for Repository Sites

If deploying to `username.github.io/repo-name`, uncomment in `next.config.mjs`:

```javascript
basePath: '/repo-name',
assetPrefix: '/repo-name',
```

And update all internal links to use the base path.

---

## Best Practices

### ✅ Do:

- Use `output: 'export'` in Next.js config
- Include `.nojekyll` in `public/` directory
- Use `images: { unoptimized: true }` for images
- Test locally with `npm run build` before pushing
- Use relative paths for assets
- Keep `CNAME` in both root and `public/` directories

### ❌ Don't:

- Use server-side features (API routes, SSR)
- Forget to add `.nojekyll` file
- Use Next.js Image Optimization without `unoptimized: true`
- Push `out/`, `.next/`, or `node_modules/` to Git
- Expect instant updates (allow 1-2 minutes for deployment)

---

## Updating Your Site

After making changes:

```bash
# 1. Make your changes
# 2. Commit and push
git add .
git commit -m "Update site content"
git push

# 3. GitHub Actions automatically rebuilds and deploys
# 4. Wait 2-5 minutes
# 5. Hard refresh browser to see changes
```

---

## Costs

**Everything is FREE! 🎉**

- ✅ GitHub Pages: Free
- ✅ GitHub Actions: 2,000 minutes/month free for public repos
- ✅ SSL Certificate: Free (auto-issued by GitHub)
- ✅ CDN: Free (global distribution)
- ✅ Bandwidth: Free (soft limit of 100GB/month)

**Only cost:** Custom domain registration ($10-15/year)

---

## Example Repository Structure

```
my-nextjs-site/
├── .github/
│   └── workflows/
│       └── nextjs.yml          ← GitHub Actions workflow
├── app/                        ← Next.js App Router
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── components/                 ← React components
│   └── Header.tsx
├── public/                     ← Static assets
│   ├── .nojekyll              ← Prevents Jekyll
│   ├── CNAME                  ← Custom domain
│   ├── favicon.ico
│   └── images/
├── .gitignore                 ← Git ignore rules
├── CNAME                      ← Custom domain (root)
├── next.config.mjs            ← Next.js config
├── package.json               ← Dependencies
├── tsconfig.json              ← TypeScript config
└── README.md                  ← Documentation
```

---

## Summary Checklist

Before deploying, verify:

- [ ] ✅ `output: 'export'` in `next.config.mjs`
- [ ] ✅ `images: { unoptimized: true }` in `next.config.mjs`
- [ ] ✅ `.github/workflows/nextjs.yml` created
- [ ] ✅ `public/.nojekyll` file exists
- [ ] ✅ `.gitignore` excludes `out/`, `.next/`, `node_modules/`
- [ ] ✅ Pushed to GitHub
- [ ] ✅ GitHub Pages source set to "GitHub Actions"
- [ ] ✅ Green checkmark in Actions tab
- [ ] ✅ (Optional) CNAME files for custom domain
- [ ] ✅ (Optional) DNS records configured

---

## Resources

### Official Documentation
- [Next.js Static Exports](https://nextjs.org/docs/app/building-your-application/deploying/static-exports)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Tools
- [DNS Checker](https://www.whatsmydns.net/) - Check DNS propagation
- [GitHub Status](https://www.githubstatus.com/) - Check GitHub service status

### Example Sites
- This guide's repo: [nanaoosaki/v0-nana-wang-personal-site](https://github.com/nanaoosaki/v0-nana-wang-personal-site)
- Live example: [nanawang.dev](https://nanawang.dev)

---

## FAQ

**Q: Can I use Next.js 14/15 with App Router?**  
A: Yes! This guide works with Next.js 13+ and App Router.

**Q: Do I need Vercel?**  
A: No! GitHub Pages is completely independent and free.

**Q: Can I use TypeScript?**  
A: Yes! TypeScript is fully supported.

**Q: How long does deployment take?**  
A: Usually 2-5 minutes after pushing to GitHub.

**Q: Can I deploy multiple sites?**  
A: Yes! Each repository can be a separate site.

**Q: Is there a file size limit?**  
A: GitHub Pages recommends keeping sites under 1GB.

**Q: Can I use a custom domain without HTTPS?**  
A: HTTPS is automatic and free with GitHub Pages. Can't be disabled.

**Q: What if I want server-side features?**  
A: Use Vercel, Netlify, or AWS instead. GitHub Pages is static-only.

---

## Conclusion

Congratulations! 🎉 You now have a free, fast, globally-distributed website powered by:

- ✅ Next.js (modern React framework)
- ✅ GitHub Pages (free hosting)
- ✅ GitHub Actions (automatic deployment)
- ✅ SSL/HTTPS (secure by default)
- ✅ Global CDN (fast worldwide)

**Total cost: $0/month** (or $10-15/year if using custom domain)

---

## Need Help?

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. View build logs in GitHub Actions tab
3. Search GitHub Issues for similar problems
4. Ask in [GitHub Community Forum](https://github.community/)

Happy deploying! 🚀

---

**Last Updated:** November 26, 2024  
**Tested with:** Next.js 16.0, React 19, GitHub Actions 2024

