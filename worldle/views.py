import csv
import random
from pathlib import Path

from worldle import worldle_bp

from flask import render_template, request

FILE_PATH = Path(__file__).resolve().parent



@worldle_bp.route("/")
def home():
    return render_template("worldle/home.html")

@worldle_bp.route("/capital")
def capital():
    valid_regions = {
        "Africa", "Americas", "Antarctic", "Asia", "Europe", "Oceania", "Worldwide"
    }
    region = request.args.get("region")

    if region not in valid_regions:
        region = "Worldwide" # Default region


    countries_csv_file_path = FILE_PATH.parent / "static" / "worldle" / "countries.csv"
    with open(countries_csv_file_path) as f:
        reader = csv.DictReader(f)
        entries = list(reader)

        if region != "Worldwide":
            entries = [entry for entry in entries if entry["region"].lower() == region.lower()]

        # Filter entries with no capitals
        entries = [entry for entry in entries if entry["capital"].strip()]

        random_row = random.choice(entries)

    return render_template("worldle/capital.html", country_data=random_row)
