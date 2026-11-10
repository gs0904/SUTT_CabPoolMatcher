from classes import RideRequest, Cab
waiting=[]
cabs= []
def add_request():
    name= input("Enter name: ")
    destination= input("Enter destination (Delhi/Jaipur): ")
    time_slot= input("Enter time slot (Morning/Afternoon/Evening/Night): ")
    year= int(input("Enter year (1-5): "))

    student = RideRequest(name, destination, time_slot, year)
    waiting.append(student)
    print("Request added successfully!")

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