# WHILE LOOP

i = 0
while i < 5: # print "Harry" – 5 times!
    print("Harry")
    i = i + 1



l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8


# RANGE FUNCTION IN PYTHON
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# step_size is usually not used with range()
for i in range(0,7): # range(7) can also be used.
    print(i) # prints 0 to 6


l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!
# Output:
# 1
# 7
# 8
# done
# THE BREAK STATEMENT
# ‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now.

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if (i==3):
        break


for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)
# PASS STATEMENT
# pass is a null statement in python.
# It instructs to “do nothing”.
l = [1,7,8]
for item in l:
    pass # without pass, the program will throw an error