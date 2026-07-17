import os
import shutil

# Main folders
TOPICS = {
    "array": "Arrays",
    "two-sum": "Arrays",
    "sort": "Sorting",
    "linked-list": "LinkedList",
    "tree": "Trees",
    "binary-tree": "Trees",
    "graph": "Graphs",
    "dynamic-programming": "DP",
    "dp": "DP",
    "stack": "Stack",
    "queue": "Queue",
}


def detect_topic(problem_name):
    name = problem_name.lower()

    for keyword, folder in TOPICS.items():
        if keyword in name:
            return folder

    return "Other"


def organize():
    current = os.getcwd()

    for item in os.listdir(current):

        # ignore folders
        if not os.path.isdir(item):
            continue

        # ignore scripts folder
        if item == "scripts":
            continue

        topic = detect_topic(item)

        destination = os.path.join(topic, item)

        if not os.path.exists(topic):
            os.mkdir(topic)

        if item != topic:
            shutil.move(item, destination)

            print(f"Moved {item} → {topic}")


if __name__ == "__main__":
    organize()
