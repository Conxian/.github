# Sovereign Documentation Strategy: GitHub Pages Implementation

## Overview

Conxian Labs utilizes a decentralized yet unified documentation strategy. We leverage GitHub Pages for project-specific documentation and Render for high-performance application hosting.

## 1. The Central Hub: `conxian.github.io`

The root repository `Conxian/Conxian.github.io` serves as the canonical landing page for all Conxian ecosystem documentation.

## 2. Project-Specific Documentation

Every public repository in the Conxian organization SHOULD enable GitHub Pages.

- **Path:** `https://conxian.github.io/<repository-name>/`
- **Source:** Preferred source is the `/docs` folder on the `main` branch or a dedicated `gh-pages` branch.
- **Automation:** Use the "Static Site" GitHub Action for automated deployments.

## 3. Custom Domain Mapping

While repositories are hosted on Render and GitHub Pages, the canonical public identity remains `conxian-labs.com`.

- **Primary Site:** Hosted on Render, mapped to `conxian-labs.com`.
- **Documentation:** Mapped to `docs.conxian-labs.com` (pointing to GitHub Pages) or kept as sub-paths.

## 4. Implementation Steps for New Repos

1. Create a `/docs` directory.
2. Add an `index.md` or `index.html`.
3. Go to Settings > Pages and set the source to GitHub Actions or the `/docs` folder.
4. Ensure the repository README links to its respective GitHub Pages URL.

---

_Sovereignty through transparency._
