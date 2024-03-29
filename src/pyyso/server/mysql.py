import socket
from threading import Thread


class MysqlServer():
    def __init__(self, serobj: bytes, ip: str = "0.0.0.0", port: int = 3307):
        self.serobj = serobj
        self.ip = ip
        self.port = port

    def __serve(self):
        s = socket.socket()
        s.bind((self.ip, self.port))
        s.listen(5)
        while True:
            # 接受客户端
            conn, addr = s.accept()
            conn.send(b"\x4a\x00\x00\x00\x0a\x38\x2e\x30\x2e\x32\x33\x00\x16\x00\x00\x00" \
                      + b"\x49\x6d\x28\x32\x4e\x76\x36\x02\x00\xff\xff\xff\x02\x00\xff\xcf" \
                      + b"\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x32\x37\x43\x17\x4d" \
                      + b"\x01\x63\x39\x1b\x23\x0a\x44\x00\x63\x61\x63\x68\x69\x6e\x67\x5f" \
                      + b"\x73\x68\x61\x32\x5f\x70\x61\x73\x73\x77\x6f\x72\x64\x00")
            len1 = conn.recv(3)
            len1 = int.from_bytes(len1, byteorder="little")
            conn.recv(len1 + 1)
            conn.send(b"\x07\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00")
            len3 = conn.recv(3)
            len3 = int.from_bytes(len3, byteorder="little")
            conn.recv(len3 + 1)
            conn.send(b"\x01\x00\x00\x01\x11\x2e\x00\x00" \
                      + b"\x02\x03\x64\x65\x66\x00\x00\x00\x18\x61\x75\x74\x6f\x5f\x69\x6e" \
                      + b"\x63\x72\x65\x6d\x65\x6e\x74\x5f\x69\x6e\x63\x72\x65\x6d\x65\x6e" \
                      + b"\x74\x00\x0c\x3f\x00\x15\x00\x00\x00\x08\xa0\x00\x00\x00\x00\x2a" \
                      + b"\x00\x00\x03\x03\x64\x65\x66\x00\x00\x00\x14\x63\x68\x61\x72\x61" \
                      + b"\x63\x74\x65\x72\x5f\x73\x65\x74\x5f\x63\x6c\x69\x65\x6e\x74\x00" \
                      + b"\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x2e\x00\x00" \
                      + b"\x04\x03\x64\x65\x66\x00\x00\x00\x18\x63\x68\x61\x72\x61\x63\x74" \
                      + b"\x65\x72\x5f\x73\x65\x74\x5f\x63\x6f\x6e\x6e\x65\x63\x74\x69\x6f" \
                      + b"\x6e\x00\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x2b" \
                      + b"\x00\x00\x05\x03\x64\x65\x66\x00\x00\x00\x15\x63\x68\x61\x72\x61" \
                      + b"\x63\x74\x65\x72\x5f\x73\x65\x74\x5f\x72\x65\x73\x75\x6c\x74\x73" \
                      + b"\x00\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x2a\x00" \
                      + b"\x00\x06\x03\x64\x65\x66\x00\x00\x00\x14\x63\x68\x61\x72\x61\x63" \
                      + b"\x74\x65\x72\x5f\x73\x65\x74\x5f\x73\x65\x72\x76\x65\x72\x00\x0c" \
                      + b"\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x26\x00\x00\x07" \
                      + b"\x03\x64\x65\x66\x00\x00\x00\x10\x63\x6f\x6c\x6c\x61\x74\x69\x6f" \
                      + b"\x6e\x5f\x73\x65\x72\x76\x65\x72\x00\x0c\x21\x00\xff\xff\x00\x00" \
                      + b"\xfd\x00\x00\x1f\x00\x00\x22\x00\x00\x08\x03\x64\x65\x66\x00\x00" \
                      + b"\x00\x0c\x69\x6e\x69\x74\x5f\x63\x6f\x6e\x6e\x65\x63\x74\x00\x0c" \
                      + b"\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x29\x00\x00\x09" \
                      + b"\x03\x64\x65\x66\x00\x00\x00\x13\x69\x6e\x74\x65\x72\x61\x63\x74" \
                      + b"\x69\x76\x65\x5f\x74\x69\x6d\x65\x6f\x75\x74\x00\x0c\x3f\x00\x15" \
                      + b"\x00\x00\x00\x08\xa0\x00\x00\x00\x00\x1d\x00\x00\x0a\x03\x64\x65" \
                      + b"\x66\x00\x00\x00\x07\x6c\x69\x63\x65\x6e\x73\x65\x00\x0c\x21\x00" \
                      + b"\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x2c\x00\x00\x0b\x03\x64" \
                      + b"\x65\x66\x00\x00\x00\x16\x6c\x6f\x77\x65\x72\x5f\x63\x61\x73\x65" \
                      + b"\x5f\x74\x61\x62\x6c\x65\x5f\x6e\x61\x6d\x65\x73\x00\x0c\x3f\x00" \
                      + b"\x15\x00\x00\x00\x08\xa0\x00\x00\x00\x00\x28\x00\x00\x0c\x03\x64" \
                      + b"\x65\x66\x00\x00\x00\x12\x6d\x61\x78\x5f\x61\x6c\x6c\x6f\x77\x65" \
                      + b"\x64\x5f\x70\x61\x63\x6b\x65\x74\x00\x0c\x3f\x00\x15\x00\x00\x00" \
                      + b"\x08\xa0\x00\x00\x00\x00\x27\x00\x00\x0d\x03\x64\x65\x66\x00\x00" \
                      + b"\x00\x11\x6e\x65\x74\x5f\x77\x72\x69\x74\x65\x5f\x74\x69\x6d\x65" \
                      + b"\x6f\x75\x74\x00\x0c\x3f\x00\x15\x00\x00\x00\x08\xa0\x00\x00\x00" \
                      + b"\x00\x1e\x00\x00\x0e\x03\x64\x65\x66\x00\x00\x00\x08\x73\x71\x6c" \
                      + b"\x5f\x6d\x6f\x64\x65\x00\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00" \
                      + b"\x1f\x00\x00\x26\x00\x00\x0f\x03\x64\x65\x66\x00\x00\x00\x10\x73" \
                      + b"\x79\x73\x74\x65\x6d\x5f\x74\x69\x6d\x65\x5f\x7a\x6f\x6e\x65\x00" \
                      + b"\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x1f\x00\x00" \
                      + b"\x10\x03\x64\x65\x66\x00\x00\x00\x09\x74\x69\x6d\x65\x5f\x7a\x6f" \
                      + b"\x6e\x65\x00\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00" \
                      + b"\x2b\x00\x00\x11\x03\x64\x65\x66\x00\x00\x00\x15\x74\x72\x61\x6e" \
                      + b"\x73\x61\x63\x74\x69\x6f\x6e\x5f\x69\x73\x6f\x6c\x61\x74\x69\x6f" \
                      + b"\x6e\x00\x0c\x21\x00\xff\xff\x00\x00\xfd\x00\x00\x1f\x00\x00\x22" \
                      + b"\x00\x00\x12\x03\x64\x65\x66\x00\x00\x00\x0c\x77\x61\x69\x74\x5f" \
                      + b"\x74\x69\x6d\x65\x6f\x75\x74\x00\x0c\x3f\x00\x15\x00\x00\x00\x08" \
                      + b"\xa0\x00\x00\x00\x00\xdc\x00\x00\x13\x01\x31\x04\x75\x74\x66\x38" \
                      + b"\x04\x75\x74\x66\x38\x04\x75\x74\x66\x38\x07\x75\x74\x66\x38\x6d" \
                      + b"\x62\x34\x12\x75\x74\x66\x38\x6d\x62\x34\x5f\x30\x39\x30\x30\x5f" \
                      + b"\x61\x69\x5f\x63\x69\x00\x05\x32\x38\x38\x30\x30\x03\x47\x50\x4c" \
                      + b"\x01\x32\x08\x36\x37\x31\x30\x38\x38\x36\x34\x02\x36\x30\x75\x4f" \
                      + b"\x4e\x4c\x59\x5f\x46\x55\x4c\x4c\x5f\x47\x52\x4f\x55\x50\x5f\x42" \
                      + b"\x59\x2c\x53\x54\x52\x49\x43\x54\x5f\x54\x52\x41\x4e\x53\x5f\x54" \
                      + b"\x41\x42\x4c\x45\x53\x2c\x4e\x4f\x5f\x5a\x45\x52\x4f\x5f\x49\x4e" \
                      + b"\x5f\x44\x41\x54\x45\x2c\x4e\x4f\x5f\x5a\x45\x52\x4f\x5f\x44\x41" \
                      + b"\x54\x45\x2c\x45\x52\x52\x4f\x52\x5f\x46\x4f\x52\x5f\x44\x49\x56" \
                      + b"\x49\x53\x49\x4f\x4e\x5f\x42\x59\x5f\x5a\x45\x52\x4f\x2c\x4e\x4f" \
                      + b"\x5f\x45\x4e\x47\x49\x4e\x45\x5f\x53\x55\x42\x53\x54\x49\x54\x55" \
                      + b"\x54\x49\x4f\x4e\x03\x43\x53\x54\x06\x53\x59\x53\x54\x45\x4d\x0f" \
                      + b"\x52\x45\x50\x45\x41\x54\x41\x42\x4c\x45\x2d\x52\x45\x41\x44\x05" \
                      + b"\x32\x38\x38\x30\x30\x07\x00\x00\x14\xfe\x00\x00\x02\x00\x00\x00")
            while True:
                len4 = conn.recv(3)
                len4 = int.from_bytes(len4, byteorder="little")
                req = conn.recv(len4 + 1)
                print(str(req[2:]))
                if req[2:] == b"SHOW SESSION STATUS":
                    p1 = b"\x01\x00\x00\x01\x02"
                    p2 = b"\x30\x00\x00\x02\x03\x64\x65\x66\x0a\x6a\x64\x62\x63\x61\x74\x74" \
                         + b"\x61\x63\x6b\x06\x61\x74\x74\x61\x63\x6b\x06\x61\x74\x74\x61\x63" \
                         + b"\x6b\x02\x73\x31\x02\x73\x31\x0c\x3f\x00\xff\xff\x00\x00\xfc\x90" \
                         + b"\x00\x00\x00\x00"
                    p3 = b"\x30\x00\x00\x03\x03\x64\x65\x66\x0a\x6a\x64\x62\x63\x61\x74\x74" \
                         + b"\x61\x63\x6b\x06\x61\x74\x74\x61\x63\x6b\x06\x61\x74\x74\x61\x63" \
                         + b"\x6b\x02\x73\x32\x02\x73\x32\x0c\xff\x00\xfc\x03\x00\x00\xfd\x00" \
                         + b"\x00\x00\x00\x00"
                    len7 = len(self.serobj + b"\x04\x65\x76\x69\x6c")
                    p4 = (len7 + 3).to_bytes(3, byteorder="little") + b"\x04\xfc" + (len7).to_bytes(2,
                                                                                                    byteorder="little") + self.serobj + b"\x04\x65\x76\x69\x6c"
                    p5 = b"\x07\x00\x00\x05\xfe\x00\x00\x02\x00\x00\x00"
                    conn.send(p1 + p2 + p3 + p4 + p5)
                else:
                    conn.send(b"\x07\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00")

    def run(self):
        """
        使用这个启动服务器
        """
        self.thread = Thread(target=self.__serve)
        self.thread.start()