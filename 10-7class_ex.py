class Robot:
    """Represents a robot, with a name."""
    population = 0 # A class variable, counting the number of robots
    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))
        # When this person is created, the robot adds to the population
        self.__class__.population += 1 # 因为每个对象都通过self.__class__属性引用其类,所有可用该句代替Robot.population += 1
    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))
    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))
    @classmethod # 意思同 how_many = classmethod(how_many) 标记为类方法
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

aa = Robot('aa')
bb = Robot('bb')
aa.say_hi()
aa.how_many()

