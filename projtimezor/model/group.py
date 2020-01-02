class Group:

    def __init__(self, data):
        self.uuid = data['uuid']
        self.name = data['name']
        self.affinity = data['affinity']

    @property
    def properties(self):
        return self.__dict__