numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort()

print("\nNumbers in ascending order with tags:")
for i, num in enumerate(numbers, start=1):
    print(f"Item{i}: {num}")
