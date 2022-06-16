from Parser import *

class Map:
    def __init__(self, location: str):
        self.Location = location or ""
        self.IsMPQ = location and isMPQ(location)

        
        return
    def print(self):
        print(self.Location)
        print(self.IsMPQ)

if __name__ == "__main__":
    MAP = Map("Hello World.w3x")
    MAP.print()