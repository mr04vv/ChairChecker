class Tag:
    tag_chair_relation = {}

    @staticmethod
    def add(tag_id, chair_id):
        Tag.tag_chair_relation.update({tag_id: chair_id})

    @staticmethod
    def getChairId(tag_id):
        return Tag.tag_chair_relation[tag_id]

    @staticmethod
    def getTagRelation():
        return Tag.tag_chair_relation
