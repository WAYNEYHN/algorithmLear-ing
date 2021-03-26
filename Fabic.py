<<<<<<< HEAD
#普通的斐波拉契递归解法 时间复杂度 O(2^n) 空间复杂度O(1)
def fabic_normal(num):
	if num == 0 or num ==1:
		return num
	else:
		return fabic_normal(num-1) + fabic_normal(num-2)


#自底向上的解法, 时间复杂度O(n)空间复杂度O(1)
def fabic_for(num):
	res = [0, 1]
	for i in range(num):
		temp = res[-1] +res[-2]
		res[0] = res[1]
		res[1] = temp
	return res[0]


#递归解法带备忘录 时间复杂度O(n)空间复杂度O(n)
def fabic_note(num, note):
	if num == 0 or num == 1:
		return num
	if note[num] != 0:
		return note[num]
	note[num] = fabic_note(num-1, note)+ fabic_note(num-2, note)
	print(note)
	return note[num]

note = [0 for i in range(21)]
=======
#普通的斐波拉契递归解法 时间复杂度 O(2^n) 空间复杂度O(1)
def fabic_normal(num):
	if num == 0 or num ==1:
		return num
	else:
		return fabic_normal(num-1) + fabic_normal(num-2)


#自底向上的解法, 时间复杂度O(n)空间复杂度O(1)
def fabic_for(num):
	res = [0, 1]
	for i in range(num):
		temp = res[-1] +res[-2]
		res[0] = res[1]
		res[1] = temp
	return res[0]


#递归解法带备忘录 时间复杂度O(n)空间复杂度O(n)
def fabic_note(num, note):
	if num == 0 or num == 1:
		return num
	if note[num] != 0:
		return note[num]
	note[num] = fabic_note(num-1, note)+ fabic_note(num-2, note)
	print(note)
	return note[num]

note = [0 for i in range(21)]
>>>>>>> d6bc1f944635e174e38aa8cc449fd794d1c11168
print(fabic_for(20))