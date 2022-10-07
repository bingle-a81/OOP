class Box:
    def __init__(self):
        self.boxes=[]

    def add_thing(self, obj):
        self.boxes.append(obj)

    def get_things(self):
        return self.boxes

class Thing:
    def __init__(self):