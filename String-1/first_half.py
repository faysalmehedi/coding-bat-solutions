#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
	return str[:len(str)/2]


print(first_half('WooHoo'),
first_half('HelloThere'),
first_half('abcdef'))