#!/usr/bin/env python3
"""
Base85 encoder and decoder
"""

from __future__ import annotations
from beartype import beartype

CHARSET = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
CHAR_MAP = {char: idx for idx, char in enumerate(CHARSET)}


@beartype
def encode(data: bytes) -> bytes:
    """
    Base85 encoder implemented from scratch
    """
    output_buf = []
    for i in range(0, len(data), 4):
        block = data[i:i + 4]

        padded_block = block.ljust(4, b'\x00')

        value = int.from_bytes(padded_block, byteorder='big')

        encoded_block = []
        for _ in range(5):
            encoded_block.append(CHARSET[value % 85])
            value //= 85

        encoded_block.reverse()

        valid_chars = len(block) + 1
        output_buf.extend(encoded_block[:valid_chars])

    return bytes(output_buf)


@beartype
def decode(data: bytes) -> bytes:
    """
    Base85 decoder implemented from scratch
    """
    output_buf = []
    for i in range(0, len(data), 5):
        block = data[i:i + 5]

        padded_block = block.ljust(5, CHARSET[-1:])

        value = 0
        try:
            for char in padded_block:
                value = value * 85 + CHAR_MAP[char]
        except KeyError:
            raise ValueError(f"Invalid Base85 character in chunk starting at byte {i}")

        try:
            raw_block = value.to_bytes(4, byteorder='big')
        except OverflowError:
            raise ValueError(f"Base85 overflow in chunk starting at byte {i}")

        valid_bytes = len(block) - 1
        output_buf.extend(raw_block[:valid_bytes])

    return bytes(output_buf)