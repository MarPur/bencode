def encode(value_to_encode):
    """
    Bencodes python value to binary string

    :param value_to_encode: int, string, list or dict
    :return: Bencoded `value_to_encode`
    :raise: ValueError if the provided value cannot be encoded
    """

    try:
        return _encode_value(value_to_encode)
    except Exception as e:
        raise ValueError('Could not bencode the value')


def _encode_value(value_to_encode):
    encoded_string = None

    value_type = type(value_to_encode)

    if value_type is str or value_type is bytes:
        encoded_string = _encode_string(value_to_encode)
    elif value_type is int:
        encoded_string = _encode_int(value_to_encode)
    elif value_type is list:
        encoded_string = _encode_list(value_to_encode)
    elif value_type is dict:
        encoded_string = _encode_dict(value_to_encode)
    else:
        raise ValueError()
    return encoded_string


def _encode_string(str_to_encode):
    try:
        return (str(len(str_to_encode)) + ':' + str_to_encode).encode('ascii')
    except:
        return bytes(str(len(str_to_encode)) + ':', 'ascii') + str_to_encode


def _encode_int(int_to_encode):
    return ('i' + str(int_to_encode) + 'e').encode('ascii')


def _encode_list(list_to_encode):
    encoded_list = b'l'

    for item in list_to_encode:
        encoded_list += _encode_value(item)

    encoded_list += b'e'

    return encoded_list


def _encode_dict(dict_to_encode):
    keys = list(dict_to_encode.keys())

    for key in keys:
        if type(key) is not str:
            raise ValueError()

    keys.sort()

    encoded_dict = b'd'

    for key in keys:
        encoded_dict += _encode_string(key) + _encode_value(dict_to_encode[key])

    encoded_dict += b'e'

    return encoded_dict