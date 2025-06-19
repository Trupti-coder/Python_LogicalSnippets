def generate_series():
    series = []
     for i in range(1, 11):
        series.append(i)       # Add the number
        series.append(i * 2)   # Add the number multiplied by 2
    return series
# Example usage
result = generate_series()
print(result)  # Output: [1, 2, 2, 4, 3, 6, 4, 8, ..., 10, 20]