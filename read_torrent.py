import pprint
from bencode import decode

f = open('/home/martynas/Downloads/ubuntu-15.10-desktop-amd64.iso.torrent', 'rb')
content = f.read(-1)
decoded = decode(content)

pprint.pprint(decoded)