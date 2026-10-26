# Tilawah Tracker — Starter

A private Quran reading-progress tracker. This starter is the **designed app
shell**: every page already matches our target design, with placeholder data.
The _logic_ — real authentication, a database, and live calculations — gets
built onto this shell over the coming episodes. For now the forms (update last
stop, login, register) are non-functional stubs.

## Pages (routed from the top menu)

- **Today (`/`)** — your progress card (page, juz, % through, pace), your _last stop_, and the _record today's reading_ form
- **Progress (`/progress`)** — this cycle's progress, pace, and a goal check (are you meeting one khatma a month?)
- **Khatmas (`/khatmas`)** — total khatmas completed, member-since / cycle dates, and a table of completed khatmas
- **Login / Register** — placeholder forms, not wired up yet

All data is hardcoded for now.

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

## Project structure

```
tilawah-tracker/
├── app.py              # routes + placeholder data
├── pyproject.toml      # dependencies (managed by uv)
├── templates/
│   ├── base.html       # top nav + page layout
│   ├── index.html      # Today: progress card + last stop + record form
│   ├── progress.html   # This cycle: pace + goal check
│   ├── khatmas.html    # dashboard: totals + completed-khatma table
│   ├── login.html      # placeholder login
│   └── register.html   # placeholder register
└── static/
    └── style.css       # the design system (cards, navy + amber, serif numbers)
```

— TechSpire · @techspire-sa
