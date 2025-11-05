
Economic Evolution Enterprise – Web Asset Pack
=============================================

Contents
--------
- logo_* (stacked, horizontal, icon) in color, black, and white — PNG + SVG (PNG-wrapped)
- transparent-background exports (default) and *_on_white convenience renders
- Favicon set: PNG sizes [16, 32, 48, 64, 96, 128, 180, 192, 256, 512] and favicon.ico (multi-size)
- Social icons: square and circle (400/800/1024)

Recommended Google Fonts (Organic/Humanist)
------------------------------------------
Headings (H1–H3): **Nunito** (700/800)
Body (P): **Source Sans 3** (400/600)
UI/Small: **Work Sans** (500/600)

CSS Import (no @import in production; prefer <link>)
----------------------------------------------------
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Source+Sans+3:wght@400;600&family=Work+Sans:wght@500;600&display=swap" rel="stylesheet">

Tailwind config suggestion
-------------------------
theme.extend.fontFamily = {
  'sans': ['Source Sans 3', 'system-ui', 'ui-sans-serif', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'],
  'heading': ['Nunito', 'ui-sans-serif', 'system-ui', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial'],
  'ui': ['Work Sans', 'ui-sans-serif', 'system-ui', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial'],
}

Example HTML favicons
---------------------
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon_32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon_192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon_180.png">
<link rel="icon" href="/assets/favicon.ico">

Notes
-----
- PNG-based SVGs are provided for convenience; if you later obtain true vector artwork, replace these.
- Colors were subtly contrast-optimized for web legibility while preserving brand tone.
