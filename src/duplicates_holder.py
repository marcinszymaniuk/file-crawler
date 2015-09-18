class DuplicatesHolder:
    def __init__(self):
        self.duplicates = {}

    def add(self, path, duplicates):
        self.duplicates[path]=duplicates