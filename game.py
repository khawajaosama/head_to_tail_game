k=0
a = 0
while k<3:
    from random import randint

    res = randint(1, 6)

    print("-----------------------------")
    try:
        Number = int(input("Enter Your No 1 till 6: "))

        if Number > 0 and Number < 7:
            res = str(res)

            print("My Number is " + res)

            res = int(res)

            if res != Number:

                a += Number
                a = str(a)
                print("Your Score is = " + a)
                a = int(a)
            else:
                print("You Lose")
                k += 1
                if k == 1:
                    print("-----------------")
                    print("2 Lives Remaining")
                if k == 2:
                    print("-----------------")
                    print("1 Lives Remaining")

                if k == 3:
                    print("-----------------")
                    print("Game Over")
                    print("No Lives Remaining")
                    print("------------------")
                    k=k+1

                    while k == 4:
                        start = input("Type Y = Continue       OR       Type N = Exit")
                        if start == "Y" or start == "y":
                            k = 0
                            a = 0
                        elif start == "N" or start =="n":
                            print("----------------------------")
                            print("Thanks For Playing!")
                            k=5

                        else:
                            print("---------------------------")
                            print("Invalid Selection")
                            k=4



        else:
            print("Incorrect Value , Value is not from 1 till 6")


    except ValueError:
        print("You enterd a String, Please Enter a Number")