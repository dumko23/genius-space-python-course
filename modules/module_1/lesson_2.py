from operator import index

custom_str = 'Some string'
num = 123
num_float = 123.456
custom_bool = True
none = None
custom_list = [1, 2, 3]
custom_tuple = (1, 2, 3)
custom_dict = {'key': 'value'}
custom_set = {1, 2, 3}

print(custom_str == 'Some string')
print(num == 124)
print(num_float == 123.456)
print(num_float < num)
print(custom_bool == False)
print(none is None)
print(4 in custom_list)
print(2 in custom_tuple)
print('key' in custom_dict)
print(1 in custom_set)

num_str = 125
str(num_str)
message = 'Hi, my name is Python!'
message.replace('y', '0').replace('i', '1')
split_test = 'This is a split test'
split_test.split()
string_join = ''.join(split_test)
print(len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend.index(6))
print(len(list_append))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.items())

