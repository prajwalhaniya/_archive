import json

simple_data = {
    "name": "PJ",
    "subject": "Python",
    "address": {
        "home": ("Bengaluru", "India"),
    },
}

with open("simpled_data.json", mode="w", encoding="utf-8") as write_file:
    json.dump(simple_data, write_file)