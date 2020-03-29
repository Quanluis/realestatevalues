def main ():

    import statistics

    print("Real Estate Values")
    print("******************************")

    def houses():

        houses = []
        
        while True:

            answer =  int(input("Enter cost of one home or 0 to quit"))

            if answer > 0:

                houses.append(answer)

                continue
                         
            else:
                print("Prices of homes in your area")
                houses.sort()
                print(houses)

                print("The median value is $ ", statistics.median(houses))
        

                print("The average sale price is $ ", sum(houses) / len(houses))
                
                print("The minimum sale price is $ ", houses[0])
                print("The maximum sale price is $ ", houses.pop())
                break
                
    def values():

        houses()

    values()

main()
