"""Tilawah Tracker — walking skeleton (designed shell).

The pages already match the target design; the logic (auth, database, real
calculations) gets implemented over the coming episodes. For now all data is
hardcoded, and the forms (update last stop, login, register) are
non-functional stubs.
"""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# --- Placeholder data (hardcoded for now — no database yet) ---

USER = {"name": "Samir", "member_since": "Jul 2026"}

# Where the reader currently is, this cycle.
PROGRESS = {
    "cycle": 1,
    "current_page": 142,
    "total_pages": 604,    # pages in the Mushaf
    "current_juz": 8,
    "ayah": 5,
    "cycle_started": "Sep 18, 2026",
}

# Pace / activity figures.
PACE = {
    "this_month_pages": 96,
    "pages_per_day": 8,
    "cycles_done": 2,
}

# The reader's goal, used for the KPI check.
TARGET = {
    "days_per_khatma": 30,   # "monthly khatma"
    "pages_per_juz": 20,
}

# Completed khatmas so far (newest first).
KHATMAS = [
    {"n": 2, "started": "Aug 10, 2026", "finished": "Sep 16, 2026", "days": 37},
    {"n": 1, "started": "Jul 5, 2026",  "finished": "Aug 8, 2026",  "days": 34},
]


def _percent():
    return round(PROGRESS["current_page"] / PROGRESS["total_pages"] * 100)


@app.route("/")
def home():
    """Today: the progress card, last stop, and the update form."""
    return render_template(
        "index.html",
        user=USER, progress=PROGRESS, pace=PACE, percent=_percent(),
    )


@app.route("/progress")
def progress():
    """This cycle: progress, pace, and the goal check."""
    target_per_day = round(PROGRESS["total_pages"] / TARGET["days_per_khatma"])
    on_track = PACE["pages_per_day"] >= target_per_day
    pages_left = PROGRESS["total_pages"] - PROGRESS["current_page"]
    days_to_finish = round(pages_left / PACE["pages_per_day"])
    return render_template(
        "progress.html",
        user=USER, progress=PROGRESS, pace=PACE, percent=_percent(),
        target_per_day=target_per_day, on_track=on_track,
        pages_left=pages_left, days_to_finish=days_to_finish,
    )


@app.route("/khatmas")
def khatmas():
    """Dashboard: total khatmas and the khatma history."""
    return render_template(
        "khatmas.html",
        user=USER, progress=PROGRESS, pace=PACE, khatmas=KHATMAS,
    )


@app.route("/update", methods=["POST"])
def update():
    """Non-functional stub — the new last stop isn't saved yet."""
    return redirect(url_for("home"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Non-functional stub — no one is actually authenticated yet."""
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Non-functional stub — no account is actually created yet."""
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("register.html")


if __name__ == "__main__":
    # Port 5001 (macOS uses 5000 for AirPlay).
    app.run(debug=True, port=5001)
