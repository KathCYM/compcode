import json
import sys

def reformat_json(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    reformatted_data = []
    for idx, item in enumerate(data):
        reformatted_item = {
            "idx": idx,
            "platform": item.get("platform"),
            "question_title": item.get("question_title"),
            "difficulty": item.get("difficulty"),
            "pass@1": item.get("pass@1")
        }
        reformatted_data.append(reformatted_item)

    return reformatted_data

def append_metrics(reformatted_data, metrics_file):
    with open(metrics_file, 'r') as file:
        metrics_data = json.load(file)

    metrics_data = metrics_data[0].get("detail")
    pass_1 = metrics_data.get("pass@1")
    pass_5 = metrics_data.get("pass@5")
    pass_10 = metrics_data.get("pass@10")
    for idx, i in enumerate(pass_1):
        reformatted_data[idx]["pass_1"] = pass_1[i]
    for idx, i in enumerate(pass_5):
        reformatted_data[idx]["pass_5"] = pass_5[i]
    for idx, i in enumerate(pass_10):
        reformatted_data[idx]["pass_10"] = pass_10[i]
    return reformatted_data

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_json_file> <metrics_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    metrics_file = sys.argv[2]

    # Reformat original JSON
    formatted_data = reformat_json(input_file)

    # Append metrics data
    combined_data = formatted_data #append_metrics(formatted_data, metrics_file)

    # Output combined data
    for entry in combined_data:
        print(entry)
