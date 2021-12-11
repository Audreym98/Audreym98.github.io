import json
from collections import Counter

f_name_in = "alu_subfam_pairs_conf.txt"

network_data = {}
box_plot_data = []
subfam_to_index = {}
nodes = []
links = []
heatmap_data = {}
sub_pairs_to_conf = {}
subfam_links = Counter()

# set up source Alu type to target Alu type
alu_type_source_to_target = {
"AluY": {"AluY": 0, "AluJ": 0, "AluS": 0},
"AluJ": {"AluY": 0, "AluJ": 0, "AluS": 0},
"AluS": {"AluY": 0, "AluJ": 0, "AluS": 0}
}

# subfam pairs merged in full polyA run
# read in file, create a set
merged_subfams = set()
f_name_merged = "all_merged_subfams_dfam.txt"
with open(f_name_merged, "r") as f_in:
    for line in f_in:
        merged = line.split()[-1].split("_")
        for sub_A in merged:
            for sub_B in merged:
                merged_subfams.add((sub_A, sub_B))

with open(f_name_in, "r") as f_in:
    lines = f_in.readlines()

# build pairs to conf
for line in lines:
    line_info = line.split()
    subfam_A = line_info[0]
    subfam_B = line_info[1]
    conf = line_info[2][:5]
    sub_pairs_to_conf[(subfam_A, subfam_B)] = float(conf)
    # total pairs for this subfam
    subfam_links[subfam_A] += 1

# create network data
for pair, conf in sub_pairs_to_conf.items():
   subfam_A = pair[0]
   subfam_B = pair[1]
   source_group = subfam_A[:4]
   target_group = subfam_B[:4]
   box_plot_data.append({"source_type": source_group, "conf": conf})
   # at subfam A group, counter
   alu_type_source_to_target[source_group][target_group] += 1
   if subfam_A not in subfam_to_index.keys():
       subfam_to_index[subfam_A] = len(nodes)
       nodes.append({"name": subfam_A, "group": source_group, "index": subfam_to_index[subfam_A], "links": subfam_links[subfam_A]})
   if subfam_B not in subfam_to_index.keys():
       subfam_to_index[subfam_B] = len(nodes)
       nodes.append({"name": subfam_B, "group": target_group, "index": subfam_to_index[subfam_B], "links": subfam_links[subfam_B]})
   # add link
   # if pair in set
   merged = 0
   if (subfam_A, subfam_B) in merged_subfams:
       merged = 1
   links.append({"source": subfam_to_index[subfam_A], "target": subfam_to_index[subfam_B], "value": conf, "merged": merged})

# print target to source type values for table
for source_type in alu_type_source_to_target.keys():
    print(source_type)
    source_type_dict = alu_type_source_to_target[source_type]
    summ = sum(source_type_dict.values())
    for target_type, count in source_type_dict.items():
        print(target_type, count, summ)

network_data['nodes'] = nodes
network_data['links'] = links

# print to json file
f_name_out_network = "alu_subfam_network.json"
f_name_out_box_plot = "alu_type_conf.json"

with open(f_name_out_network, "w") as f_out:
    json.dump(network_data, f_out, indent = "")

with open(f_name_out_box_plot, "w") as f_out:
    json.dump(box_plot_data, f_out, indent = "")


