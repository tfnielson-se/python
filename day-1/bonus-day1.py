import pdb
# text = 'string'
# print(type(text))
#
# user_input = input("input: ")
# print(user_input)

list_str = []
length = len(list_str)
while len(list_str) < 4:
    ask = input("enter a name: ")
    list_str.append(ask)
    # pdb.set_trace()
else:
    print(list_str)

