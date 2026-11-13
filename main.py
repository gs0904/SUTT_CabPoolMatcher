from classes import RideRequest, Cab
from data import load_cabs
import heapq
waiting=[]
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
    year= input("Enter year (1-5): ")
    if not year.isdigit() or int(year)<1 or int(year)>5:
        print("Invalid year")
        return
    year=int(year)

    student = RideRequest(name, destination, time_slot, year)
    waiting.append(student)
    print("Request added")

def view():
    print("\n ---Waiting Students---> ")

    if len(waiting)==0:
        print("No students waiting.")
    else:
        for student in waiting:
            print(student.name, student.destination, student.time_slot, student.year)

    print("\nCabs -> ")

    if len(cabs)==0:
        print("No cabs available.")
    else:
        for cab in cabs:
            print(cab.driver, cab.destination, cab.time_slot)
            print("Seats:", len(cab.students), "/", cab.seats)
            print("Departed:", cab.has_left)

def make_queues():
    queues = {}
    for i, student in enumerate(waiting):
        key = (student.destination, student.time_slot)
        if key not in queues:
            queues[key] = []
        heapq.heappush(queues[key], (-student.year, student.requested_at, i, student))
    return queues

def find_matches():
    matched = waiting.copy()

    for cab in cabs:
        if cab.has_left:
            continue

        print("\nCab:", cab.driver)
 
        count = 0
        for student in matched[:]:
            if student.destination==cab.destination and student.time_slot==cab.time_slot:
                if count< cab.seats-len(cab.students):
                    print(student.name, "- Year", student.year)
                    matched.remove(student)
                    count+=1
        if count==0:
            print("No matching students")

def dispatch():
    print("\n---Available Cabs---")
    for i, cab in enumerate(cabs):
        if not cab.has_left:
            print(i+1, cab.driver, "-", cab.destination, "-", cab.time_slot)

    num = int(input("Enter cab number: "))

    if num<1 or num>len(cabs):
        print("Invalid cab number")
        return

    cab = cabs[num-1]

    if cab.has_left:
        print("This cab has already left.")
        return

    queues=make_queues()
    key=(cab.destination, cab.time_slot)
    count=0

    if key in queues:
        while queues[key] and len(cab.students) < cab.seats:
            student=heapq.heappop(queues[key])[3]
            cab.students.append(student)
            waiting.remove(student)
            count+=1 

    if count==0:
        print("No matching students available.")
        return

    cab.has_left=True

    print("Cab dispatched.")
    print("Students travelling:")
    for student in cab.students:
        print(student.name)

def main():
    while True:
        print("\n---Cab Pool Matcher---")
        print("1. Add ride request")
        print("2. View waiting students and cabs")
        print("3. Quit")
        print("4. Find matches")
        print("5. Dispatch cab")

        choice = input("Enter your choice: ")

        if choice== "1":
            add_request()
        elif choice== "2":
            view()
        elif choice== "3":
            print("Byeee")
            break
        elif choice == "4":
            find_matches()
        elif choice == "5":
            dispatch()
        else:
            print("Invalid choice")

cabs=load_cabs()
main()
