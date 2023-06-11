# begin = int(input("Enter beginning"))
# end = int(input("Enter end"))
#
# for i in range(begin, end + 1):
# 	for j in range(1, 10 + 1):
# 		print(f"{i} * {j} = {i * j}")


# i = 0
# while i < 10:
# 	j = 0
# 	print("nested loop begins")
# 	while j < 0:
# 		print(f"i = {i} ; j = {j}")
# 		j += 1
# 	i += 1

# begin = int(input("Enter beginning"))
# end = int(input("Enter end"))
# i = begin
# while i < end:
# 	j = 1
#
# 	while j <= 10:
# 		print(f"{i} * {j} = {i * j}")
# 		j += 1

#
# for i in range(5):
# 	for j in range(5):
# 		if i == 2 and j == 2:
# 			print(" ", end="")
# 		else:
# 			print("  ", end="")
# 		print("* ", end = "")
# 	print ()

for i in range(5):
	for j in range(5):
		if 1 <= i <= 3 and 1 <= j <= 3:
			print("   ", end="")
		else:
			print("*  ", end="")
	print()

print()

for i in range(3):
	for j in range(7):
		if i == 1 and 1 <= j <= 5:
			print("   ", end="")
		else:
			print("*  ", end="")
	print()

print()

for i in range(7):
	for j in range(3):
		if j == 1 and 1 <= i <= 5:
			print("   ", end="")
		else:
			print("*  ", end="")
	print()

print()

stars = 6
spaces = 0
for i in range(stars):
	for j in range(spaces):
		print("  ", end="")
	for j in range(stars):
		print("  * ", end="")
	spaces += 1
	stars -= 1
	print()

print()

stars = 1
spaces = 5
for i in range(stars):
	for j in range(stars):
		print("  ", end="")
	for j in range(spaces):
		print("  * ", end="")
	stars -= 1
	spaces += 1
	print()

