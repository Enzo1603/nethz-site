import csv
import random

with open("static/worldle/countries.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # regions = set()
    # subregions = set()

    # for row in reader:
    #     region = row["region"]
    #     subregion = row["subregion"]

    #     regions.add(region)
    #     subregions.add(subregion)

    # print(sorted(regions))
    # print(sorted(subregions))

    csv_entries = list(reader)
    print(len(csv_entries))
    c1 = random.choice(csv_entries)
    csv_entries.remove(c1)
    print(len(csv_entries))
