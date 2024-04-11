# Elevator
# Assuming we are just looking at 1 elevator in a single elevator shaft.
# Elevator has interface with buttons.
#   - Number buttons for each floor
#   - "Open door" and "close door" buttons.
#   - Emergency button and/or phone for emergencies.

# Functionality:
#   - Elevator can receive instructions from button presses both inside AND outside of the elevator. These will be queued, presumably just arranged FIFO.
#   - Some special logic for which direction elevator does next -> if we're moving up, we'll do every "Up" action for

# class Elevator:
    # def __init__(self, curFloor=0):
        # curFloor: Int
        # Direction: None # None, Up, Down -> Determines if the elevator is moving up/down, or is stationary (None)
        # floors: List[Int] -> List of all floors that elevator can go to.
        # curInputs = {upInputs: [], downInputs: []} -> Contains all "button press" inputs to the elevator. Must have logic to determine where a new "button press" will be placed in curInputs.
        #   - If we're already going up, then a new "up" button press will occur before any "down" commands.
        #   - Button presses inside and outside of elevator do the same thing! They are added to the queue in similar fashion.

    # Methods:

        # closeDoor -> Close door, IF we're not moving. Do nothing if door is already closed.
        # openDoor -> Open door, IF we're not moving.  If door is already open, add another x seconds to the "door open" command that we're still on.

        # pressFloorButton(floorNum) -> Takes an input for a floor selection. Uses logic to decide where to place this in instructions.
        #   - If NOT moving -> simple, add this instruction to the list (as the first and only item for now).
        #   - If elevator is moving -> Add this instruction to the list. Execute FIRST if it comes between current floor and the next floor we are scheduled to visit.

        # General logic for button press:
        #   - If first command, start executing the command and add it to the queue of inputs.
        #   - If NOT first command, add the command the the queue of inputs.

        # Logic for ordering queue:
        #   - If we're moving up AND we press a new button:
        #       1) If button is current floor, stop at this floor and open the doors.
        #       2) If button is above current floor, we add this to the "up" part of the queue (all actions moving upward). Sort this part of the queue (or use a heap).
        #       3) If button is below current floor, we add this to the "down" part of the queue. It will be sorted to illustrate the queue of instructions once we start moving "down".

        # General Logic: When we reach a floor, openDoor.
        # When someone presses "up" or "down" outside the elevator, that floor is added to the current queue. When we reach that floor, we make the direction "up" if it isn't already.