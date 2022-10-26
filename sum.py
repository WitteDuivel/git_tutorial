def add_nums(nums):
	the_sum = 0
	for e in nums:
		the_sum += int(e)
	return the_sum
if __name__ == "__main__":
    the_nums = []
    while (num := input("=>")) != "q":
        the_nums.append(num)
    print(add_nums(the_nums))
