import re
s = "A man, a plan, a canal: Panama"
clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
print(clean == clean[::-1])  # Output: True
