headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Classic Doctor Who episodes to be released in colour"
]

for index, headline in enumerate(headlines):
  print(f"Headline #{index}: {headline}")

total_words = 0
for headline in headlines:
    # Split each headline into words and count them
    words = headline.split()
    total_words += len(words)
    # total_words = total_words + len(words)

# Calculate and display the average (mean)
average_words = total_words / len(headlines)
print(round(average_words, 2))

# Banker's Algorithm
# Rounds to the nearest even number at 0.5 boundary
print(round(1.5))
print(round(2.6))

print(f"Average headline length: {average_words:.2f}")

print(f"{1:>3}")
print(f"{10:>3}")
print(f"{110:>3}")