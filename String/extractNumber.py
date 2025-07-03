import re
s = "ab12cd34"
print([int(num) for num in re.findall(r'\d+', s)])  # Output: [12, 34]
