import json
import csv

def parse_float(label,labels,row):
    try:
        v= float(row[labels[label]] if row[labels[label]] else "-1")
    except:
        v = row[labels[label]]
    return v

csv_file = csv.reader(open("polis_filtered.csv"))

data =  []

for row in csv_file:
   if csv_file.line_num == 1:

       labels = {}
       for i,l in zip(range(len(row)),row):
           labels[l]=i

   else:
       if parse_float("Longitude",labels,row) != -1:
           entry = {}
           for k in labels.keys():
               if k in ["Elevation m", "Hellenicity", "Democracy",
                "Walls", "Victors", "area 1", "Proxenoi", "Koinon", "staseis"]:
                    val = parse_float(k,labels,row)
                    if k == "area 1":
                        k = "Area"
                    entry[k] = val
           data.append(entry)

print(json.dumps(data, sort_keys=True, indent=2))