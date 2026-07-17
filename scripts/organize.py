import re
import shutil
from pathlib import Path


TOPIC_FOLDERS = {
    "Arrays",
    "LinkedList",
    "Trees",
    "Graphs",
    "DynamicProgramming",
    "Stack",
    "Queue",
    "Heap",
    "Recursion",
    "Backtracking",
    "BinarySearch",
    "Sorting",
    "Greedy",
    "Trie",
    "BitManipulation",
    "SlidingWindow",
    "TwoPointers",
    "Math",
    "Other",
}

SKIP_FOLDERS = {".git", ".github", "scripts", *TOPIC_FOLDERS}

TOPIC_KEYWORDS = (
    ("Arrays", ("two-sum", "array", "subarray", "matrix", "hashing", "hash-map", "hashmap", "prefix-sum")),
    ("LinkedList", ("linked-list", "linkedlist", "list-node")),
    ("Trees", ("tree", "bst", "binary-tree", "traversal", "inorder", "preorder", "postorder")),
    ("Graphs", ("graph", "dfs", "bfs", "island", "topological", "shortest-path", "dijkstra")),
    ("DynamicProgramming", ("dynamic-programming", "dp", "memoization", "tabulation", "knapsack", "house-robber")),
    ("Stack", ("stack", "parentheses", "next-greater", "monotonic-stack")),
    ("Queue", ("queue", "deque")),
    ("Heap", ("heap", "priority-queue", "kth-largest", "kth-smallest")),
    ("Backtracking", ("backtracking", "permutation", "combination", "subsets", "n-queens")),
    ("BinarySearch", ("binary-search", "lower-bound", "upper-bound", "search-in-rotated")),
    ("Sorting", ("sort", "sorting", "merge-sort", "quick-sort")),
    ("Greedy", ("greedy", "interval", "jump-game", "activity-selection")),
    ("Trie", ("trie", "prefix-tree")),
    ("BitManipulation", ("bit-manipulation", "bitwise", "xor", "single-number")),
    ("SlidingWindow", ("sliding-window", "window", "substring")),
    ("TwoPointers", ("two-pointers", "two-pointer", "3sum", "three-sum", "container-with-most-water")),
    ("Recursion", ("recursion", "recursive")),
    ("Math", ("math", "gcd", "prime", "sieve", "palindrome-number", "pow")),
)


def normalize_name(folder_name):
    name = folder_name.lower()
    name = re.sub(r"^\d+[-_.\s]+", "", name)
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name


def detect_topic(folder_name):
    normalized = normalize_name(folder_name)

    for topic, keywords in TOPIC_KEYWORDS:
        if any(keyword in normalized for keyword in keywords):
            return topic

    return "Other"


def merge_or_move(source, destination):
    if not destination.exists():
        shutil.move(str(source), str(destination))
        return

    for child in source.iterdir():
        target = destination / child.name
        if target.exists():
            if target.is_dir() and child.is_dir():
                merge_or_move(child, target)
            elif target.is_file() or target.is_symlink():
                target.unlink()
                shutil.move(str(child), str(target))
            else:
                raise RuntimeError(f"Cannot overwrite {target}")
        else:
            shutil.move(str(child), str(target))

    source.rmdir()


def organize():
    root = Path.cwd()

    for item in sorted(root.iterdir()):
        if not item.is_dir():
            continue
        if item.name in SKIP_FOLDERS:
            continue
        if item.name.startswith("."):
            continue

        topic = detect_topic(item.name)
        topic_dir = root / topic
        destination = topic_dir / item.name

        topic_dir.mkdir(exist_ok=True)
        merge_or_move(item, destination)
        print(f"Moved {item.name} -> {topic}")


if __name__ == "__main__":
    organize()
