s = "HelloWorld123"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Upper:", upper, "Lower:", lower)  # Output: Upper: 2 Lower: 8