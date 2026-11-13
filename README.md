
# Cab Pool Matcher

This project contains a Python-based cab pooling application for SUTT Recruitment-Task 1.

It allows students travelling to Delhi and Jaipur to submit ride requests, find matching cabs and share rides based on their destination and time slot. It also uses a priority queue to give preference to students in higher academic years.

## Contents

- `main.py` - Contains the main menu and handles ride requests, viewing, matching and cab dispatch.
- `classes.py` - Defines the `RideRequest` and `Cab` classes.
- `data.py` - Loads cab details from the JSON file.
- `cabs.json` - Contains the list of available cabs with their driver names, seat capacity, destinations and time slots.

## Prerequisites

Before running the project, ensure you have:

- Python 3 installed.
- No additional libraries are required. The project uses Python's standard library.

## How to Run

1. Clone or download the repository.
2. Open the project folder in the terminal.
3. Run the following command:

```bash
python main.py
```

The application will display a menu through which users can add ride requests, view waiting students and cabs, find matches and dispatch cabs.

## Cab File Format

The available cabs are stored in `cabs.json`.

Each cab contains the following details:
- Driver name
- Number of seats
- Destination (Delhi or Jaipur)
- Time slot (Morning, Afternoon, Evening or Night)

## Priority System

Students are grouped according to their destination and time slot. A priority queue is maintained for each group using Python's `heapq` module.

Students from higher academic years are given priority. If two students belong to the same year, the one who submitted their request earlier gets priority.

## Tricky Situations

### 1. Half-empty Cab

A cab can be dispatched even if all its seats are not occupied. For example, a cab with four seats can leave with just one or two students. Once dispatched, it is marked as departed and cannot take any more students.

### 2. No Cabs Left

If all cabs for a particular destination and time slot have already departed, new students remain in the waiting list. They are not removed unless they are actually assigned to a cab.

### 3. Same Year

Students from higher academic years get priority. If two students belong to the same year, the one who submitted their request earlier gets priority. This is handled using the request timestamp and the position of the request in the waiting list.

### 4. Lots of Students (1,000 Requests)

Let `n` represent the number of waiting students and `c` represent the number of cabs.

| Operation | Time Complexity | Reason |
|---|---|---|
| Add one request | O(1) | Appending a request to the waiting list takes constant time. |
| Add 1,000 requests | O(n) | Each request is added once. |
| Dispatch one cab | O(n log n) | Priority queues are created from the waiting students before assigning students to the cab. |
| Find an open cab | O(c) | The cab list is checked until an open cab is found. |
