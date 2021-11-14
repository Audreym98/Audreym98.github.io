import json

f_name_in = "top_artist_collabs.json"

with open(f_name_in) as json_file:
    data = json.load(json_file)

# keys are nodes and links
nodes = data['nodes']
links = data['links']
genre_links = []
for link_data in links:
    source = link_data['source']
    target = link_data['target']
    entry_dict = {}
    entry_dict['source_genre'] = nodes[source]['group']
    entry_dict['target_genre'] = nodes[target]['group']
    genre_links.append(entry_dict)

# print to json file
f_name_out = "genre_collabs.json"
with open(f_name_out, "w") as f_out:
    json.dump(genre_links, f_out, indent = "")

