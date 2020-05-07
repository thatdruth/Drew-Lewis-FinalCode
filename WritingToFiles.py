

#Name_file = open("NamesForReading.txt", "a")

#Name_file.write("Sean - Suite Guy") #be careful not to run this again once done can mess up your file

#Name_file.write("\nNaji - Best Neighbor")

#Name_file = open("NamesForReading.txt", "w") Will overwrite and only include what is written in this command

Name_file = open("NamesForReading1.txt", "w") #adding a number makes a new file with the same name except for the number

Name_file.write("\nMarcellus - Doorman")

Name_file.close()