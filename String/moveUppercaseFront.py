s = "aBcDeFg"
upper = ''.join([c for c in s if c.isupper()])
lower = ''.join([c for c in s if c.islower()])
print(upper + lower)  # Output: BDFgace
