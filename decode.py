import random
import matplotlib.pyplot as plt

frequency = {i: 0 for i in range(1, 51)}

for _ in range(1000):
    num = random.randint(1, 50)
    frequency[num] += 1

plt.figure(figsize=(12, 6))
plt.bar(frequency.keys(), frequency.values(), color="orange", edgecolor="black")
plt.title("Random Number Frequency (1-50)")
plt.xlabel("Number")
plt.ylabel("Count")
plt.grid(True)

# Save instead of show (for headless environments)
plt.savefig("random_number_plot.png")
print("✅ Plot saved as random_number_plot.png")
