import os
import shutil

TOPICS = {
    "two-sum": "Arrays",
    "array": "Arrays",
    "maximum-subarray": "Arrays",
    "binary-search": "BinarySearch",
    "search": "BinarySearch",
    "linked-list": "LinkedList",
    "reverse-linked": "LinkedList",
    "tree": "Trees",
    "binary-tree": "Trees",
    "graph": "Graphs",
    "dfs": "Graphs",
    "bfs": "Graphs",
    "dynamic-programming": "DP",
    "dp": "DP",
    "house-robber": "DP",
    "stack": "Stack",
    "queue": "Queue",
    "heap": "Heap",
    "priority-queue": "Heap",
    "recursion": "Recursion",
    "backtracking": "Backtracking",
}

IGNORE = {".git", ".github", "scripts", "Other"}
IGNORE.update(TOPICS.values())

def detect_topic(problem_name):
    name = problem_name.lower()
    for keyword, folder in TOPICS.items():
        if keyword in name:
            return folder
    return "Other"

def organize():
    current = os.getcwd()
    for item in os.listdir(current):
        if item.startswith("."):
            continue
        if not os.path.isdir(item):
            continue
        if item in IGNORE:
            continue

        topic = detect_topic(item)
        destination = os.path.join(topic, item)

        if not os.path.exists(topic):
            os.mkdir(topic)

        if item != topic:
            shutil.move(item, destination)
            print(f"Moved {item} -> {topic}")

if __name__ == "__main__":
    organize()
