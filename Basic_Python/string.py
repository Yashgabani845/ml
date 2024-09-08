name = "yash gabani"
print(len(name))
fname = name[0:4]
print(fname)
lname = name[-6:-1]
print(name[-6:])
print(lname)
print(name[1:10:2]) #will print from 1 to 10 with sip of 2 a then h then g then b then n 

#methods : visit handbook
# \n for new line 
# \t tab 
# \` signle quote
# \\ double quote



# -------------- Lists and Tuples --------------

l1 = [1,2,3,4,5]
l1.sort() #only works if we have same type of 
print(l1)
l2 = l1[1:3]
print(l2)


#other methods 
# l1 = [1,8,7,2,21,15]
# • l1.sort(): updates the list to [1,2,7,8,15,21]
# • l1.reverse(): updates the list to [15,21,2,7,8,1]
# • l1.append(8): adds 8 at the end of the list
# • l1.insert(3,8): This will add 8 at 3 index
# • l1.pop(2): Will delete element at index 2 and return its value.
# • l1.remove(21): Will remove 21 from the list. 

#------------------------Tuple----------------------
#to store contant list for using 

tup1 = (1,2,4,"yash",2)
print(tup1)

# can not change anything in tuple

print(tup1[3])
tup2= (1,)
print(tup2) # for 1 element , is needed

