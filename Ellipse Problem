#Name: Feng, Ke
#DePaul ID: 1927931
#Date:02/02/2019
#HW2, Problem 2 
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Problem Solution Notes
#Step 1: Use random library to create point P(px, py)---falls inside/on/outside the ellipse
#Step 2: Create a rectangle that has the length of the major-axis and the width of the minor-axis
#Step 3: Use Pythagorean theorem to calculate the minor-axis （key parameters： PF1，central coordinate of F1／F2， distance of center point to P）
#Step 4：Giving conditions: if PF1+PF2<=2a, inside the ellipse, return True, if not, outside, return False
#Step 5: Calculate the percentage of points on the ellipse (count(True)/n)
#Step 6: area of ellipse=rectangle * percentage

#a)Import libraries 
import random

#b)Create an user interface
print("Welcome!\nThis program will use random numbers to compute the area of an ellipse.")
f1x,f1y=input("Enter the position of F1(format:x y):").split()
f1x=float(f1x)
f1y=float(f1y)
f2x,f2y=input("Enter the position of F2(format:x y):").split()
f2x=float(f2x)
f2y=float(f2y)
a=eval(input("Enter the length of the major axis (format: 1):"))
num=eval(input("Enter the number of random points(format:n):"))

#c)Use Random Library to create P(px, py) and calculate the distance from midpoint to define range of px, py
result = []
recs = []
cx=(f1x+f2x)//2
cy=(f1y+f2y)//2
    
for i in range(1,num+1):
    px = random.uniform(cx-a//2,cx+a//2)
    py = random.uniform(-cy-a//2,cy+a//2)

#d)Calculate the area of the rectangle 
#d-1)Calculate the center point C(m, n) of F1, F2, and calculate the distance between P and C
    m=((f1x+f2x)//2)
    n=((f1y+f2y)//2)
    dist1=((m-px)**2+(n-py)**2)**0.5

#d-2)Calculate the distance between P and F1 or F2 (when P to F1 is equal to P to F2)
    dist2=((px-f1x)**2+(py-f1y)**2)**0.5

#d-3)The length of the closest rectange
    reclength=(dist1**2-dist2**2)**0.5

#d-4)area of the rectangle
    rec=(2*a)*(2*reclength)

#e)Write conditions 
    pf1=((f1x-px)**2+(f1y-py)**2)**0.5
    pf2=((f2x-px)**2+(f2y-py)**2)**0.5
    if (pf1 + pf2) <= 2 * a:
        result.append(True)
        recs.append(rec)
    else:
        result.append(False)

#f)Use percentage to calculate the area of the ellipse
percentage = result.count(True)/num
area=rec*percentage
print("Thinking...\nThe area of the ellipse is approximately: "+ str(area))

    
        
        
    
    

