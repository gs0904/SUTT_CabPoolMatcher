from classes import RideRequest, Cab
waiting=[]
cabs= []
def add_request():
    name= input("Enter name: ").title()
    if name.strip() == "":
        print("cannot be empty")
        return
    destination= input("Enter destination (Delhi/Jaipur): ").title()
    if destination not in ["Delhi", "Jaipur"]:
        print("Invalid")
        return
    time_slot= input("Enter time slot (Morning/Afternoon/Evening/Night): ").title()
    if time_slot not in ["Morning", "Afternoon", "Evening", "Night"]:
        print("Invalid time slot")
        return
    year= int(input("Enter year (1-5): "))
    if not year.isdigit() or int(year)<1 or int(year)>5:
        print("Invalid year")
        return

    student = RideRequest(name, destination, time_slot, year)
    waiting.append(student)
    print("Request added")

def main():
    while True:
        print("\nCab Pool Matcher")
        print("1. Add ride request")
        print("2. View waiting students and cabs")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice== "1":
            add_request()
        elif choice== "2":
            print(":)")
        elif choice== "3":
            print("Byeee")
            break
        else:
            print("Invalid choice")
main()