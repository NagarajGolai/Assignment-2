# (b) Develop a program to reas the name and year of birth of a person. Display whether the person is a senior citizen or not.
import datetime
name = input("Enter the name of the person: ")
birth_year = int(input("Enter the year of birth of the person: "))
today = datetime.date.today()
year = today.year
age = year - birth_year
if age >= 60:
print(name + "is a senior citizen")
else:
print(name + "is not a senior citizen")