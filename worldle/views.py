import csv
import random

from worldle import worldle_bp

from flask import render_template, request




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



    with open("static/worldle/countries.csv") as f:
        reader = csv.DictReader(f)
        entries = list(reader)

        if region != "Worldwide":
            entries = [entry for entry in entries if entry["region"].lower() == region.lower()]

        random_row = random.choice(entries)

    return render_template("worldle/capital.html", country_data=random_row)