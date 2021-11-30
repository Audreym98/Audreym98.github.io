import json

f_name_in = "happiness_ratings.csv"
data = []

with open(f_name_in, "r") as f_in:
    lines = f_in.readlines()
print(len(lines[1:]))
for line in lines[1:]:
    line = line.split(",")
    entry = {
    "Country": line[0],
    "Region": line[1],
    "Rank": line[2],
    "Score": line[3],
    "Economy": line[5],
    "Family": line[6],
    "Health": line[7],
    "Freedom": line[8],
    "Trust": line[9]
    }
    data.append(entry)

# print to json file
f_name_out = "happiness_ratings.json"
with open(f_name_out, "w") as f_out:
    json.dump(data, f_out, indent = "")