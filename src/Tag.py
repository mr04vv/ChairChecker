from src import Chair


class Tag:
    tag_chair_relation = {}

    @staticmethod
    def add(tag_id, chair_id):
        if tag_id not in Tag.tag_chair_relation:
            Tag.tag_chair_relation.update({tag_id: chair_id})
            return True
        else:
            return False

    @staticmethod
    def getChairId(tag_id):
        if tag_id in Tag.tag_chair_relation:
            return Tag.tag_chair_relation[tag_id]
        else:
            return None

    @staticmethod
    def getTagRelation():
        return Tag.tag_chair_relation

    @staticmethod
    def deleteTagRelation(tagId):
        if tagId in Tag.tag_chair_relation:
            chair_id = Tag.getChairId(tagId)
            Tag.tag_chair_relation.pop(tagId)
            for chair in Chair.Chair.chairs:
                if chair.id == chair_id:
                    print(Tag.tag_chair_relation)
                    chair.deleteTag(tagId)

    @staticmethod
    def deleteTagRelationAll(tagId):
        if tagId in Tag.tag_chair_relation:
            chair_id = Tag.getChairId(tagId)
            Tag.tag_chair_relation.pop(tagId)
            for chair in Chair.Chair.chairs:
                if chair.id == chair_id:
                    print(Tag.tag_chair_relation)
        # print(Tag.tag_chair_relation)
            # Chair.Chair.chairs[chair_id-1].deleteTag(tagId)
