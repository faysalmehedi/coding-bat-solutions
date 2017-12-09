#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
	result = ''
	for i in range(len(str)):
		result = result + str[:i+1]
	return result
'''def string_splosion(str):
    c = []
    for i in xrange(1, len(str)+1):
        c.append(str[:i])
    return "".join(c)'''

print(string_splosion('Code'),
string_splosion('abc'),
string_splosion('ab'))