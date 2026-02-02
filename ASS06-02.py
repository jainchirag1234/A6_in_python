# # Q.2. Write a Menu Driven (Menu: INSERT, DELETE, PRINT, EXIT) program in Python to
# implement Simple Queue Operations on a simple queue of integers using a class
# consisting of attributes SQueue (a list consisting of elements of the Simple Queue),
# Front and Rear and methods INSERT, DELETE and PRINT.

Queue = []
top = 0
while True :
    print("\nPress 1 for INSERT.")
    print("Press 2 for DELETE.")
    print("Press 3 for PRINT.")
    print("Press 4 for EXIT.")
    try :
        n = int(input("Enter your choice : "))
        if n == 1 :
            try :
                insert = int(input("\nEnter Value : "))
                Queue.append(insert)
                top = insert
            except :
                print("\nEnter only numeric value.")
        elif n == 2 :
            if Queue  != [] :
                print(Queue[0], " delete")
                Queue.pop(0)
            else : 
                print("\nQueue is empty.")
        elif n == 3 :
            if Queue != [] :
                print("\n", Queue)
            else :
                print("\nQueue is empty.")
        elif n == 4 :
            break
        else :
            print("\nEnter valid choice.")   
    except :
        print("\nEnter only numeric value.")