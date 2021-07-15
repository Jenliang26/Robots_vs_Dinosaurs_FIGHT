from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        
    def create_fleet(self):
        robot_one = Robot("Hank")
        self.robots.append(robot_one)
        robot_two = Robot("Frank")
        self.robots.append(robot_two)
        robot_three = Robot("Mark")
        self.robots.append(robot_three)


