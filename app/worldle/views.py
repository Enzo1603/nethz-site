import csv
import random
from pathlib import Path
from copy import deepcopy

from . import worldle
from .. import cache


from flask import abort, render_template, redirect, url_for

FILE_PATH = Path(__file__).resolve().parent
COUNTRIES_CSV_FILE_PATH = (
    FILE_PATH.parent.parent / "static" / "worldle" / "countries.csv"
)

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

with open(COUNTRIES_CSV_FILE_PATH, "r", encoding="utf-8") as f:
    READER = csv.DictReader(f)
    CSV_ENTRIES = list(READER)


def get_csv_entries():
    """Randomize the csv dataset before copying it for the individual views"""
    return random.sample(CSV_ENTRIES, len(CSV_ENTRIES))


####### VIEWS #######


@worldle.route("/")
@cache.cached()
def home():
    return render_template("worldle/home.html")


@worldle.route("/capitals/")
def default_capitals():
    return redirect(url_for("worldle.capitals", region=DEFAULT_REGION))


@worldle.route("/capitals/<string:region>/")
def capitals(region):
    if region not in VALID_REGIONS:
        abort(404)

    entries = deepcopy(get_csv_entries())

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


@worldle.route("/languages/")
def default_languages():
    return redirect(url_for("worldle.languages", region=DEFAULT_REGION))


@worldle.route("/languages/<string:region>")
def languages(region):
    if region not in VALID_REGIONS:
        abort(404)

    entries = deepcopy(get_csv_entries())

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
