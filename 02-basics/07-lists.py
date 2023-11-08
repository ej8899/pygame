# lists and tuples

my_list = [1,2,3,4.5,'word']
print(f'LIST length: {len(my_list)}')
print(my_list)

my_list.reverse()
print (my_list)

my_list.append(10)
print(my_list)


#
# TUPLES are a constant and can't be modified
#
my_tuple = (1,2,3,45, 'word', [7,8,9])
print (my_tuple)
#my_tuple.append(10) # fails - no method on tuples

#lists start at 0
print (my_tuple[4])
print (my_tuple[5])
print (my_tuple[5][1])
print (my_tuple[-1])
print (my_tuple[-2])