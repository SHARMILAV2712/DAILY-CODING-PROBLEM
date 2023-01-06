'''DAY 15
Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string.
You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

Examples

alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"  '''

#SOLUTION
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def alphabet_index(alphabet, string): 
	a = 0
	for i in string.lower():
		if (alphabet.index(i)+1) > a:
			a = alphabet.index(i) + 1
	print(str(a)+alphabet[a-1])
string = input()
alphabet_index(alphabet,string)
