# Tilawah Tracker

A small, private web app for tracking daily Quran reading through the 604-page
Madinah Mushaf. You record where you stopped; the app counts the pages, keeps
your history, and tracks each khatma.

It answers three questions: where do I continue, how much have I read, and how
has my reading developed over time?

Built in the open in the TechSpire series _Spec-Driven Development_: one
feature per episode, each from a written spec. The product stays deliberately
small; the sophistication comes from the specs and the workflow, not from
features.

This README is the product overview: what we're building, its rules, and its scope.
Each feature's detailed requirements live in its own spec.

## Terms

- **Stop**: the page number you record after reading. Each stop is one entry.
- **Reading day**: a date with at least one recorded stop.
- **Khatma**: one full read of the Mushaf, page 1 to 604.

## How it works

- You record only a **stop page** and, optionally, the **ayah**. The app sets the date.
- Pages read = this stop − your previous stop. A new khatma starts from 0.
  Record 10, then 12: that's 10 pages, then 2 pages.
- Several stops on the same day add up into one reading day.
- At page 604, a **Finish khatma** action appears. It records the khatma and
  starts a new one from page 1.

## Rules and restrictions

- **Reading only moves forward.** A new stop must be higher than your last stop
  and no higher than 604.
- A stop **equal** to your last stop is ignored. A **lower** stop is rejected.
- **Finish khatma** is available only at page 604. Until you use it, no new stops
  can be recorded.
- Recorded entries **can't be edited or deleted**, and you can't change your
  position or the date by hand.
- The **ayah** is shown back to you only. It isn't used in any calculation or
  checked against the page.
- **Private by default.** Every account sees only its own data, enforced on the
  server, including for manually typed URLs.
- Juz and hizb come from the page number, using a fixed 604-page table generated
  once during development.

## Pages

- **Landing**: what the app is, with links to register and log in
- **Register / Login / Logout**
- **Dashboard**: last stop; position (page, juz, hizb); this khatma's progress;
  total pages; reading days; average pages per reading day; completed khatmas;
  recent reading days; **Finish khatma** at page 604
- **Record a stop**: shows your last stop; takes a stop page and an optional ayah
- **History**: reading days, newest first, with the pages read each day
- **Yearly summary**: for a chosen year: pages, reading days, average pages per
  reading day, khatmas completed

## Out of scope

- Quran text, translation, tafsir, or surah and ayah data
- Reading time, duration, or speed
- Personal notes
- Entering or changing the date
- Goals, targets, streaks, schedules, or reminders
- Editing or deleting entries
- Starting a new khatma before page 604
- More than one Mushaf edition
- Groups, sharing, or any social features; any role besides a registered user
- Audio, tajweed, or memorization tracking
- Import or export, attachments, or runtime integrations
- AI features inside the app
- A native mobile app

Nothing here gets added without an approved change spec.

## Build order

Each step gets its own spec before any code:

1. Foundation and persistence
2. Landing page
3. Register
4. Login, logout, and protected pages
5. Entries and the forward-only rules
6. Record a stop
7. Dashboard and khatma progress
8. History
9. Summary statistics
10. Yearly summary
11. Finish khatma and start a new one
12. Ownership checks and end-to-end verification

## Current state

This is the **designed app shell** from Episode 2: the pages match the target
design, but the data is hardcoded and the forms (record a stop, login, register)
don't work yet. Where the shell disagrees with this README, the shell will change. In
particular, the shell's monthly goal check, target pages per day and on-track
check will be removed.

Current shell pages:

- **Today (`/`)**: progress card, your _last stop_, and the record form
- **Progress (`/progress`)**: this cycle's progress
- **Khatmas (`/khatmas`)**: completed khatmas and totals
- **Login / Register**: placeholder forms, not wired up yet

## Run it

You'll need [uv](https://docs.astral.sh/uv/) installed.

```bash
uv sync                 # create the environment + install Flask
uv run python app.py    # start the app
```

Then open **http://localhost:5001** in your browser.
Press `Ctrl + C` in the terminal to stop it.

> Used `venv` + `pip` before? `uv sync` replaces `python -m venv` + activate +
> `pip install`, and `uv run` runs the app without activating anything.

## Development conventions

- **Use uv for everything.** Never `pip` or `python -m venv`.
- **Stack:** Flask, Jinja templates, and one stylesheet (`static/style.css`).
  No JavaScript frameworks.
- **Don't add a dependency** without agreeing on it first.
- **Spec first:** every feature starts from a written spec, and the code does
  only what that spec asks for.

## Coding conventions

- **PEP 8 style:** 4-space indentation; `snake_case` for functions and variables;
  `UPPER_CASE` for constants.
- **Type hints** on every function's parameters and return value.
- **Thin routes:** a route reads the request, calls a function, and renders a
  template. Reading rules (pages read, forward-only checks) live in plain
  functions, so they can be tested on their own.
- **Validate on the server:** never trust form values; check every input before
  using it.
- **Safe SQL:** always use query parameters; never build SQL with string formatting.
- **Where things belong:** routes in `app.py`; all database code in `db.py`,
  never inside a route; every page is a template extending `base.html`; all
  styles in `static/style.css`, no inline `<style>` tags.
- **Templates:** use `url_for()` for every internal link; never hardcode URLs.
- **Errors:** use `abort()` for HTTP errors, not plain error strings.
- **Database:** SQLite through Python's built-in `sqlite3` module; no ORM.
- **Port 5001:** don't change it (macOS uses 5000 for AirPlay).

## Project structure

```
tilawah-tracker/
├── app.py              # routes + placeholder data
├── db.py               # all database code (empty until step 1)
├── tilawah.db          # SQLite database (created by db.py, not committed)
├── pyproject.toml      # dependencies (managed by uv)
├── templates/
│   ├── base.html       # top nav + page layout
│   ├── index.html      # Today: progress card + last stop + record form
│   ├── progress.html   # This cycle's progress
│   ├── khatmas.html    # completed khatmas + totals
│   ├── login.html      # placeholder login
│   └── register.html   # placeholder register
├── static/
│   └── style.css       # the design system (cards, navy + amber, serif numbers)
└── tests/              # pytest tests (empty for now)
```

— TechSpire · @techspire-sa
