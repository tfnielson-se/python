# Coding Exercise 1
# Please download the essay.txt file from the resources of this article. Then, create a program that reads that file and prints out its text. The first letter of each word in the output should be uppercase.

file = open('essay.txt', 'r')
file_content = file.read()
file.close()
print(file_content.title())

# Coding Exercise 2
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

char_num = len(file_content)
print(char_num)

# Please download the members.txt file from the resources of this article.
#
# Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
new_member = input('Enter a new member:  ') + "\n"

file = open('members.txt', 'r')
members = file.readlines()
file.close()

# Then, the member is added to members.txt. In this case, the text file content would be:
members.append(new_member)
file = open('members.txt', 'w')
file.writelines(members)
file.close()

# Coding Exercise 4
# Create a program that generates multiple text files by iterating over the filenames list. The text Hello should be written inside each generated text file.

files = ['file1.txt', 'file2.txt']

for txt_file in files:
    greeting = 'Hello'
    file = open(txt_file, 'w')
    file.writelines(greeting)
    file.close()

# Coding Exercise 5
# Please download the three text files a.txt, b.txt, and c.txt from the resources. Then, create a program that reads each text file and prints out the content of each in the command line. The expected output would be like the following:

files = ['a.txt', 'b.txt', 'c.txt']

for txt_file in files:
    file = open(txt_file, 'r')
    content = file.read()
    file.close()
    print(content)


