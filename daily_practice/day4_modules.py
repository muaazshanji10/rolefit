import json

def count_event_types(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    event_count = {}

    for d in data:
        event_type = d["type"]["name"]
        if event_type in event_count:
            event_count[event_type] += 1
        else:
            event_count[event_type] = 1

    return event_count

if __name__ == "__main__":
    path = "/Users/muaazshanji/projects/statsbomb-data/data/events/15946.json"
    results = count_event_types(path)
    print(results)