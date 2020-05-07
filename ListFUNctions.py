
LuckyNumbers = [1, 5, 7, 3, 4, 14, 19, 21]
Cool_People = ["Chris", "Cole", "Ryan","Ethan", "Ethan", "Hana", "Kris"]
Cool_People.extend(LuckyNumbers)
Cool_People.append("Mason")
Cool_People.insert(1, "Behram")
Cool_People.remove("Hana")
Cool_People.pop()
print(Cool_People.index("Ryan"))
print(Cool_People.count("Ethan"))
LuckyNumbers.sort()
LuckyNumbers.reverse()
Cool_People2 = Cool_People.copy()

print(Cool_People)
print(LuckyNumbers)
print(Cool_People2)