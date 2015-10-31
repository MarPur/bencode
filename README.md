# bencode
Encodes / Decodes bencoded content.

[Bencode](https://en.wikipedia.org/wiki/Bencode) is an encoding format used by Bittorrent to encode .torrent files with information about the tracker and the contents to be downloaded.

This library provides functions to read such information as well as write it.

# Usage

An example of how to read contents from .torrent file is provided in read_torrent.py.

# Running the unit tests

Navigate to the module and run
```
python3 -m unittest tests
```
