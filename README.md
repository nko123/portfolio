# Nkem Okweye · Portfolio

Personal portfolio site for Nkem Okweye, data scientist at Georgetown University School of Medicine and MS Data Science & Analytics candidate. Built with [Quarto](https://quarto.org) and published with GitHub Pages from the `docs/` folder.

**Live site:** https://nko123.github.io/portfolio

## Structure

```
index.qmd            Home: intro, impact numbers, experience timeline, featured projects, contact
work.qmd             All projects (Quarto listing of projects/, filterable by category)
projects/*.qmd       One case study per project
about.qmd            Story and skills
resume.qmd           Full résumé
404.qmd              Not-found page
assets/
  img/               Project covers and portrait
  logos/             Employer and school logos
  theme-light.scss   Light palette (Bootstrap variables + CSS tokens)
  theme-dark.scss    Dark palette, used by the navbar toggle
  project-card.ejs   Card template for the Work listing
  favicon.svg
styles.css           Layout and components, colored only through the theme tokens
docs/                Rendered site (generated, do not edit by hand)
```

## Add a project

1. Create `projects/<slug>.qmd`.
2. Fill in the front matter. These fields drive the card on the Work page:

```yaml
---
title: "Project title"
subtitle: "One-line summary"
description: "Two sentences for the card."
date: 2026-05-01            # used for sorting
image: ../assets/img/<cover>.jpg
categories: [Statistics, R]
course: "DSAN 5100 · Georgetown"
cat_label: "Statistics · R" # label shown on the card image
stat: "+5.47 pts"           # headline result
stat_text: "swing vs. blue states"
---
```

3. To feature it on the homepage, add a card to the `#work` section of `index.qmd`.

## Preview and publish

```bash
quarto preview      # live preview
quarto render       # build into docs/
git add -A && git commit -m "Update site" && git push
```

GitHub Pages serves the `main` branch, `/docs` folder.

## Design

"Studio Portrait": deep teal taken from the portrait backdrop, muted gold for numbers, Instrument Serif headlines with Figtree body text. Change colors in `assets/theme-light.scss` and `assets/theme-dark.scss`; every component reads from those tokens.
