import socket
from threading import Thread
from pyyso.misc.ReferenceWrapper_Stub import *
from pyyso.misc.Lease import *


class RMIServer():

    def __init__(self, serobj: bytes, ip: str = "0.0.0.0", port: int = 1099, refip: str = "0.0.0.0",
                 refport: int = 51510):
        self.serobj = serobj
        self.ip = ip
        self.port = port
        self.refip = refip
        self.refport = refport

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
            # 接收调用报文
            conn.recv(43)
            # 接收客户端请求的一个字节
            len2 = conn.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len2 = ord(len2)
            # 接收剩下的请求报文
            conn.recv(len2)
            # 返回Refernce_Wrapper_Stub
            conn.send(RefeneceWrapper_Stub(self.refip, self.refport))
            # 回到registry这里，接收一个字节的JRMI Ping
            conn.recv(1)
            # 发送一个字节的JRMI PingAck
            conn.send(b"\x53")
            # 接收一个字节的JRMI DgcAck
            conn.recv(1)
            # 关闭链接
            conn.close()

    def __serve2(self):
        # 新建一个socket
        s2 = socket.socket()
        s2.bind((self.refip, self.refport))
        s2.listen(5)
        while True:
            conn2, addr2 = s2.accept()
            # 接收JRMP请求
            conn2.recv(7)
            # 返回确认信息
            conn2.send(b"\x4e\x00\x09\x6c\x6f\x63\x61\x6c\x68\x6f\x73\x74\x00\x00\xdd\xa6")
            # 接收客户端请求的一个字节
            conn2.recv(1)
            # 再接收一个字节，这个字节标志了客户端请求报文剩下的长度
            len1 = conn2.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len1 = ord(len1)
            # 接收剩下的请求报文
            conn2.recv(len1 + 4)
            # 接收451个字节，一般是定长信息，如果有需要可以设置成更小的值
            conn2.recv(451)
            # 发送信息
            conn2.send(Lease())
            # 接收41个字节的数据
            conn2.recv(41)
            # 发送数据
            conn2.send(self.serobj)
            # 关闭链接
            conn2.close()

    def run(self):
        self.thread1 = Thread(target=self.__serve)
        self.thread1.start()
        self.thread2 = Thread(target=self.__serve2)
        self.thread2.start()
