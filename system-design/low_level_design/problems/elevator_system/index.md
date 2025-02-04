# Design an elevator system

### Requirements

For the elevator design problem, the requirements are defined below:

R1: There exist multiple elevator cars and floors in the building.

R2: The building can have a maximum of 15 floors and three elevators.

R3: The elevator car can move up or down or be in an idle state.




R4: The elevator door can only be opened when it is in an idle state.

R5: Every elevator car passes through each floor.

R6: The panel outside the elevator should have buttons to call an elevator car and to specify whether the passenger wants to go up or down.

R7: The panel inside the elevator should have buttons to go to every floor. There should be buttons to open or close the lift doors.




R8: There should be a display inside and outside the elevator car to show the current floor number and direction of the elevator car.

R9: The display inside the elevator should also show the capacity of the elevator car.

R10: Each floor has a separate panel and a display for each elevator car.




R11: Multiple passengers can go to the same or different floors in the same or opposite direction.

R12: The elevator system should be able to control the elevator car movement and the door functioning and monitor the elevator car.

R13: The elevator control system should be able to send the most appropriate elevator to the passenger when the passenger calls the elevator car.

R14: The elevator car can carry a maximum of eight persons or 680 kilograms at once.

### components of elevator system

- Button

    - ElevatorButton

    - HallButton

    - ElevatorButton & HallButton are inherited from Button class

    ```
        @abstract
        Button
        --
        - status: bool
        --
        + pressDown()
        + isPressed()

        @extends
        ElevatorButton
        - destinationFloorNumber: int

        @extends
        HallButton
        - buttonSign: Direction
        - sourceFloorNumber: int

    ```

- Elevator panel and hall panel

    - `ElevatorPanel`: class which is used to represent the complete grid of buttons

    ```
        ElevatorPanel
        - floorButton: ElevatorButton{list}
        - openButton: ElevatorButton
        - closeButton: ElevatorButton
    ```
    
    - `HallPanel`: class represents the buttons that are outside the elevator

    ```
        HallPanel
        - up: HallButton
        - down: HallButton
    ```

- Display
    
    - The display class consists of floor number, capacity and direction
    
    - Sepearate methods: `showHallDisplay()` and  `showElevatorDisplay()`

    ```
        Display
        --
        - floor: int
        - capacity: int
        - direction: Direction
        --
        + showElevatorDisplay()
        + showHallDisplay()
    ```

- Door: Door of an elevator
    
    ```
        - state: DoorState
        --
        + isOpen()
    ```

- ElevatorCar: is the class that expresses the elevators of the building.
    ```
        ElevatorCar
        --
        - id: int
        - door: Door
        - state: ElevatorState
        - currentFloor: int
        --
        + openDoor()
        + closeDoor()
        + move()
        + stop()
    ```

- Floor

    ```
        Floor
        --
        - displays: Display{list}
        - panels: HallPanel{list}
        --
        + isBottomMost(): bool
        + isTopMost(): bool
    ```

- ElevatorSystem

    ```
        ElevatorSystem
        --
        - building: Building
        --
        + monitoring
        + selectBestElevatorCar()
    ```