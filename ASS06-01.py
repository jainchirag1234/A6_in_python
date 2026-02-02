# Q.1. Write a Menu Driven (Menu: PUSH, POP, PEEP, PRINT, EXIT) program in Python to
# implement stack operations on a stack of integers using a class consisting of attributes
# Stack (a List consisting of elements of the Stack) and TOP, and methods PUSH, POP,
# PEEP and PRINT.


Stack = []
top = 0
while True :
    print("\nPress 1 for PUSH.")
    print("Press 2 for POP.")
    print("Press 3 for PEEP.")
    print("Press 4 for PRINT.")
    print("Press 5 for EXIT.")
    try :
        n = int(input("Enter your choice : "))
        if n == 1 :
            try :
                insert = int(input("\nEnter Value : "))
                Stack.append(insert)
                top = insert
            except :
                print("\nEnter only numeric value.")
        elif n == 2 :
            if Stack  != [] :
                print("\nItem deleted which value is ", top)
                Stack.remove(top)
                if len(Stack) == 0 :
                    Stack = []
                    top = 0
                else :
                    top = Stack[len(Stack)-1]
            else : 
                print("\nStack is empty.")
        elif n == 3 :
            flag = False
            Search = int(input("Enter Number for Search : "))
            for peep in Stack :
                if peep == Search :
                    flag = True
            if flag == False :
                print(Search ," is not Present in the Stack")
            else :
                print(Search, " is Present in the Stack")
        elif n == 4 :
            if Stack != [] :
                print("\n", Stack)
            else :
                print("\nStack is empty.")
        elif n == 5 :
            break
        else :
            print("\nEnter valid choice.")   
    except :
        print("\nEnter only numeric value.")