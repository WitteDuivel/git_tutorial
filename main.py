from sum import add_nums
print("Hello, World!")
name = input("What is your name?\n")
print(f"Hello {name}")

the_nums = []

while (num := input(">>> ")) != "q":
    the_nums.append(num)

print(add_nums(the_nums))
