# Python 101 for Pharmacists

Modern, web-styled handbook built from Markdown.

This project contains:

- `handbook.md` - the full handbook source content
- `handbook-web.html` - interactive web viewer (modern UI, TOC, code highlighting, copy buttons, collapsible solutions/outputs)

## Run Locally

1. Open a terminal in this folder:

   ```bash
   cd "/home/brainart/Desktop/Python 101"
   ```

2. Start a local web server:

   ```bash
   python3 -m http.server 8000
   ```

3. Open in your browser:

   [http://localhost:8000/handbook-web.html](http://localhost:8000/handbook-web.html)

## How It Works

- `handbook-web.html` loads `handbook.md` dynamically in the browser.
- Markdown is rendered using `marked.js`.
- Code snippets are highlighted with `highlight.js`.
- Additional UI enhancements are applied at runtime:
  - styled table of contents with active section tracking
  - card-based visual components across sections
  - IDE-like code blocks with copy action
  - collapsible sections for:
    - Complete Working Solution
    - Complete Reference Solution
    - Expected Output

## Deploy (Share Online)

### Option 1: GitHub Pages

1. Push this folder to a GitHub repository.
2. Go to **Settings -> Pages**.
3. Choose **Deploy from a branch**.
4. Select `main` branch and `/ (root)` folder.
5. Open the generated Pages URL.

### Option 2: Netlify

1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop this project folder.
3. Netlify gives you a live URL instantly.

## Notes

- Use a local server (not `file://`) so `fetch("./handbook.md")` works correctly.
- After editing `handbook.md` or `handbook-web.html`, refresh the browser to see changes.
