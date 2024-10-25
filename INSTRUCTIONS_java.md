# Problem: Elevator Optimization

## Problem Setup

You are given a list of pairs. Each pair represents a person where:
- The first number is the **floor where the person is currently located**.
- The second number is the **floor where they want to go**.

The elevator starts at a given floor `n`.

### Task

Your task is to create a Java program that calculates the **total distance** traveled by the elevator to pick up and drop off all the people in the optimal order.

### Requirements

- **Input**: A list of pairs, each representing a person `(currentFloor, targetFloor)`, and an integer `startingFloor` representing the initial position of the elevator.
- **Output**: The total number of floors traveled by the elevator to fulfill all requests.
- **Optimization Goal**: Minimize the total travel distance.

---

## Java Class Definition

You are given a partial class `Elevator`. Your task is to complete the `emptyElevator` method to optimize the route of the elevator and calculate the total distance traveled.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Elevator {
    private int currentFloor;
    private int totalMovement;
    private List<int[]> peopleWaiting;
    private List<int[]> peopleInElevator;

    public Elevator(int startFloor) {
        this.currentFloor = startFloor;
        this.totalMovement = 0;
        this.peopleWaiting = new ArrayList<>();
        this.peopleInElevator = new ArrayList<>();
    }

    public void addPeople(List<int[]> people) {
        this.peopleWaiting.addAll(people);
    }

    public void goToFloor(int floor) {
        this.totalMovement += Math.abs(this.currentFloor - floor);
        this.currentFloor = floor;
    }

    public void dropOff() {
        // Drop off people at the current floor
        this.peopleInElevator.removeIf(person -> person[1] == this.currentFloor);
    }

    public void pickUp() {
        // Pick up people at the current floor
        List<int[]> toPickUp = new ArrayList<>();
        for (int[] person : this.peopleWaiting) {
            if (person[0] == this.currentFloor) {
                toPickUp.add(person);
            }
        }
        this.peopleInElevator.addAll(toPickUp);
        this.peopleWaiting.removeAll(toPickUp);
    }

    public boolean isEmpty() {
        return this.peopleInElevator.isEmpty() && this.peopleWaiting.isEmpty();
    }

    public int emptyElevator() {
        // Your code goes here
        return this.totalMovement;
    }
}
```

## Test Cases

The following test cases evaluate the functionality and correctness of the `Elevator` class in various scenarios. Each test is designed to check if the elevator can successfully pick up and drop off all passengers while minimizing the total travel distance.

```java
public class TestElevator {
    public static void main(String[] args) {
        // Test 1: Basic example
        Elevator elevator = new Elevator(3);
        List<int[]> people1 = new ArrayList<>(Arrays.asList(new int[]{1, 5}, new int[]{6, 2}, new int[]{4, 3}, new int[]{3, 8}));
        elevator.addPeople(people1);
        int totalDistance1 = elevator.emptyElevator();
        assert elevator.isEmpty() : "Test 1 Failed: Elevator not empty!";
        System.out.println("Test 1: Got distance of: " + totalDistance1);

        // Test 2: All people on the same target floor
        elevator = new Elevator(0);
        List<int[]> people2 = new ArrayList<>(Arrays.asList(new int[]{1, 3}, new int[]{2, 3}, new int[]{0, 3}));
        elevator.addPeople(people2);
        int totalDistance2 = elevator.emptyElevator();
        assert elevator.isEmpty() : "Test 2 Failed: Elevator not empty!";
        System.out.println("Test 2: Got distance of: " + totalDistance2);

        // Test 3: Starting with an empty elevator
        elevator = new Elevator(5);
        int totalDistance3 = elevator.emptyElevator();
        assert elevator.isEmpty() : "Test 3 Failed: Elevator not empty!";
        System.out.println("Test 3: Got distance of: " + totalDistance3);

        // Test 4: Single person to drop off
        elevator = new Elevator(10);
        List<int[]> people4 = new ArrayList<>(Arrays.asList(new int[]{10, 0}));
        elevator.addPeople(people4);
        int totalDistance4 = elevator.emptyElevator();
        assert elevator.isEmpty() : "Test 4 Failed: Elevator not empty!";
        System.out.println("Test 4: Got distance of: " + totalDistance4);

        // Test 5: Multiple stops
        elevator = new Elevator(2);
        List<int[]> people5 = new ArrayList<>(Arrays.asList(new int[]{2, 10}, new int[]{10, 3}, new int[]{5, 12}, new int[]{3, 1}, new int[]{6, 8}, new int[]{8, 2}, new int[]{4, 7}, new int[]{7, 5}, new int[]{12, 1}, new int[]{1, 6}));
        elevator.addPeople(people5);
        int totalDistance5 = elevator.emptyElevator();
        assert elevator.isEmpty() : "Test 5 Failed: Elevator not empty!";
        System.out.println("Test 5: Got distance of: " + totalDistance5);
    }
}
```
