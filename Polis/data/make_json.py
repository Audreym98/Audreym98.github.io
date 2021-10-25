import json
import csv

def parse_float(label,labels,row):
    try:
        v= float(row[labels[label]] if row[labels[label]] else "-1")
    except:
        v = row[labels[label]]
    return v

csv_file = csv.reader(open("polis_filtered.csv"))

data =  {"type": "FeatureCollection",
   "features": []}

for row in csv_file:
   if csv_file.line_num == 1:

       labels = {}
       for i,l in zip(range(len(row)),row):
           labels[l]=i

   else:
       if parse_float("Longitude",labels,row) != -1:
           entry = {"type": "Feature",
                    "geometry": {
                       "type": "Point",
                       "coordinates":
                       [parse_float("Longitude",labels,row),parse_float("Latitude",labels,row)]
                           },
                    "properties":{
                        }
                    }
           for k in labels.keys():
               if k != "Latitude" and k != "Longitude":
                   value = parse_float(k,labels,row)
                   entry["properties"][k] = value
                   if k == "staseis":
                       if value == 0:
                           entry["properties"]["staseis absent"] = value
                           entry["properties"]["staseis present"] = -1
                       else:
                           entry["properties"]["staseis absent"] = -1
                           entry["properties"]["staseis present"] = value
           data["features"].append(entry)

print(json.dumps(data, sort_keys=True, indent=2))