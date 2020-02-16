class Group:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.affinity = data['affinity']
        self.filename = data['filename']

    @property
    def properties(self):
        return self.__dict__