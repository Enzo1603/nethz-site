import csv
import random
from pathlib import Path

from worldle import worldle_bp

from flask import abort, render_template

FILE_PATH = Path(__file__).resolve().parent


@worldle_bp.route("/")
def home():
    return render_template("worldle/home.html")


@worldle_bp.route("/capital/<string:region>")
def capital(region="worldwide"):
    VALID_REGIONS = {
        "africa", "americas", "antarctic", "asia", "europe", "oceania", "worldwide"
    }

    if region not in VALID_REGIONS:
        abort(404)

    countries_csv_file_path = FILE_PATH.parent / "static" / "worldle" / "countries.csv"
    with open(countries_csv_file_path) as f:
        reader = csv.DictReader(f)
        entries = list(reader)

        if region != "worldwide":
            entries = [
                entry for entry in entries if entry["region"].lower() == region.lower()
            ]

        # Filter entries with no capitals
        entries = [entry for entry in entries if entry["capital"].strip()]

        random_row = random.choice(entries)

    return render_template(
        "worldle/capital.html", region=region, country_data=random_row
    )
