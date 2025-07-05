emails = ["alice@gmail.com", "bob@yahoo.com", "carol@outlook.com"]
domains = [email.split('@')[1] for email in emails]
print(domains)  # Output: ['gmail.com', 'yahoo.com', 'outlook.com']
