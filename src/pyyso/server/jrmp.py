import socket
from threading import Thread


class JRMPListener():
    def __init__(self, serobj: bytes, ip: str = "0.0.0.0", port: int = 789):
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
            # 接受JRMP请求
            conn.recv(7)
            # 返回确认信息
            conn.send(b"\x4e\x00\x09\x6c\x6f\x63\x61\x6c\x68\x6f\x73\x74\x00\x00\xdd\xa6")
            # 接收客户端请求的一个字节
            conn.recv(1)
            # 再接收一个字节，这个字节标志了客户端请求报文剩下的长度
            len1 = conn.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len1 = ord(len1)
            # 接收剩下的请求报文
            conn.recv(len1 + 4)
            # 接收客户端请求的一个字节
            len2 = conn.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len2 = ord(len2)
            # 接收剩下的请求报文
            conn.recv(len2)
            # 接收451个字节，一般是定长信息，如果有需要可以设置成更小的值
            conn.recv(451)
            conn.send(self.serobj)

    def run(self):
        self.thread = Thread(target=self.__serve)
        self.thread.start()
