#Name: Feng, Ke
#DePaul ID: 1927931
#Date:02/02/2019
#HW2, Problem 1
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Problem Solving Notes
#Step 1:Create a list of alphabet
#Step 2:Gauge out the last letter in "namesBoys" and "namesGirls", and count those letters
#Step 3:Create a dictionary storing keys and values. keys are letters, values are counts
#Step 4:Check how many keys are in alphabet, storing those into a place
#Step 5:Check how many keys are not in alphabet, storing those into a place. Not in alphabet returns 0
#Step 6:Get key and value using step 4 and 5

#a)Create a list of alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#b)Gauge out the last character in namesGirls, using [-1] indexing
girlcount = []
f = open("namesGirls.txt")
girls = f.readlines()
for girl in girls:
    char = girl.replace("\n","")[-1]
    girlcount.append(char)

#c)Gaught out the last character in namesBoys, using [-1] indexing 
boycount = []
f = open("namesBoys.txt")
boys = f.readlines()
for boy in boys:
    char = boy.replace("\n","")[-1]
    boycount.append(char)

#d)-------------------------Work on girls' results------------------------------------
#d-1)Count girls' results and throw them into an empty dictionary
girlresult = {}
for girl in set(girlcount):
    girlresult[girl] = girlcount.count(girl)

#d-2)Seperate the dictionary into keys and values, keys are letters, values are counts
girlresult = dict(sorted(girlresult.items(),key=lambda k:k[0]))
girlkeys = []
girlvalues = []
for key,value in girlresult.items():
    girlkeys.append(key)
    girlvalues.append(value)

#d-3)See how many girls' letters' keys are in alphabet list 
nums = []
for key,value in girlresult.items():
    inde = alphabet.index(key)
    nums.append(inde)

#d-4)Generating a new empty list storing keys that are not in alphabet list   
need = []
length =  len(nums)
for i in range(length):
    if i+1<length:
        cal = nums[i+1] - nums[i] 
    if cal != 1:
        c = cal -1
        if c!=1:
            for j in range(1,c+1):
                need.append(nums[i]+j)
        else:
            need.append(nums[i]+1)

#d-5)Not in alphabet list insert 0           
for n in need:
    girlkeys.insert(n,alphabet[n])
    girlvalues.insert(n,0)

#e)-----------------------Working on Boys results (Same process)--------------------
#e-1)Create a dictionary, storing key:value format, counting how many times for last letter
boyresult = {}
for boy in set(boycount):
    boyresult[boy] = boycount.count(boy)

#e-2)seperate key and value in dictionary
boyresult = dict(sorted(boyresult.items(),key=lambda k:k[0]))
boykeys = []
boyvalues = []
for key,value in boyresult.items():
    boykeys.append(key)
    boyvalues.append(value)

#e-3)See how many keys are in alphabet 
nums = []
for key,value in boyresult.items():
    inde = alphabet.index(key)
    nums.append(inde)

#e-4)See how many keys are not in alphabet 
need = []
length =  len(nums)
for i in range(length):
    if i+1<length:
        cal = nums[i+1] - nums[i] 
    if cal != 1:
        c = cal -1
        if c!=1:
            for j in range(1,c+1):
                need.append(nums[i]+j)
        else:
            need.append(nums[i]+1)
#e-5)Those not in alphabet given zero         
for n in need:
    boykeys.insert(n,alphabet[n])
    boyvalues.insert(n,0)

#f)Print Result 
print("Letter\tBoys\tGirls")
for i in range(len(girlkeys)):
    print(girlkeys[i]+"\t"+str(boyvalues[i])+"\t"+str(girlvalues[i]))
    

