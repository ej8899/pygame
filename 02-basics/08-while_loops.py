# x = 0
# print ("start of while:")
# while x < 10:
#     x+=1
#     if x == 5:
#         continue
    
#     print (x)
    


# my_list = []
# counter = 0

# while counter <= 100:
#     if counter % 2 == 0:
#       my_list.append(counter)
#     counter += 1

# print (my_list)

# print ("\n\nFOR LOOP:\n")
# for x in [1,2,3]:
#     print(x)


# basic_dict = {1:'one', 2:'two', 3:'three'}
# for x in basic_dict:
#     print(x)
# for x in basic_dict.items():
#     print(x)



# print ("\n\nFOR LOOP RANGES:\n")
# for x in range(10,20,2):
#     print(x)




practice_list = [[10,40,20,50], [2,42,10], [101,12,4]]
for nested_list in practice_list:
    # print(nested_list)
    for value in nested_list:
        # print (value)
        if (value < 50 and value > 9):
          print (value)
        if (value > 100):
          print (f'ending loop - found: {value}')
          break;
                