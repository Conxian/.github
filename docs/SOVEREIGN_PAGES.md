# Sovereign Documentation Strategy: GitHub Pages Implementation

## Overview

Conxian Labs utilizes a decentralized yet unified documentation strategy. We leverage GitHub Pages for project-specific documentation and Render for high-performance application hosting. This ensures that documentation for each component of the ecosystem is co-located with its source code while remaining accessible through a unified portal.

## 1. The Central Hub: `conxian.github.io`

The root repository `Conxian/Conxian.github.io` (or the `.github` repository documentation hub) serves as the canonical landing page for all Conxian ecosystem documentation. It provides a directory of all project-specific documentation sites.

## 2. Project-Specific Documentation

Every public repository in the Conxian organization **MUST** enable GitHub Pages to host its technical documentation and API references.

- **Path:** `https://conxian.github.io/<repository-name>/`
- **Source:** The preferred source is the `/docs` folder on the `main` branch.
- **Automation:** Repositories should use a standardized GitHub Action (e.g., `deploy-docs.yml`) to automate the build and deployment of documentation on every push to `main`.

## 3. Unified Branding & Navigation

To provide a seamless experience, all project documentation sites should:
- Use consistent styling (e.g., shared CSS or documentation frameworks like MkDocs/Docusaurus).
- Include a "Global Header" or "Back to Hub" link pointing to `https://conxian.github.io/`.
- Link to the organization's `repository-taxonomy.md` to provide context on the repository's role.

## 4. Custom Domain Mapping

While repositories are hosted on GitHub Pages for resilience, the canonical public identity is unified under the primary corporate domain.

- **Corporate Site:** Hosted on Render, mapped to `conxian-labs.com`.
- **Documentation Portal:** Mapped to `docs.conxian-labs.com` (pointing to the GitHub Pages hub).

## 5. Implementation Steps for New Repos

1. **Initialize Docs:** Create a `/docs` directory in the repository root.
2. **Standard Files:** Add an `index.md` and ensure the repository's `README.md` is synced or linked within the docs.
3. **Enable Pages:** Go to `Settings > Pages` and set the source to `GitHub Actions`.
4. **Deploy Workflow:** Add a `.github/workflows/deploy-docs.yml` file (templated from the `.github` repository).
5. **Cross-Link:** Ensure the repository `README.md` prominently links to its GitHub Pages URL.

---

_Sovereignty through transparency. Documentation is the map of our autonomous landscape._
