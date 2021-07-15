from fleet import Robot

class Fleet:
    def __init__(self):
        self.robot_fleet = []
        
    def create_fleet(self):
        robot_one = Robot("Hank")
        self.robot_fleet.append(robot_one)
        robot_two = Robot("Frank")
        self.robot_fleet.append(robot_two)
        robot_three = Robot("Mark")
        self.robot_fleet.append(robot_three)


