from random import randint
import statistics
def RNG_English(hit, crit):
    hitnum1 = randint(0,100) # Generates a random number between 0 and 100
    hitnum2 = randint(0,100) # Generates a random number between 0 and 100
    critnum = randint(0, 100) # Generates a random number between 0 and 100
    hit_avg = statistics.mean([hitnum1, hitnum2]) # Averages the 2 hit numbers
    if hit_avg <= hit:
        print("You've hit the enemy!") # If the averaged number is below the hit chance, it will hit the attack.
        if critnum <= crit:
            print("It was a critical attack Big Damage!") # If the critnum is below the crit chance, it will be a crit.
    else:
        print("You missed the attack!") # If the averaged number is above the hit chance, it misses.
def RNG_Japan(hit,crit):
    hitnum1 = randint(0, 100)# Generates a random number between 0 and 100
    critnum = randint(0, 100)# Generates a random number between 0 and 100
    if hitnum1 <= hit:
        print("You've hit the enemy!") # If the single random number is below the hit chance, it will hit the attack.
        if critnum >= crit:
            print("It was a critical attack Big Damage!") # If the critnum is below the crit chance, it will be a crit.
    else:
        print("You missed the attack!") # In case the random number is above the hit chance, it misses
def main():
    while True:
        hit_chance = int(input("Insert your HIT chance (1 - 100) " ))
        crit_chance = int(input("Insert your CRIT chance (1 - 100) " ))
        option = int(input("If you want to simulate an RNG English System, press 1, if you want to simulate the RNG Japan System, press 2 " ))
        if option == 1:
            RNG_English(hit_chance, crit_chance)
            option2 = int(input("Press 1 to restart the simulation, 2 to exit "))
            if option2 == 2:
                break
        elif option == 2:
            RNG_Japan(hit_chance, crit_chance)
            option2 = int(input("Press 1 to restart the simulation, 2 to exit "))
            if option2 == 2:
                break
        else:
            print("That's not a correct option! Please try again. ")
    exit()
if __name__ == "__main__":
    main()

