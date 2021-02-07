kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")
kirjain = "a"

if kirjain1 < kirjain2 < kirjain3:
    kirjain = kirjain2
elif kirjain1 < kirjain3 < kirjain2:
    kirjain = kirjain3
elif kirjain2 < kirjain1 < kirjain3:
    kirjain = kirjain1
elif kirjain2 < kirjain3 < kirjain1:
    kirjain = kirjain3
elif kirjain3 < kirjain1 < kirjain2:
    kirjain = kirjain1
elif kirjain3 < kirjain2 < kirjain1:
    kirjain = kirjain2
print(f"Keskimmäinen kirjain on {kirjain}")
