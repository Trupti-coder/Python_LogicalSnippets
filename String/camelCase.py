import re
s = "camelCaseExample"
print(re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower())  # Output: camel_case_example
