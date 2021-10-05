import sys
import json

f_name_in = sys.argv[1]
f_name_out = sys.argv[2]
f_in = open(f_name_in, "r")

ncols = f_in.readline().split()[1]
nrows = f_in.readline().split()[1]
data = {}
data["height"] = nrows
data["width"] = ncols

# skip next 4 lines
for i in range(4):
    f_in.readline()

values = []
line = f_in.readline()
while line:
    line = line.split()
    for value in line:
        values.append(float(value))
    line = f_in.readline()
print("max")
print(max(values))
print("min")
print(min(values))

data["values"] = values
f_in.close()

with open(f_name_out, "w") as f_out:
    json.dump(data, f_out, indent = "")
