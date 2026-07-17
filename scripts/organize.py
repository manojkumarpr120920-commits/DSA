import os
import shutil
import json

# Load LeetCode problem-topic database
with open("scripts/leetcode_topics.json", "r") as file:
    TOPICS = json.load(file)


def detect_topic(problem_name):
    name = problem_name.lower()

    for keyword, folder in TOPICS.items():
        if keyword in name:
            return folder

    return "Other"


def organize():
    current = os.getcwd()

    for item in os.listdir(current):

        # Only check folders
        if not os.path.isdir(item):
            continue

        # Don't move scripts folder
        if item == "scripts":
            continue

        # Don't move topic folders again
        if item in TOPICS.values():
            continue

        topic = detect_topic(item)

        destination_folder = topic

        # Create topic folder if missing
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)

        destination = os.path.join(destination_folder, item)

        # Move problem folder
        if not os.path.exists(destination):
            shutil.move(item, destination)
            print(f"Moved {item} → {destination_folder}")

        else:
            print(f"Already exists: {destination}")


if __name__ == "__main__":
    organize()
