class Elevator(object):
    def __init__(self):
        self.cf = 0  # current floor
        self.dirc = "NULL"
        self.req = dequeu([])
        self.reqSet = set([])

    def in_cmg_req(self, floor):
        self.req.append(floor)
        self.reqSet.add(floor)

    def process(self):
        self.req = sorted(self.req)

        while self.req:
            goal_floor = self.req.popleft()
            if goal_floor not in self.reqSet:
                continue

            self.get_direction(cf, gf)
            self.go_to_dest(cf, goal_floor)

    def get_direction(self, cf, gf):
        if cf > goal_floor:
            self.dirc = "DOWN"
        else:
            self.dirc = "UP"

    def go_to_dest(self, cf, goal_floor):
        while cf != goal_floor:
            if cf in self.reqSet:
                self.reqSet.remove(cf)
                self.openDoors()
                self.closeDoors()

            if self.dirc == "DOWN":
                cf -= 1
            else:
                cf += 1

        else:
            self.reqSet.remove(cf)
            self.openDoors()
            self.closeDoors()
            self.dirc = "NULL"

    def openDoors(self):
        pass

    def closeDoors(self):
        pass
