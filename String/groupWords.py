words = ["eat", "tea", "ate", "bat", "tab"]
from collections import defaultdict
groups = defaultdict(list)
for word in words:
        groups[''.join(sorted(word))].append(word)
print(list(groups.values()))