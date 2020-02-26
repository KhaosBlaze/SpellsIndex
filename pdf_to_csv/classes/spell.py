class Spell:
    """Spell class for creating the large index to go into go to csv"""
    def __init__(self):
        self.name = None
        self.level = None
        self.school = None
        self.casting_time =  None
        self.range = None
        self.components = None
        self.Duration = None
        self.Description = None
        self.classes = []

    def __str__(self):
        printer =  "Name: " + self.name + "\n"
        printer+=  "Level: " + self.level + "\n"
        printer+=  "School: " + self.school + "\n"
        printer+=  "Casing Time: " + self.casting_time + "\n"
        printer+=  "Range: " + self.range + "\n"
        return printer

    def add_class(self, newClass):
        self.classes.append(newClass)

    def get_class(self):
        """Return csv formated reply for imports"""
        pass
