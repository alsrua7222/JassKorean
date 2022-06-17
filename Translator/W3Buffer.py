# from buffer import *

# war3 버퍼스트림 읽기 전용
class W3Buffer:
    def __init__(self, buffer) -> None:
        self._buffer = buffer
        self._type = 0 # 0 = char, 1 = short, 2 = int, float, 3 = string
        return
    
    def readStream(self) -> None:
        # 포인터 위치 바꾸는 방법 많다. - seek()를 써라. or 복잡하게 구현해라.
        buffer = bytearray()
        with open(self._buffer, "rb") as f:
            cache = -1
            while True:
                # string 이면 계속 1씩 받다가 \0이 나오면 멈춤
                data = bytes()
                if cache != self._type:
                    offset = self.getOffset()

                if self._type == 3:
                    while True:
                        buf = f.read(offset)
                        if not buf or buf == b'\0':
                            break
                        data += buf
                else:
                    data = f.read(offset)
                
                if not data:
                    break
                
                buffer.extend(data)
                if buffer:
                    yield buffer.decode()
                    buffer.clear()
        return

    def getOffset(self) -> int:
        if self._type in [0, 3]:
            return 1
        elif self._type == 1:
            return 2
        elif self._type == 2:
            return 4
        return 8

    def readInt(self) -> None:
        self._type = 4
        return

    def readShort(self) -> None:
        self._type = 2
        return 
    
    def readFloat(self) -> None:
        self._type = 4
        return
    
    def readString(self) -> None:
        self._type = 1
        return


if __name__ == "__main__":
    url = "Translator/Hex.txt"
    instance = W3Buffer(url)
    instance.readInt()
    for i in instance.readStream():
        print(i)
