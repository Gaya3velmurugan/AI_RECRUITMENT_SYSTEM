import json
import os

FILE_PATH = "app/storage/candidates.json"


def add_candidate(candidate):

    if os.path.exists(FILE_PATH):

        with open(FILE_PATH, "r") as file:
            candidates = json.load(file)

    else:
        candidates = []

    candidates.append(candidate)

    with open(FILE_PATH, "w") as file:
        json.dump(candidates, file, indent=4)

    return candidate