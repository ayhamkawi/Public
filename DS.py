## Data structure example


films = {
            "Finding Dory":[3,5],
            "Tarazan":[18,1]
            }


while True:
            choice = input("The film you like: ").strip().title()
            print (films[choice])

            if choice in films:
                        age=int(input("your age?").strip())
                        ## AgE
                        if age>=films[choice][0]:
                                    print ("Playing {}".format(choice))
                                    #Tickets number
                                    if films[choice][1]>0:
                                                print ("There is tickets!!")
                                                films[choice][1]=films[choice][1]-1
                                                print (films[choice][1])
                                    elif films[choice][1]<=0:
                                                print ("Sorry, no tickets avaiable")
                        else: print ("You cannot watch that")
            else:
                        print("We do not have this one")
                        
