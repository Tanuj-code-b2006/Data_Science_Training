"""
#making a list
lst=[]
n=int(input("Enter number of elements you want to add inside list:"))
for i in range (0,n):
    ele=input("Enter element you want to add in the list:")
    lst.append(ele)
print(lst)
"""


"""
#making a dictionary 
dct={}
n_d=int(input("Enter number of key-value pairs you wanna add in dictionary:"))
key=input("Enter key:")
value=input("Enter value:")

for i in range(0,n_d):
    key=input("Enter key:")
    value=input("Enter value:")
    dct[key]=value
print("Final dictionary:",dct)
"""


# World Cup data
world_cup_2021 = (2021, "Qatar", "Argentina")

world_cup_2027 = {
    "year": 2027,
    "host_country": "TBD",
    "winner": "TBD"
}

# User input
year = int(input("Enter the year (2021 or 2027): "))
if year == 2021:
    print("\n2021 World Cup Information")
    print("Year:", world_cup_2021[0])
    print("Host country:", world_cup_2021[1])
    print("Winner:", world_cup_2021[2])
elif year == 2027:
    print("\n2027 World Cup Information")
    print("Year:", world_cup_2027["year"])
    print("Host country:", world_cup_2027["host_country"])
    print("Winner:", world_cup_2027["winner"])
    choice = input("Do you want to update information for 2027? (y/n): ")
    if choice.lower() == 'y':
        world_cup_2027["host_country"] = input("Enter the new host country: ")
        world_cup_2027["winner"] = input("Enter the new winner: ")

        print("\nUpdated 2027 World Cup Information")
        print("Year:", world_cup_2027["year"])
        print("Host country:", world_cup_2027["host_country"])
        print("Winner:", world_cup_2027["winner"])
    else:
        print("No updates made.")
else:
    print("Sorry, wrong year input.")
