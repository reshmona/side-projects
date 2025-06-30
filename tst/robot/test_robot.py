from src.robot.robot import Robot
from src.robot.robot_manager import RobotManager
from io import StringIO
import sys
import unittest

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_initial_position(self):
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_turn_left(self):
        self.robot.turn_left()
        self.assertEqual(self.robot.report(), "0,0,WEST")
        self.robot.turn_left()
        self.assertEqual(self.robot.report(), "0,0,SOUTH")

    def test_turn_right(self):
        self.robot.turn_right()
        self.assertEqual(self.robot.report(), "0,0,EAST")
        self.robot.turn_right()
        self.assertEqual(self.robot.report(), "0,0,SOUTH")

    def test_move_north(self):
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_move_east(self):
        self.robot.turn_right()
        self.robot.move()
        self.assertEqual(self.robot.report(), "1,0,EAST")

    def test_move_south(self):
        self.robot.turn_right()
        self.robot.turn_right()
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,-1,SOUTH")

    def test_move_west(self):
        self.robot.turn_left()
        self.robot.move()
        self.assertEqual(self.robot.report(), "-1,0,WEST")

    def test_sequence(self):
        self.robot.move()
        self.robot.turn_right()
        self.robot.move()
        self.robot.turn_left()
        self.robot.move()
        self.assertEqual(self.robot.report(), "1,2,NORTH")

    def test_multiple_robots(self):
        r1 = Robot()
        r2 = Robot()
        r2.turn_right()
        r2.move()
        self.assertEqual(r1.report(), "0,0,NORTH")
        self.assertEqual(r2.report(), "1,0,EAST")
        r1.move()
        r2.move()
        self.assertEqual(r1.report(), "0,1,NORTH")
        self.assertEqual(r2.report(), "2,0,EAST")

class TestRobotManager(unittest.TestCase):
    def setUp(self):
        self.manager = RobotManager()

    def test_new_and_switch(self):
        self.manager.execute_command("NEW", [])
        self.assertEqual(len(self.manager.robots), 1)
        self.manager.execute_command("NEW", [])
        self.assertEqual(len(self.manager.robots), 2)
        self.manager.execute_command("SWITCH", ["0"])
        self.assertEqual(self.manager.current_robot, 0)
        self.manager.execute_command("SWITCH", ["1"])
        self.assertEqual(self.manager.current_robot, 1)

    def test_move_and_report(self):
        self.manager.execute_command("NEW", [])
        self.manager.execute_command("MOVE", [])
        output = StringIO()
        sys.stdout = output
        self.manager.execute_command("REPORT", [])
        sys.stdout = sys.__stdout__
        self.assertIn("0,1,NORTH", output.getvalue())

    def test_list_robots(self):
        self.manager.execute_command("NEW", [])
        self.manager.execute_command("NEW", [])
        output = StringIO()
        sys.stdout = output
        self.manager.execute_command("LIST", [])
        sys.stdout = sys.__stdout__
        self.assertIn("Robot #0", output.getvalue())
        self.assertIn("Robot #1", output.getvalue())

    def test_invalid_switch(self):
        self.manager.execute_command("NEW", [])
        output = StringIO()
        sys.stdout = output
        self.manager.execute_command("SWITCH", ["5"])
        sys.stdout = sys.__stdout__
        self.assertIn("Invalid robot number", output.getvalue())

    def test_no_robot_selected(self):
        output = StringIO()
        sys.stdout = output
        self.manager.execute_command("MOVE", [])
        sys.stdout = sys.__stdout__
        self.assertIn("No robot selected", output.getvalue())

if __name__ == "__main__":
    unittest.main()
