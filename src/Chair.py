from src import Tag


class Chair:
    chair_list = []
    chairs = []

    def __init__(self, id):
        self.id = id
        self.tags = []
        self.rssi = []
        self.rssi2 = []
        self.rssiFromAntenna = {}
        self.rssi2FromAntenna = {}
        Chair.chair_list.append(id)
        Chair.chairs.append(self)

    def findTagByChairId(self):
        return self.tags

    def addTag(self, tagId):
        # print(Tag.Tag.tag_chair_relation)
        if tagId not in self.tags:
            res = Tag.Tag.add(tagId, self.id)
            if res:
                self.tags.append(tagId)
                Tag.Tag.add(tagId, self.id)
            return res

    def getId(self):
        return self.tags

    def deleteTag(self, tagId):
        if tagId in self.tags:
            # print(str(Tag.Tag.tag_chair_relation))
            self.tags.remove(tagId)
            # print("koko")
            # Tag.Tag.deleteTagRelation(tagId)

    def deleteTagAll(self):
        self.tags.clear()

    def deleteChair(self):
        for i in self.tags:
            Tag.Tag.deleteTagRelationAll(i)
        Chair.chair_list.remove(self.id)
        Chair.chairs.remove(self)
        self.deleteTagAll()
        del self
