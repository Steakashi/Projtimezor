class Group:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.priority = data['priority']
        self.filename = data['filename']

    @property
    def properties(self):
        return self.__dict__