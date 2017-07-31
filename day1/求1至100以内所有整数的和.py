i = 1
sums = 0
# while i <= 100:
# 	sums += i
# 	i += 1
# print(sums)

# while i <= 100:
# 	if i % 2 != 0:
# 		print(i)
# 	i += 1

while i < 100:
	if i % 2 != 0:
		sums += i
	else:
		sums -= i
	i+=1
print(sums)

