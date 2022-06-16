import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from W3Buffer import W3Buffer

class Camera:
    def __init__(self):
        self.target = CameraInterface()
        self.offsetZ = 0
        self.rotation = 0
        self.aoa = 0 # angle of attack
        self.distance = 0
        self.roll = 0
        self.fov = 0
        self.farClipping = 0
        self.name = ""
        return

class CameraInterface:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        return

class CameraTrans:
    def __init__(self) -> None:
        return
    def warToJson(self, abs_filename: str) -> None:
        result = []
        
        buf = W3Buffer(abs_filename)
        collect = []

        fileVersion = 0 # offset 4
        numCameras = 0 # offset 4
        buf.readInt()
        for i, v in enumerate(buf.readStream()):
            if i == 0:
                fileVersion = int(v)
            elif i == 1:
                numCameras = int(v)
            else:
                break
        
        total_offset = 8
        for i in range(numCameras):
            camera = Camera()
            buf.readInt()
            for i, v in enumerate(buf.readStream()):
                
                camera.target.x = int(v)
if __name__ == "__main__":
    # url = "Translator/Hex.txt"
    # instance = W3Buffer(url)
    # instance.readInt()
    # for i in instance.readStream(url):
    #     print(i)