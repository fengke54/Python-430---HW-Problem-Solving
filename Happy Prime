#Name: Feng, Ke
#DePaul ID: 1927931
#Date:01/18/2019
#HW1, Problem 2 
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Problem Solution Notes
#Step 1: Define a Prime Function
#Step 2: Define a Happy Function
#Step 3: Build a Counter and count 20 prime, then 20 happyn numbers
#Step 4: Build a Counter and count 20 numbers fits Function 1(Prime) and Function 2(Happy) / another 20 numbers fits Function 1 but not Function 2

#a) Write a function that returns True if an int is prime
def isprime(num):
    if (num<=1):  #Prime Number cannot be 1
        return False 
    for i in range(2, num):
        if num % i ==0:   #Any number divied by Prime have a remainder.  
            return False
    return True 

#b) Write a functon that returns True if an int is happy
def ishappy(num):
    sqr_sumfirst=[] 
    while True:
        str_digits=str(num) #Break the number into single digits by using str
        sums=0
        for j in str_digits:
            sums+=(int(j)*int(j)) #str digits should be changed back to int for further calculation 
        if sums==1:
            return True
        elif sums in sqr_sumfirst:  #loops endlessly in a cycle...if sums not eqaul to one
            return False
        sqr_sumfirst.append(sums)
        num=sums

#c) Write a function that returns True if an int is a happy prime (both happy and prime)
def happyprime(num):
    if isprime(num)==True and ishappy(num)==True:    #Fit both condition, return True. If not, False
        return True
    return False 
            
#d) Print 20 prime
print("A. Show the first 20 primes: ") 
counter=0
number=0
while counter<20:
    if isprime(number)==True:
        print(number)
        counter+=1   #Everytime it is a prime, counter plus 1
    number+=1        #Number goes to the next one   (Same with the rest prints) 

#e) Print 20 happy numbers
print("B. Show the first 20 happy numbers: ") 
counter=0
number=0
while counter<20:
    if ishappy(number)==True:
        print(number)
        counter+=1
    number+=1


#f) Print 20 happy primes
print("C. Show the first 20 happy primes: ") 
counter=0
number=0
while counter<20:
    if happyprime(number)==True:
        print(number)
        counter+=1
    number+=1


#g) Print 20 sad primes
print("D. Show the first 20 sad numbers: ") 
counter=0
number=0
while counter<20:
    if ishappy(number)==False and isprime(number)==True:
        print(number)
        counter+=1
    number+=1


