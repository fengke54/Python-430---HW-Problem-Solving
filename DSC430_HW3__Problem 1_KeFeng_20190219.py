#Name: Feng, Ke
#DePaul ID: 1927931
#Date:02/18/2019
#HW2, Problem 1
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

#Problem Solving Notes
#class--starts with __init__ (private: only works for this class)

import random

#Dice (6, 10, 20) 

#Create Six-Sided Dice class, including roll(), getFaceValue(), and __Repr___()methods
class SixSidedDie():

    def __init__(self): 
        self.facevalue=0 #private attribute, only goes in this class 

    def roll(self):
        self.facevalue=random.randint(1, 6)
        return self.facevalue #generate rolls

    def getFaceValue(self):
        return self.facevalue #result display

    def __repr__(self):
        return "SixSidedDice(%d)" % self.facevalue #Methods for showing instances

#Create Ten-Sided Dice class, including roll(), getFaceValue(), and __Repr___()methods---repeating steps in six
class TenSidedDie():

    def __init__(self):
        self.facevalue=0

    def roll(self):
        self.facevalue=random.randint(1, 10)
        return self.facevalue

    def getFaceValue(self):
        return self.facevalue

    def __repr__(self):
        return "TenSidedDiece(%d)" % self.facevalue

#Create Twenty-Sided Dice class, including roll(), getFaceValue(), and __Repr___()methods---repeating steps in six 
class TwentySidedDie():

    def __init__(self):
        self.facevalue=0

    def roll(self):
        self.facevalue=random.randint(1, 20)
        return self.facevalue

    def getFaceValue(self):
        return self.facevalue

    def __repr__(self):
        return "TwentySidedDiece(%d)" % self.facevalue

#Cup
class cup:
    def __init__(self, count_six, count_ten, count_twenty):
        self.count_six=count_six
        self.count_ten=count_ten
        self.count_twenty=count_twenty #start the class with __init__
        self.SidedDie=[] #this only goes within class, wihtout init, global variable goes beyond this class

    def roll(self):
        sum=0
        for i in range (self.count_six):    #pass the roll method from sixsideddie(), loop every element in six-roll, save the result in list SidedDie[]. calculate sum. 
            s=SixSidedDie()
            sum=sum+s.roll()
            self.SidedDie.append(s)
        for i in range(self.count_ten):
            t=TenSidedDie()
            sum=sum+t.roll()
            self.SidedDie.append(t)
        for i in range(self.count_twenty):
            w=TwentySidedDie()
            sum=sum+w.roll()
            self.SidedDie.append(w) #calculate sum of each dice
        return sum

    def getSum(self):
        sum=0
        for i in self.SidedDie:
            sum=sum+i.getFaceValue() 
        return sum

    def __repr__(self):
        result="Cup("
        L=len(self.SidedDie)
        count=0
        for i in self.SidedDie:
            result+=i.__repr__()
            count=count+1
            if (count!=L):
                result+=" "
        result+=")"
        return result #display sum value 
            

