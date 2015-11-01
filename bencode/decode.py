from collections import namedtuple

ReturnValue = namedtuple('ReturnValue', ['value', 'chars_decoded'])

def decode(value_to_decode):
    """Decodes bencoded bytes to python value

    :param value_to_decode:
    :return: str, int`
    :raise: ValueError if the provided value cannot be decoded
    """
    try:
        return _decode(value_to_decode).value
    except:
        raise ValueError('bytes could not be decoded')


def _decode(string_to_decode):
    try:
        int(string_to_decode[0:string_to_decode.find(b':')])
        is_string = True
    except:
        is_string = False

    first_char = chr(string_to_decode[0])

    if first_char  == 'i':
        return _decode_int(string_to_decode)
    elif first_char == 'l':
        return _decode_list(string_to_decode)
    elif first_char == 'd':
        return _decode_dict(string_to_decode)
    elif is_string:
        return _decode_string(string_to_decode)
    else:
        raise ValueError('bytes could not be decoded')


def _decode_int(int_to_decode):
    encoded_int = int_to_decode.split(b'e')[0][1:]

    return ReturnValue(
        value=int(encoded_int),
        chars_decoded=len(encoded_int) + 2
    )


def _decode_string(string_to_decode):
    string_length = int(string_to_decode.split(b':')[0])

    bytes_decoded = string_to_decode[len(str(string_length)) + 1:(len(str(string_length)) + 1) + string_length]

    try:
        bytes_decoded = bytes_decoded.decode('utf-8')
    except:
        pass

    return ReturnValue(
        value=bytes_decoded,
        chars_decoded=len(str(string_length)) + 1 + string_length
    )


def _decode_dict(string_to_decode):
    decoded_dict = {}

    index = 1

    while chr(string_to_decode[index]) != 'e':
        key_return_value = _decode_string(string_to_decode[index:])
        value_return_value = _decode(string_to_decode[index + key_return_value.chars_decoded:])

        decoded_dict[key_return_value.value] = value_return_value.value

        index += key_return_value.chars_decoded + value_return_value.chars_decoded

    return ReturnValue(
        value=decoded_dict,
        chars_decoded=index + 1
    )


def _decode_list(list_to_decode):
    decoded_list = []
    chars_decoded = 0

    index = 1

    while chr(list_to_decode[index]) != 'e':
        current_part = list_to_decode[index:]

        decode_result = _decode(current_part)

        decoded_list.append(decode_result.value)
        index += decode_result.chars_decoded

    return ReturnValue(
        value=decoded_list,
        chars_decoded=index + 1
    )
