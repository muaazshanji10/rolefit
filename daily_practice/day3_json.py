import json

# The full, exact path to one of my real StatsBomb event files
file_path = "/Users/muaazshanji/projects/statsbomb-data/data/events/15946.json"

with open(file_path, "r") as f:
    data = json.load(f)

print("Total events in this match:", len(data))
print("\nFirst event structure:")
print(data[0])

import json

file_path = "/Users/muaazshanji/projects/statsbomb-data/data/events/15946.json"

with open(file_path, "r") as f:
    data = json.load(f)

print("Total events in this match:", len(data))
print("\nFirst event type name:", data[0]['type']['name'])

# The syntax pattern:
#if "key_name" in my_dict:
    # Do something if the key exists

# 1. Start with an empty dictionary to store counts
type_counts = {}

# 2. Loop through every single event dictionary in the match
for d in data:
    event_type = d['type']['name']
    
    # 3. Increment the count or initialize it
    if event_type in type_counts:
        type_counts[event_type] += 1
    else:
        type_counts[event_type] = 1

print("Event breakdown for this match:")
print(type_counts)


