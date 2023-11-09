x = 0
print ("start of while:")
while x < 10:
    x+=1
    if x == 5:
        continue
    
    print (x)
    


my_list = []
counter = 0

while counter <= 100:
    if counter % 2 == 0:
      my_list.append(counter)
    counter += 1

print (my_list)

print ("\n\nFOR LOOP:\n")
for x in [1,2,3]:
    print(x)