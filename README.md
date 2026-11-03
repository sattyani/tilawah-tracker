# Tilawah Tracker

A small, private web app for tracking daily Quran reading through the 604-page
Madinah Mushaf. You record where you stopped; the app counts the pages, keeps
your history, and tracks each khatma.

Built in the open in the TechSpire series _Spec-Driven Development_: one
feature per episode, each from a written spec.

## Status

This is the **designed app shell**: every page matches the target design, but
the data is hardcoded and the forms (record a stop, login, register) don't work
yet. Features are added one specification at a time.

The full product definition, with rules, scope and success criteria, is in
[docs/project-overview.md](docs/project-overview.md).

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
- **Private by default.** Every account sees only its own data.

## Out of scope

- Quran text, translation, tafsir, or surah and ayah data
- Reading time, duration, or speed
- Personal notes
- Goals, targets, streaks, schedules, or reminders
- Editing or deleting entries
- Starting a new khatma before page 604
- Groups, sharing, or any social features
- Audio, tajweed, or memorization tracking
- Import or export, attachments, or runtime integrations
- AI features inside the app
- A native mobile app

Nothing here gets added without an approved change spec.

## Pages (current shell)

- **Today (`/`)** — progress card, your _last stop_, and the record form
- **Progress (`/progress`)** — this cycle's progress
- **Khatmas (`/khatmas`)** — completed khatmas and totals
- **Login / Register** — placeholder forms, not wired up yet

> The shell still shows a monthly goal check and pace target on the Progress
> page. Those are out of scope and will be removed when that page is built.

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
├── app.py                   # routes + placeholder data
├── pyproject.toml           # dependencies (managed by uv)
├── docs/
│   └── project-overview.md  # what we're building: rules, scope, success criteria
├── templates/
│   ├── base.html            # top nav + page layout
│   ├── index.html           # Today: progress card + last stop + record form
│   ├── progress.html        # This cycle's progress
│   ├── khatmas.html         # completed khatmas + totals
│   ├── login.html           # placeholder login
│   └── register.html        # placeholder register
└── static/
    └── style.css            # the design system (cards, navy + amber, serif numbers)
```

— TechSpire · @techspire-sa
