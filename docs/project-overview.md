# Tilawah Tracker — Project Overview

## Purpose

A small, private web app for tracking daily Quran reading through the 604-page
Madinah Mushaf. It answers three questions: where do I continue, how much have I
read, and how has my reading developed over time?

It is also the teaching project for a spec-driven-development series, so the
product stays deliberately small. The sophistication comes from the specs and the
workflow, not from features.

## Terms

- **Stop** — the page number the user records after reading. Each stop is one entry.
- **Reading day** — a date with at least one recorded stop.
- **Khatma** — one full read of the Mushaf, page 1 to 604 (a reading cycle).

## How it works

1. The user registers and logs in.
2. The dashboard shows their last stop.
3. After reading, they record a **stop page** and, optionally, the **ayah**.
4. The app sets the date, counts the pages, and updates their progress.
5. At page 604, they choose **Finish khatma**, and a new khatma starts from page 1.

## Rules

- **The user enters only a stop page and an optional ayah.** The app sets the date.
- **Pages read = new stop − previous stop.** A new khatma starts from 0.
  Example: record 10, then 12 → 10 pages, then 2 pages.
- **Forward only.** A new stop must be higher than the last stop and no higher than 604.
- A stop **equal** to the last stop is ignored: nothing is recorded.
  A **lower** stop is rejected.
- **Several stops on one day** are added together into one reading day.
- **Finish khatma** appears only when the last stop is 604, and is chosen by the
  user. Until then, no new stops can be recorded.
- **Entries are permanent.** They can't be edited or deleted, and the position and
  date can't be changed by hand.
- The **ayah** is shown back to the user only. It isn't used in any calculation or
  checked against the page.
- **Private by default.** A user sees only their own data, enforced on the server,
  including for manually typed URLs.
- Juz and hizb are derived from the page number using a fixed 604-page table,
  generated once during development.

## Pages

- **Landing** — what the app is, with links to register and log in
- **Register / Login / Logout**
- **Dashboard** — last stop; position (page, juz, hizb); this khatma's progress;
  total pages; reading days; average pages per reading day; completed khatmas;
  recent reading days; **Finish khatma** at page 604
- **Record a stop** — shows the last stop; takes a stop page and an optional ayah
- **History** — reading days, newest first, with the pages read each day
- **Yearly summary** — for a chosen year: pages, reading days, average pages per
  reading day, khatmas completed

## Out of scope

- Quran text, translation, tafsir, or surah and ayah data
- Reading time, duration, or speed
- Personal notes
- Entering or changing the date
- Goals, targets, streaks, schedules, or reminders
- Editing or deleting entries, or changing the position by hand
- Starting a new khatma before page 604
- More than one Mushaf edition
- Groups, sharing, or any social features; any role besides a registered user
- Audio, tajweed, or memorization tracking
- Import or export, attachments, or runtime integrations
- AI features inside the app
- A native mobile app

Nothing here is added without an approved change spec.

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

The repo is the designed app shell from Episode 2: the pages match the target
design, but the data is hardcoded and the forms don't work. Where the shell
disagrees with this overview, the overview wins. In particular, the shell's
monthly goal check, target pages per day and on-track check will be removed.
