# Tilawah Tracker

## Overview

A small, private Flask app for tracking daily Quran reading through the 604-page Madinah Mushaf.
Built spec-first.

## Architecture

```
tilawah-tracker/
├── app.py            # All routes
├── db.py             # All database code — empty until step 1
├── tilawah.db        # SQLite database — created by db.py, never committed
├── templates/
│   ├── base.html     # Shared layout — every page extends it
│   └── *.html        # One template per page
├── static/
│   └── style.css     # All styles
├── tests/            # pytest tests — empty until we write tests
├── pyproject.toml    # Dependencies — managed by uv
└── README.md         # High-level product overview and scope
```

Key files:

- `app.py` — every route lives here. Routes stay thin: read the request, call a function,
  render a template.
- `db.py` — all database code, and only here — never inside a route. It's empty until step 1:
  don't assume any database helper exists until that step builds it.
- `tilawah.db` — the SQLite database, created by `db.py`. It's in `.gitignore`: never commit it
  or edit it by hand.
- `templates/base.html` — the shared layout. Every new page is a new template that extends it.
- `static/style.css` — all styles. Never inline `<style>` tags.
- `tests/` — one `test_<feature>.py` per feature. Empty until we write tests.
- `README.md` — the product overview and scope.

Reading rules (pages read, forward-only checks) live in plain functions, not inside routes,
so they can be tested on their own.

## Code style

- Python: PEP 8 — `snake_case` for functions and variables, `UPPER_CASE` for constants
- Type hints on every function's parameters and return value
- Routes do one job: read the request, call a function, render a template
- Templates: `url_for()` for every internal link — never hardcode URLs
- Errors: `abort()` for HTTP errors — never return a bare error string
- SQL: always parameterized (`?` placeholders) — never f-strings in SQL
- Input: validate every form value on the server — never trust the browser

## Tools & libraries

- uv only — never `pip`, never `python -m venv`
- Flask only — no FastAPI, no Django
- SQLite through the built-in `sqlite3` only — no PostgreSQL, no SQLAlchemy or other ORM
- SQLite foreign keys are off by default — every connection must run `PRAGMA foreign_keys = ON`
- No JavaScript frameworks — no React, no jQuery, no npm packages
- No new dependencies without agreement
- Python 3.10+

## Commands

```bash
uv sync                 # install dependencies
uv run python app.py    # run at http://localhost:5001 — keep 5001 (macOS uses 5000)
uv run pytest           # run the tests — none yet
```

## Critical rules

- The user records only a stop page and an optional ayah; the app sets the date.
- Pages read = this stop − previous stop. A new khatma starts from 0.
- Forward only: a new stop must be > the last stop and ≤ 604. Equal → ignored. Lower → rejected.
- No new stops after 604 until **Finish khatma** is used; it is only available at 604.
- Entries are never edited or deleted. The ayah is display-only, never used in calculations.
- Every account sees only its own data, enforced on the server, including typed URLs.
- Juz and hizb come from the page number via a fixed 604-page table generated once.
- Build only what the current spec asks for. Nothing out of scope without an approved spec.

### Build status

| #   | Step                                      | Status      |
| --- | ----------------------------------------- | ----------- |
| 1   | Foundation and persistence                | Not started |
| 2   | Landing page                              | Not started |
| 3   | Register                                  | Not started |
| 4   | Login, logout, protected pages            | Not started |
| 5   | Entries and forward-only rules            | Not started |
| 6   | Record a stop                             | Not started |
| 7   | Dashboard and khatma progress             | Not started |
| 8   | History                                   | Not started |
| 9   | Summary statistics                        | Not started |
| 10  | Yearly summary                            | Not started |
| 11  | Finish khatma, start a new one            | Not started |
| 12  | Ownership checks, end-to-end verification | Not started |
