while True:
    print ("__________Welcome to the Bill Splittert App!_________")
    print("")

    bill=float(input ("Enter total bill amount:",))
    if bill<0:
        print("bill can't be negetive.")

    people=int (input ("Enter number of people:",))
    if people<=0:
        print ("people must have be more than 0:",)

    tip= int (input ("Enter tip percentage (o/5/10/20):"))
    if tip not in (0,5,10,15,20):
        print("invalide tip percentage")

    print("")
    tip=(tip/100)*bill
    print("tip:", tip)
    total=bill+tip
    print("total:", total)
    person=total/people
    print ("per person:", person)
    print("")

    again = input("Would you like to calculate another bill? (y/n): ")
    if again != 'y':
        print("Thank you for using the Bill Splitter App!")
        break

'''
__________Welcome to the Bill Splittert App!_________

Enter total bill amount:50000
Enter number of people:5
Enter tip percentage (o/5/10/20):20

tip: 10000.0
total: 60000.0
per person: 12000.0

Would you like to calculate another bill? (y/n): n
Thank you for using the Bill Splitter App!
'''
