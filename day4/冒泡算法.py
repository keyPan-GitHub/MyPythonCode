"""

li = [33,2,10,1]

print(li)

for i in range(len(li) - 1):
	# i = 0			
	# current 	li[0]	0	1
	# new_value li[0]	1	2
	# current = li[i]
	# new_value = li[i + 1]
	# print(i,current,new_value)
	if li[i] > li[i + 1]:
		temp = li[i]
		li[i] = li[i+1]
		li[ i + 1] = temp


print(li)


for i in range(len(li) - 2):
	# i = 0			
	# current 	li[0]	0	1
	# new_value li[0]	1	2
	# current = li[i]
	# new_value = li[i + 1]
	# print(i,current,new_value)
	if li[i] > li[i + 1]:
		temp = li[i]
		li[i] = li[i+1]
		li[ i + 1] = temp


print(li)



for i in range(len(li) - 3):
	# i = 0			
	# current 	li[0]	0	1
	# new_value li[0]	1	2
	# current = li[i]
	# new_value = li[i + 1]
	# print(i,current,new_value)
	if li[i] > li[i + 1]:
		temp = li[i]
		li[i] = li[i+1]
		li[ i + 1] = temp


print(li)

"""

# 冒泡排序
li = [33, 2, 10, 1155, 1, 56, 587, 789, 456, 98, 156, 454, 43, 9, 8, 7, 65]

for j in range(1, len(li)):

    for i in range(len(li) - j):
        # i = 0
        # current 	li[0]	0	1
        # new_value li[0]	1	2
        # current = li[i]
        # new_value = li[i + 1]
        # print(i,current,new_value)
        if li[i] > li[i + 1]:
            temp = li[i]
            li[i] = li[i + 1]
            li[i + 1] = temp

print(li)
