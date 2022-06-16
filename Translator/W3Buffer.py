# from buffer import *

# war3 버퍼스트림 읽기 전용
class W3Buffer:
    def __init__(self, buffer) -> None:
        self._buffer = buffer
        self._offset = 0
        return
    
    def readStream(self) -> None:
        buffer = bytearray()
        with open(self._buffer, "rb") as f:
            while True:
                data = f.read(self._offset)
                if not data:
                    break
                buffer.extend(data)
                if buffer:
                    yield buffer.decode()
                    buffer.clear()
        return

    def readInt(self) -> None:
        self._offset = 4
        return

    def readShort(self) -> None:
        self._offset = 2
        return 
    
    def readFloat(self) -> None:
        self._offset = 4
        return
    
    def readString(self) -> None:
        self._offset = 1
        return


if __name__ == "__main__":
    # a = "Hello world".encode()
    # b = memoryview(a)
    # print(a)
    url = "Translator/Hex.txt"
    # with open("Translator/Hex.txt", "rb") as f:
    #     tmp = f.read()
    # data = bytearray(tmp)
    # print(memoryview(data))
    instance = W3Buffer(url)
    instance.readInt()
    for i in instance.readStream():
        print(i)
