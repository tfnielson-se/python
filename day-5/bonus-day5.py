# Coding Exercise 1
filenames = ['document', 'report', 'presentation']
# Copy-paste the above list in a .py file and extend the code, so it prints out the output below:
# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt
for i, filename in enumerate(filenames):
    print(f"{i}-{filename.capitalize()}.txt")

# Coding Exercise 2
ips = ['100.122.133.105', '100.122.133.111']
# Copy-paste the ips list in a .py file and extend the program so it:
# 1. Prompts the user to input an index (e.g, 0 or 1).
ip_num = int(input('Enter 0 or 1: 1'))
# 2. Returns the IP address that has that index.
print(ips[ip_num])
# Here is how the program would behave when executed:

