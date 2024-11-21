# Design an elevator system

components of elevator system

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