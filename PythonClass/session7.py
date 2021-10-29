class Programminglang:
    def __init__(self, name, difficulty, level, timetolearn):
        self.name = name
        self.difficulty = difficulty
        self.level = level
        self.timetolearn = str(timetolearn)

    def info(self):
        return self.name + ' (' + self.difficulty + ') ' + self.level + ' level language' + ' needs at least ' + self.timetolearn + ' month(s) to learn'

    def __str__(self):
        return 'a programming language object made by sajjad kazemi'

    def __add__(self, other):
        return int(self.timetolearn) + int(other.timetolearn)


Go = Programminglang("Go", "hard", "low", 3)
Python = Programminglang("pythons", "EZ", "very high", 2)
print(Go.level); print(Python.level); print(Go.info); print(Python); print(Go); print(Python+Go);