#Name: Feng, Ke
#DePaul ID: 1927931
#Date:01/16/2019
#HW1, Problem 1 
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Problem Solving Notes:
#Step 1: Overlap=Length * Width 
#Step 2: Calculate Length and Width. The most important two coordinates are upper right and bottom left. 
#Step 3: Define a function calculating width and length using coordinates. If >0, return x*y. If not, return 0. 

#m, n are two lists. Each have [x, y, z]. Using coordinate value to calculate overlap length and overlap width.
def overlap(m, n):
    length=min(m[0]+m[2], n[0]+n[2])-max(m[0],n[0])
    width=min(m[1]+m[2], n[1]+n[2])-max(m[1],n[1])

#If both length and width are larger then zero, return the area. If not, return zero. (if condition) 
    if(length>0)and(width>0):    
        return length*width
    else:
        return 0

totalScore = 0

S1 = [1,5,3]
S2 = [5,6,2]
S3 = [2,1,2]
S4 = [9,6,2]
S5 = [7,2,3]
S6 = [3,2,5]
S7 = [5,3,1] 

#---------- ---------- ---------- ---------- ----------
print( "Test 1: " + str(S1) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S1,S6)
r2 = overlap(S6,S1)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 2: " + str(S2) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S2,S6)
r2 = overlap(S6,S2)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 3: " + str(S3) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S3,S6)
r2 = overlap(S6,S3)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 4: " + str(S4) + str(S6) )
print( "Correct Answer: 0" )
r1 = overlap(S4,S6)
r2 = overlap(S6,S4)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 0:
    s1 = s1 + 1
if r2 == 0:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 5: " + str(S5) + str(S6) )
print( "Correct Answer: 3" )
r1 = overlap(S5,S6)
r2 = overlap(S6,S5)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 3:
    s1 = s1 + 1
if r2 == 3:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 6: " + str(S6) + str(S6) )
print( "Correct Answer: 25" )
r1 = overlap(S6,S6)
r2 = overlap(S6,S6)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 25:
    s1 = s1 + 1
if r2 == 25:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 7: " + str(S7) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S7,S6)
r2 = overlap(S6,S7)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print ( "Total Score: " + str(totalScore) )
print ( "Percentage: " + str(100*totalScore/14) )

    



