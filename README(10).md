# JASS X / TWITTER STUDIO

A single-file PySide6 desktop application for organizing and discovering a curated collection of 100 X (Twitter) pages focused on AI, technology, research, developers, open source, cloud and innovation.

## Features

- **100 curated pages** included out of the box
- Modern dark **Studio-style dashboard**
- **Dashboard** with summary statistics and quick access
- **All Pages** directory
- **Favorites** view
- **Categories** view
- Search by page name, handle or category
- Category filter
- **Open ↗** button for every page
- Double-click a page to open its X profile
- Add your own X/Twitter pages
- Local SQLite database
- Data persists between launches
- Single Python file
- No external database server required
- Responsive table and navigation layout

## Categories

The starter directory covers areas such as:

- AI companies and labs
- AI researchers and educators
- AI developers
- AI infrastructure
- Machine learning frameworks
- Developer tools
- Cloud and DevOps
- Open source
- AI hardware
- AI image, video, audio and music
- Data and ML platforms
- Technology leaders

## Requirements

- Python 3.10+
- PySide6

Install PySide6 if needed:

```powershell
py -m pip install PySide6
```

## Run

Place `x_twitter_studio_enhanced.py` in your Downloads/project folder and run:

```powershell
cd C:\Users\singh\Downloads
py x_twitter_studio_enhanced.py
```

## Data Storage

The application creates its local database at:

```text
~/.jass_x_studio/x_studio.db
```

On Windows this is normally under your user profile.

The database stores:

- Page name
- X/Twitter handle
- Category
- Favorite status
- Notes

The starter 100 pages are inserted automatically when the database is first created. Existing pages are not duplicated.

## Adding Pages

Use:

**＋ Add Page**

Enter:

1. Page name
2. X/Twitter handle
3. Category

The handle can be entered with or without `@`.

## Web Directory

`index.html` is a lightweight browser version of the same 100-page directory.

Open it directly in Firefox or another browser. It provides:

- Search
- Category information
- 100 clickable X profile links
- No Python installation required

## Project Files

```text
JASS X / TWITTER STUDIO/
├── x_twitter_studio_enhanced.py
├── index.html
└── README.md
```

## Design Philosophy

JASS X / TWITTER STUDIO is intended as a **personal discovery and organization tool**, not an automated social-media bot.

It does not automatically follow accounts or perform actions on behalf of the user. Selecting **Open ↗** takes the user to the actual X profile, where the user can decide what to do.

## Future Ideas

Possible additive improvements:

- Favorites toggle directly from the table
- Notes editor for each page
- Custom collections
- Recently opened pages
- Import/export CSV
- Import/export JSON
- More curated lists
- In-app preview cards
- Optional X API integration
- Backup and restore of the local database

## License

Personal project. Add a license here if you decide to publish the project publicly.
