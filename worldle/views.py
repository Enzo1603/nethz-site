import csv
import random
from pathlib import Path
from copy import deepcopy

from worldle import worldle_bp

from flask import abort, render_template, redirect, url_for

FILE_PATH = Path(__file__).resolve().parent
COUNTRIES_CSV_FILE_PATH = FILE_PATH.parent / "static" / "worldle" / "countries.csv"

DEFAULT_REGION = "worldwide"
VALID_REGIONS = {
    "africa",
    "americas",
    "antarctic",
    "asia",
    "europe",
    "oceania",
    "worldwide",
}

with open(COUNTRIES_CSV_FILE_PATH) as f:
    READER = csv.DictReader(f)
    CSV_ENTRIES = list(READER)


@worldle_bp.route("/")
def home():
    return render_template("worldle/home.html")


@worldle_bp.route("/capitals/")
def default_capitals():
    return redirect(url_for("worldle_bp.capitals", region=DEFAULT_REGION))


@worldle_bp.route("/capitals/<string:region>/")
def capitals(region):
    if region not in VALID_REGIONS:
        abort(404)

    entries = deepcopy(CSV_ENTRIES)

    if region != DEFAULT_REGION:
        entries = [
            entry for entry in entries if entry["region"].lower().strip() == region
        ]

    # Filter entries with no capitals
    entries = [entry for entry in entries if entry["capital"].strip()]

    random_row = random.choice(entries)

    return render_template(
        "worldle/capitals.html",
        region=region,
        country_data=random_row,
    )


@worldle_bp.route("/languages/")
def default_languages():
    return redirect(url_for("worldle_bp.languages", region=DEFAULT_REGION))


@worldle_bp.route("/languages/<string:region>")
def languages(region):
    if region not in VALID_REGIONS:
        abort(404)

    entries = deepcopy(CSV_ENTRIES)

    if region != DEFAULT_REGION:
        entries = [
            entry for entry in entries if entry["region"].lower().strip() == region
        ]

    # Filter entries with no languages
    entries = [entry for entry in entries if entry["languages"].strip()]

    random_row = random.choice(entries)

    return render_template(
        "worldle/languages.html",
        region=region,
        country_data=random_row,
    )
