""" Hackathon - Level 3 """

def oddish_evenish_num(n):
	return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'

	
print(oddish_evenish_num(1190))
