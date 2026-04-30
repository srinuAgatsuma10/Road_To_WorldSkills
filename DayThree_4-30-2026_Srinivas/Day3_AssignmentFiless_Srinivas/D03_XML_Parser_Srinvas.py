import xml.etree.ElementTree as ET
import json

with open("config.xml", "r") as f:
    f.read()

# Parse XML
tree = ET.parse("config.xml")
root = tree.getroot()

endpoints = []

for ep in root.findall("endpoint"):
    endpoints.append({
        "url": ep.get("url"),
        "method": ep.get("method"),
        "auth": ep.get("auth")
    })

print(endpoints)

# Write into JSON
with open("endpoints.json", "w") as f:
    json.dump(endpoints, f, indent=2)