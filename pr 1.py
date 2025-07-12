print('Welcome to Introduction')
print("")
Name = input ("Enter you Name:")
Age = int(input ("Enter you Age:"))
Height = float(input ("Enter you Height:"))
Favourite = int(input ("Enter you Favourite Number:"))
print("")
print("Thank you! Here is the information we collected")
print("")
print("Name:",Name,"type:",type(Name),"Memory Address:",id(Name))
print("Age:",Age,"type:",type(Age),"Memory Address:",id(Age))
print("Height:",Height,"type:",type(Height),"Memory Address:",id(Height))
print("Favourite:",Favourite,"type:",type(Favourite),"Memory Address:",id(Favourite))
print("")

import datetime

age=int(input("how old are you?"))
current_year=datetime.datetime.now().year
birth_year=current_year - age
print("you were born in",birth_year)

'''
Welcome to Introduction

Enter you Name:smit
Enter you Age:17
Enter you Height:5.87
Enter you Favourite Number:2426

Thank you! Here is the information we collected

Name: smit type: <class 'str'> Memory Address: 2486283580688
Age: 17 type: <class 'int'> Memory Address: 140727030582200
Height: 5.87 type: <class 'float'> Memory Address: 2486329172240
Favourite: 2426 type: <class 'int'> Memory Address: 2486279935984

how old are you?17
you were born in 2008

'''
