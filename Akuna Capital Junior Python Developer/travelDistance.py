from math import acos, sin, cos, radians
from collections import defaultdict

RADIUS_MILES = 3963


class DestinationCalculator:
    def __init__(self):
        self.p1 = []
        self.p2 = []

    def process(self, line):
        line_list = line.split(":")
        if line_list[0] == "LOC":
            if not self.p1:
                self.p1 = list(map(float, line_list[2:]))
                return line_list[1]
            else:
                self.p2 = list(map(float, line_list[2:]))
                return line_list[1]
        else:
            delta_phi = abs(radians(self.p1[1]) - radians(self.p2[1]))
            numerator1 = sin(radians(self.p1[0])) * sin(radians(self.p2[0]))
            numerator2 = cos(radians(self.p1[0])) * cos(radians(self.p2[0])) * cos(delta_phi)
            numerator = acos(numerator1 + numerator2)
            dist = RADIUS_MILES * numerator
            line = line[5:]
            return line + ":" + str(dist).split(".")[0]
