def is_valid_socket_address(address):
    """Determine if the provided string is a valid socket address.

    Args:
        address: A string with a socket address, eg, 
            '127.12.23.43:5000', to be checked for validity.
    Returns:
        A boolean indicating whether the provided string is a valid 
        socket address.
    """
    try:
        ints, port = address.split(':')
        ints = [int(n) for n in ints.split('.')]
    except ValueError:
        return False
    if len(ints) != 4:
        return False
    for n in ints:
        if n < 0 or n > 250:
            return False
    if int(port) < 1 or int(port) > 65535:
        return False
    return True


if __name__ == '__main__':
    for address in ["127.12.23.43:5000",
                   "127.A:-12"]:
        print is_valid_socket_address(address)
