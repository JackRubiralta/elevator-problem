# Problem: Elevator Optimization

## Problem Setup

You are given a list of pairs. Each pair represents a person where:
- The first number is the **floor where the person is currently located**.
- The second number is the **floor where they want to go**.

The elevator starts at a given floor `n`.

### Task

Your task is to create a C++ program that calculates the **total distance** traveled by the elevator to pick up and drop off all the people in the optimal order.

### Requirements

- **Input**: A list of pairs, each representing a person `(currentFloor, targetFloor)`, and an integer `startingFloor` representing the initial position of the elevator.
- **Output**: The total number of floors traveled by the elevator to fulfill all requests.
- **Optimization Goal**: Minimize the total travel distance.

### Example

**Input**:  
`people = [(1, 5), (6, 2), (4, 3)]`  
`startingFloor = 3`

**Expected Output**:  
`Total distance traveled: 12`

---

## C++ Class Definition

You are given a partial class `Elevator`. Your task is to complete the `emptyElevator` method to optimize the route of the elevator and calculate the total distance traveled.

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Elevator {
private:
    int currentFloor;
    int totalMovement;
    vector<pair<int, int>> peopleWaiting;
    vector<pair<int, int>> peopleInElevator;

public:
    Elevator(int startFloor) {
        // Initializes the Elevator with a starting floor.
        currentFloor = startFloor;
        totalMovement = 0;
    }

    void addPeople(const vector<pair<int, int>>& people) {
        // Adds a list of people to the waiting list.
        peopleWaiting.insert(peopleWaiting.end(), people.begin(), people.end());
    }

    void goToFloor(int floor) {
        totalMovement += abs(currentFloor - floor);
        currentFloor = floor;
    }

    void dropOff() {
        // Drop off people at the current floor.
        peopleInElevator.erase(
            remove_if(peopleInElevator.begin(), peopleInElevator.end(),
                      [this](const pair<int, int>& person) { return person.second == currentFloor; }),
            peopleInElevator.end()
        );
    }

    void pickUp() {
        // Pick up people at the current floor.
        vector<pair<int, int>> toPickUp;
        for (const auto& person : peopleWaiting) {
            if (person.first == currentFloor) {
                toPickUp.push_back(person);
            }
        }

        peopleInElevator.insert(peopleInElevator.end(), toPickUp.begin(), toPickUp.end());

        peopleWaiting.erase(
            remove_if(peopleWaiting.begin(), peopleWaiting.end(),
                      [this](const pair<int, int>& person) { return person.first == currentFloor; }),
            peopleWaiting.end()
        );
    }

    bool isEmpty() const {
        return peopleWaiting.empty() && peopleInElevator.empty();
    }

    int emptyElevator() {
        // Your code goes here
        return totalMovement;
    }
};
```

## Test Cases

The following test cases evaluate the functionality and correctness of the `Elevator` class in various scenarios. Each test is designed to check if the elevator can successfully pick up and drop off all passengers while minimizing the total travel distance.

```cpp
void testElevator() {
    // Test 1: Basic example
    Elevator elevator(3);
    vector<pair<int, int>> people1 = {{1, 5}, {6, 2}, {4, 3}, {3, 8}};
    elevator.addPeople(people1);
    int totalDistance1 = elevator.emptyElevator();
    cout << "Test 1: Got distance of: " << totalDistance1 << endl;
    if (!elevator.isEmpty()) {
        cout << "Test 1 Failed: Elevator not empty!" << endl;
    }

    // Test 2: All people on the same target floor
    elevator = Elevator(0);
    vector<pair<int, int>> people2 = {{1, 3}, {2, 3}, {0, 3}};
    elevator.addPeople(people2);
    int totalDistance2 = elevator.emptyElevator();
    cout << "Test 2: Got distance of: " << totalDistance2 << endl;
    if (!elevator.isEmpty()) {
        cout << "Test 2 Failed: Elevator not empty!" << endl;
    }

    // Test 3: Starting with an empty elevator
    elevator = Elevator(5);
    int totalDistance3 = elevator.emptyElevator();
    cout << "Test 3: Got distance of: " << totalDistance3 << endl;
    if (!elevator.isEmpty()) {
        cout << "Test 3 Failed: Elevator not empty!" << endl;
    }

    // Test 4: Single person to drop off
    elevator = Elevator(10);
    vector<pair<int, int>> people4 = {{10, 0}};
    elevator.addPeople(people4);
    int totalDistance4 = elevator.emptyElevator();
    cout << "Test 4: Got distance of: " << totalDistance4 << endl;
    if (!elevator.isEmpty()) {
        cout << "Test 4 Failed: Elevator not empty!" << endl;
    }

    // Test 5: Multiple stops
    elevator = Elevator(2);
    vector<pair<int, int>> people5 = {{2, 10}, {10, 3}, {5, 12}, {3, 1}, {6, 8}, {8, 2}, {4, 7}, {7, 5}, {12, 1}, {1, 6}};
    elevator.addPeople(people5);
    int totalDistance5 = elevator.emptyElevator();
    cout << "Test 5: Got distance of: " << totalDistance5 << endl;
    if (!elevator.isEmpty()) {
        cout << "Test 5 Failed: Elevator not empty!" << endl;
    }
}

int main() {
    testElevator();
    return 0;
}
```
