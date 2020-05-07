
#I wake up
#If I am groggy
    #I take a shower

#I leave my apartment
#If its raining
    #I put on a coat
#otherwise
    #I leave my coat at home

#I am on a date 
#If I am hungry
    #We go out to eat 
#otherwise If I am tired 
    #We watch a movie
#otherwise
    #We talk about our day 


is_male = False
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not (is_tall):
    print("You are a male but not tall")
elif not(is_male) and is_tall:
    print("You are not male but you are tall")
else:
    print("You are neither male nor tall")