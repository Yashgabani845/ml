#--------------------Dictionary------------------
#same as map or json store in python - dictionary 
#key value pair 
a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

print("items in dictioanry are \n", a.items())
print("all keys are \n",a.keys())
print("upating dictionary adding sex \n",a.update({"Sex":"male"}) )
print(a.get("Sex"))
print("all keys are \n",a.keys())


#--------------------------------Set-----------------------
#no duplicate allowed
s = set() # no repetition allowed!
s.add(1)
s.add(2) # or set ={1,2}

# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

#--------------------- OPERATIONS ON SETS---------------
s1 = {1,8,2,3}

print(len(s1))
s1.remove(8)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
s1=s1.union({8,11})
print(s1)
s1=s1.intersection({8,11})
print(s1)
