class DataStructure(object):
    def __init__(self):
        self.name2id = {}
        self.id2item = {}

    def add_item(self, item_name, item_id, item):
        self.name2id[item_name] = item_id
        self.id2item[item_id] = item

    def search_by_name(self, target_name):
        target_id = self.name2id[target_name]
        target_item = self.id2item[target_id]
        return target_item

    def search_by_id(self, target_id):
        target_item = self.id2item[target_id]
        return target_item
