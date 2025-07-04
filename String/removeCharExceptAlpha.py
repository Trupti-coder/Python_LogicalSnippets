s = "Th1s h@s sp#cial char@cters!"
clean = ''.join(c for c in s if c.isalpha())
print(clean)  # Output: "Thshspcialcharcters"
