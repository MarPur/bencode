from bencode import encode

encoded_text = encode({
    'a': 'Some text',
    'c': 1000000,
    'd': ['a', 'b', 'c'],
    'binary': b'abcded456456'
})

print(encoded_text)