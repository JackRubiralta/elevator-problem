from typing import List, Tuple
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
        # Filter out people who want to get off at the current floor
        self.people_in_elevator = [(start, destination) for start, destination in self.people_in_elevator if destination != self.current_floor]

    def pick_up(self) -> None:
        """Picks up people at the current floor and moves them from waiting to in the elevator."""
        # Move people waiting at the current floor to the elevator
        people_to_pick_up = [(start, destination) for start, destination in self.people_waiting if start == self.current_floor]
        self.people_in_elevator.extend(people_to_pick_up)
        
        # Remove picked-up people from the waiting list
        self.people_waiting = [(start, destination) for start, destination in self.people_waiting if start != self.current_floor]


    def empty_elevator2(self) -> int:
        """Goes to each floor and drops off all remaining people."""
        while self.people_waiting or self.people_in_elevator:
            # Drop off people at the current floor
            self.drop_off()
            # Pick up people waiting at the current floor
            self.pick_up()
            
            # If there are still people to transport
            if self.people_in_elevator or self.people_waiting:
                # Get the list of next floors to visit
                next_floors = []
                if self.people_in_elevator:
                    next_floors.extend([destination for (_, destination) in self.people_in_elevator])
                if self.people_waiting:
                    next_floors.extend([start for (start, _) in self.people_waiting])
                
                # Find the closest floor to move to next
                next_floor = min(next_floors, key=lambda floor: abs(self.current_floor - floor))
                # Move the elevator to the next floor
                self.go_to_floor(next_floor)
            else:
                # No more people to transport
                break
        return self.total_movement
    
    def empty_elevator(self) -> int:
        """Optimized method: Goes up to pick up and drop off people, then goes down to the lowest floor with people, and finally drops off the rest."""
        if not self.people_waiting and not self.people_in_elevator:
            return self.total_movement

        # Step 1: Go up and pick up/drop off everyone on the way up
        # Collect the list of floors where people are waiting or want to go to
        all_floors_up = sorted(set(
            [floor for floor, _ in self.people_waiting if floor >= self.current_floor] +
            [destination for _, destination in self.people_waiting + self.people_in_elevator if destination >= self.current_floor]
        ))

        for floor in all_floors_up:
            # Move to the current floor
            self.go_to_floor(floor)
            # Drop off anyone who needs to get off at this floor
            self.drop_off()
            # Pick up anyone waiting at this floor
            self.pick_up()

        # Step 2: Go down to pick up/drop off everyone on the way down
        all_floors_down = sorted(set(
            [floor for floor, _ in self.people_waiting if floor < self.current_floor] +
            [destination for _, destination in self.people_waiting + self.people_in_elevator if destination < self.current_floor]
        ), reverse=True)

        for floor in all_floors_down:
            # Move to the current floor
            self.go_to_floor(floor)
            # Drop off anyone who needs to get off at this floor
            self.drop_off()
            # Pick up anyone waiting at this floor
            self.pick_up()

        # Final Step: Drop off anyone still in the elevator by going up again
        final_drop_off_floors = sorted(set(
            [destination for _, destination in self.people_in_elevator]
        ))

        for floor in final_drop_off_floors:
            # Move to the current floor
            self.go_to_floor(floor)
            # Drop off anyone who needs to get off at this floor
            self.drop_off()

        return self.total_movement



def test_elevator() -> None:
    # Test 1: Basic example
    elevator = Elevator(start_floor=3)
    elevator.add_people([(1, 5), (6, 2), (4, 3)])
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
    elevator.add_people([(2, 5), (5, 2), (2, 4)])
    total_distance = elevator.empty_elevator()
    assert len(elevator.people_in_elevator) == 0 and len(elevator.people_waiting) == 0, f"Test 5 Failed: Elevator not empty!"
    print(f"Test 5: Got distance of: {total_distance}")

# Run the tests
test_elevator()