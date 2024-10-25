# Problem: Elevator Optimization

## Problem Setup

You are given a list of pairs. Each pair represents a person where:
- The first number is the **floor where the person is currently located**.
- The second number is the **floor where they want to go**.

The elevator starts at a given floor `n`.

### Task

Your task is to create a Python program that calculates the **total distance** traveled by the elevator to pick up and drop off all the people in the optimal order.

### Requirements

- **Input**: A list of pairs, each representing a person `(current_floor, target_floor)`, and an integer `starting_floor` representing the initial position of the elevator.
- **Output**: The total number of floors traveled by the elevator to fulfill all requests.
- **Optimization Goal**: Minimize the total travel distance.

### Example

**Input**:  
`people = [(1, 5), (6, 2), (4, 3)]`  
`starting_floor = 3`

**Expected Output**:  
`Total distance traveled: 12`

---

## Class Definition

You are given a partial class `Elevator`. Your task is to complete the `solve_elevator_problem` method to optimize the route of the elevator and calculate the total distance traveled.

```python
from typing import List, Tuple

class Elevator:
    def __init__(self, start_floor: int) -> None:
        """Initializes the Elevator with a starting floor."""
        self.current_floor: int = start_floor
        self.total_movement: int = 0
        self.people_waiting: List[Tuple[int, int]] = []
        self.people_in_elevator: List[Tuple[int, int]] = []

    def add_people(self, people: List[Tuple[int, int]]) -> None:
        """Adds a list of people to the waiting list."""
        self.people_waiting.extend(people)

    def go_to_floor(self, floor: int) -> None:
        """Moves the elevator to the specified floor, updating total movement."""
        self.total_movement += abs(self.current_floor - floor)
        self.current_floor = floor

    def drop_off(self) -> None:
        """Drops off people at the current floor."""
        self.people_in_elevator = [(start, destination) for start, destination in self.people_in_elevator if destination != self.current_floor]

    def pick_up(self) -> None:
        """Picks up people at the current floor and moves them from waiting to in the elevator."""
        people_to_pick_up = [(start, destination) for start, destination in self.people_waiting if start == self.current_floor]
        self.people_in_elevator.extend(people_to_pick_up)
        self.people_waiting = [(start, destination) for start, destination in self.people_waiting if start != self.current_floor]


    def empty_elevator(self) -> int:
        """Goes to each floor and drops off all remaining people."""
       
        # your code goes here
        return self.total_movement
```

## Test Cases

The following test cases evaluate the functionality and correctness of the `Elevator` class in various scenarios. Each test is designed to check if the elevator can successfully pick up and drop off all passengers while minimizing the total travel distance. 

```python

def test_elevator() -> None:
    # Test 1: Basic example
    elevator = Elevator(start_floor=3)
    elevator.add_people([(1, 5), (6, 2), (4, 3), (3, 8)])
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 1 Failed: Elevator not empty!"
    print(f"Test 1: Got distance of: {total_distance}")


    # Test 2: All people on the same target floor
    elevator = Elevator(start_floor=0)
    elevator.add_people([(1, 3), (2, 3), (0, 3)])
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 2 Failed: Elevator not empty!"
    print(f"Test 2: Got distance of: {total_distance}")


    # Test 3: Starting with an empty elevator
    elevator = Elevator(start_floor=5)
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 3 Failed: Elevator not empty!"
    print(f"Test 3: Got distance of: {total_distance}")


    # Test 4: Single person to drop off
    elevator = Elevator(start_floor=10)
    elevator.add_people([(10, 0)])
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 4 Failed: Elevator not empty!"
    print(f"Test 4: Got distance of: {total_distance}")

    # Test 5: Multiple stops
    elevator = Elevator(start_floor=2)
    elevator.add_people([(2, 10), (10, 3), (5, 12), (3, 1), (6, 8), (8, 2), (4, 7), (7, 5), (12, 1), (1, 6)])
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 5 Failed: Elevator not empty!"
    print(f"Test 5: Got distance of: {total_distance}")

# Run the tests
test_elevator()
```
