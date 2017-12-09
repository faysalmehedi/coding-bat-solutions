#Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):
	char = ""
	for ch in str:
		char = char + (ch*2)
	return char

print(
double_char('The'),
double_char('AAbb'),
double_char('Hi-There'))