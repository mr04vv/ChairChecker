from src import Tag


class Chair:

    def __init__(self, id):
        self.id = id
        self.tags = []
        self.rssi = {}

    def findTagByChairId(self):
        return self.tags

    def addTag(self, tagId):
        if tagId not in self.tags:
            self.tags.append(tagId)
            Tag.Tag.add(tagId, self.id)

    def getId(self):
        return self.tags
