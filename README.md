# Portfolio Website

A professional portfolio website built with Quarto, showcasing projects, skills, and professional experience.

## Structure

- **index.qmd** - Landing page with hero section, about snippet, featured projects, and skills overview
- **about.qmd** - Detailed personal background and professional journey
- **skills.qmd** - Comprehensive technical skills and expertise
- **resume.qmd** - Full professional experience and education
- **projects.qmd** - Detailed project descriptions and achievements
- **styles.css** - Custom styling for a modern, professional look

## Prerequisites

You need to have Quarto installed. If you don't have it:

```bash
# On macOS with Homebrew
brew install quarto

# Or download from https://quarto.org/docs/get-started/
```

## How to Preview

1. Open terminal in this directory
2. Run the preview command:

```bash
quarto preview
```

This will:
- Build the website
- Open it in your default browser
- Auto-reload when you make changes

## How to Build

To build the static website files:

```bash
quarto render
```

The built website will be in the `docs/` folder, ready to deploy to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

## Deploying to GitHub Pages

1. Push this repository to GitHub
2. Go to Settings > Pages
3. Set Source to "Deploy from a branch"
4. Select branch: main, folder: /docs
5. Save and wait for deployment

Your site will be available at: `https://[username].github.io/[repo-name]/`

## Customization

### Colors
Edit color scheme in `styles.css`:
```css
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  --accent-color: #e74c3c;
}
```

### Content
- Update each `.qmd` file with your content
- Add more projects to `projects.qmd`
- Update skills in `skills.qmd`
- Modify resume in `resume.qmd`

### Navigation
Edit `_quarto.yml` to add/remove pages from navbar

## Features

- Responsive design (mobile-friendly)
- Modern gradient hero section
- Project cards with hover effects
- Clean typography
- Professional color scheme
- Easy navigation
- Fast loading

## Support

For Quarto documentation: https://quarto.org/docs/websites/
