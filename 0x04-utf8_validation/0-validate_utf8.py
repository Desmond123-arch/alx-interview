#!/usr/bin/python3
"""Contains the utf8 function """


def validUTF8(data) -> bool:
    """ A validate uft8 """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask all but the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & mask1) and (byte & mask2) == 0:
                num_bytes = 1  # 2-byte character
            elif (byte & mask1) and (byte & mask2):
                num_bytes = 2  # 3-byte character
            elif (byte & mask1) and (byte & mask2) and (byte & (1 << 5)):
                num_bytes = 3  # 4-byte character
            else:
                return False

        else:
            # Check if this byte is a continuation byte
            if not (byte & mask1) or (byte & mask2):
                return False

        num_bytes -= 1

    return num_bytes == 0
