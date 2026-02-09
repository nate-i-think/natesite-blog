# CLAUDE.md

This file provides guidance to Claude Code when working with the Tidbits blog.

## Commands

```bash
bundle install          # Install Ruby dependencies
jekyll serve            # Dev server at localhost:4000 (auto-rebuilds on changes)
```

## Project Structure

```
/
├── _layouts/
│   └── default.html      # Base HTML template
├── _site/                # Generated static output (do not edit)
├── assets/
│   └── css/
│       └── style.css     # All styling
├── index.md              # Homepage
├── _config.yml           # Jekyll config
├── Gemfile               # Dependencies (Jekyll 4.3)
└── CLAUDE.md             # This file
```

## Architecture

Jekyll static site for the Tidbits blog, hosted at tidbits.nathanmyers.co via Netlify.

The parent site (nathanmyers.co) lives in the parent directory. This blog is a separate Jekyll project with its own config and build.

## Adding Pages

Create a markdown file with front matter:

```yaml
---
layout: default
title: Page Title
---
```

## Adding Posts

Create a file in `_posts/` named `YYYY-MM-DD-title.md` with front matter:

```yaml
---
layout: default
title: Post Title
---
```
