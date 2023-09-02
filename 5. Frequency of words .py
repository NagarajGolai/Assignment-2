#Program to print 10 most frequently appearing words in a textfile

testfile = open("C:\\Users\\Student\\test.txt")
test_content = testfile.read()

word_list = test_content.split()
char_dict = {}

for char in word_list:
	if char in char_dict:
		char_dict[char] = char_dict[char] + 1
	else:
		char_dict[char] = 1
		
#printing
sorted_dict = sorted(char_dict.items(), key = lambda item : item[1])

first10pairs = list(sorted_dict)[:10]
print(first10pairs)