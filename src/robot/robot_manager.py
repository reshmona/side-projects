# command line program for moving a robot on a 2D surface
# commands are: LEFT, RIGHT, MOVE, REPORT
import sys
from src.robot.robot import Robot

class RobotManager:
    def __init__(self):
        self.robots = []
        self.current_robot = None

    def new_robot(self):
        self.robots.append(Robot())
        self.current_robot = len(self.robots) - 1
        print(f"Created robot #{self.current_robot}")

    def switch_robot(self, idx):
        if 0 <= idx < len(self.robots):
            self.current_robot = idx
            print(f"Switched to robot #{self.current_robot}")
        else:
            print("Invalid robot number.")

    def list_robots(self):
        for i, r in enumerate(self.robots):
            tag = "*" if i == self.current_robot else " "
            print(f"{tag} Robot #{i}: {r.report()}")

    def execute_command(self, cmd, args):
        if cmd == "NEW":
            self.new_robot()
        elif cmd == "SWITCH":
            if not args or not args[0].isdigit():
                print("Usage: SWITCH <robot_number>")
            else:
                self.switch_robot(int(args[0]))
        elif cmd == "LIST":
            self.list_robots()
        elif self.current_robot is None:
            print("No robot selected. Use NEW to create one.")
        elif cmd == "LEFT":
            self.robots[self.current_robot].turn_left()
        elif cmd == "RIGHT":
            self.robots[self.current_robot].turn_right()
        elif cmd == "MOVE":
            self.robots[self.current_robot].move()
        elif cmd == "REPORT":
            print(self.robots[self.current_robot].report())
        else:
            print("Invalid command. Please try again.")

def main():
    print("Commands: NEW, SWITCH <n>, LEFT, RIGHT, MOVE, REPORT, LIST, EXIT")
    manager = RobotManager()
    while True:
        command = input("Enter command: ").strip()
        if not command:
            continue
        parts = command.split()
        cmd = parts[0].upper()
        args = parts[1:]
        if cmd == "EXIT":
            print("Exiting the program.")
            break
        manager.execute_command(cmd, args)
