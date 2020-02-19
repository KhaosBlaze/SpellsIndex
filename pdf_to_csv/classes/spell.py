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
        self.class = []

    def add_class(self, class):
        self.class.append(class)

    def get_class(self):
        """Return csv formated reply for imports"""
