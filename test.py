import csv

with open("static/worldle/countries.csv") as f:
    reader = csv.DictReader(f)

    regions = set()
    subregions = set()

    for row in reader:
        region = row["region"]
        subregion = row["subregion"]

        regions.add(region)
        subregions.add(subregion)

    print(sorted(regions))
    print(sorted(subregions))
