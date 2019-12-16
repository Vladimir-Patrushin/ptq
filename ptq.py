points = 0

rules = input ("POINT TRACKER QUIZ \n \n \n \n \nRules: \n   1.  Only answer with given answers. \n   2.  This is a test, please send any mistakes in the following email: vpatrushin@gmail.com \nPlease press . to continue\n\n")
if rules == ".":
    one = input ("\nWho is the president of russia? (2019) \nDonald Trump, Tony Stark, Vladimir Putin, or Xi Jinpin? \nPlease answer EXACTLY like in the question.\n\n")

if one == "Vladimir Putin":
    points += 1
    print("\n\nCongratulations! You answered correctly! You have " + str(points) + " points!")

else:
    print("\n\nOh, No! Sorry, but that was the wrong answer, its acually 'Vladimir Putin', you still have " + str(points) + " points. ;-; Maybe next time!")

two = input ("\nWhen was Nintendo created?\nApril 21, 1989 | Sep 23, 1889 | Nov 15, 2001 | Feb 22, 2002 or March 14, 2002?\nPlease answer EXACTLY like in the question.\n\n")

if two == "Sep 23, 1889":
    points += 1
    print("\n\nCongratulations! You answered correctly! You have " + str(points) + " points!")

else:
    print("\n\nOh, No! Sorry, but that was the wrong answer, its acually 'Sep 23, 1889', you still have " + str(points) + " points. ;-; Maybe next time!")
