#Name: Feng, Ke
#DePaul ID: 1927931
#Date:02/18/2019
#HW2, Problem 2
#Honor Code Statement: I have not given or received any unauthorized assitance on this assignment."

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

def is_number(str):    #This function is defined for extensive check (three conditions) 
    try:
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False
        
###User Interactive
if __name__ == '__main__':
    money = 100 #(2)Provide 100 Balance 
    name = input("Welcome to the game! You are given 100 dollars to play the game. Please input your name: ") #(1)Greet the Users
    

    choice = "1"
    while (choice == "1"):
        choice = input("Do you want to play game?(1--play，0--Not play)：")
        if (choice == "0"):
            break #(3)Ask Users if they would like to play the game

        goal=random.randint(1, 100)
        print("The goal for this round is: " + str(goal)) #(4) Generate a random number between 1-100 and set it as goal
        
        betmoney = input("How much would you like to bet：") #(5)Ask user how much they would like to bet
        if (is_number(betmoney) == False):
            print ("This is an invalid input.")
            break
        elif (float(betmoney) < 0):
            print ("Bet cannot be negative.")
            break
        elif (float(betmoney) > money):
            print ("Bet cannot be larger than your balance.") #Extensive error checking (requested at the end of the problem) 
            break

        six=input("This is Six-Sided Dice. How many times would you like to roll: ")
        ten=input("This is Ten-Sided Dice. How many times would you like to roll: ")
        twenty=input("This is Twenty-Sided Dice. How many times would you like to roll: ")

        cupfilldice=cup(int(six), int(ten), int(twenty))
        cupfilldice.roll() #(6)Roll result
        print("\nBelow is the result of your rolls: ") 
        print(cupfilldice)  

        sumresult=cupfilldice.getSum() #(6)Sum of Rolled Result ---pass func
        print("\n" + str(name)+ ", the total sum of your rolling is:" + str(sumresult)+"\n")
        
#Balance Counting
        if (sumresult==goal): 
            money=money+10*float(betmoney)
            print(str(name)+",the roll matches the goal. You have won 10 times of the bet money, now your total is: "+str(money)+"\n")
        elif (abs(sumresult-goal)<= 5):
            money = money + 5 * float(betmoney)
            print (str(name)+",the roll is within 5 of the goal. You have won 5 times of the bet money. Your balance now is: " + str(money)+"\n")
        elif (abs(sumresult-goal) <= 10):
            money = money + 2 * float(betmoney)
            print (str(name)+",the roll is within 10 of the goal. you have won 2 times of the best money. Your balance now is: " + str(money)+"\n")
        else:
            money=money+ 0 * float(betmoney) 
            print(str(name)+",your roll fail to match or within 5/10 range of the goal. You do not earn any money. Your balance now is: " + str(money)+"\n")
    

        
        
        
