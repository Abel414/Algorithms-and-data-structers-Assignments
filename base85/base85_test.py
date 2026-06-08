"""
Unit tests for 02.Base85
"""

import pytest
import base85ed
import random


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"


def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"


def test_03_empty_data_edge_case():
    """
    Test edge case with empty bytes input
    """
    assert base85ed.encode(b"") == b""
    assert base85ed.decode(b"") == b""


def test_04_roundtrip_text():
    """
    Test that decoding an encoded string returns the exact original text
    """
    original = b"Hello, World! This is a longer string."
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert decoded == original


def test_05_roundtrip_binary():
    """
    Test roundtrip with pure binary data (all possible byte values)
    """
    original = bytes(range(256))
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert decoded == original


def test_06_multiple_chunks():
    """
    Test data that spans across multiple 4-byte chunks
    """
    original = b"12345"
    assert base85ed.decode(base85ed.encode(original)) == original

    original = b"12345678"
    assert base85ed.decode(base85ed.encode(original)) == original


def test_07_decode_invalid_character():
    """
    Test that decoding an invalid Base85 character raises a ValueError
    """
    with pytest.raises(ValueError, match="Invalid Base85 character"):
        base85ed.decode(b"F# ")


def test_08_decode_overflow():
    """
    Test that decoding a sequence that exceeds 32 bits raises a ValueError
    """
    with pytest.raises(ValueError, match="Base85 overflow"):
        base85ed.decode(b"~~~~~")

    with pytest.raises(ValueError, match="Base85 overflow"):
        base85ed.decode(b"~~~~")


def test_09_partial_chunks_high_bytes():
    """
    Test partial chunks with maximum byte values to ensure padding doesn't corrupt data.
    This specifically stress-tests the fix made in the decode function.
    """
    original = b"\xff"
    assert base85ed.decode(base85ed.encode(original)) == original

    original = b"\xff\xff"
    assert base85ed.decode(base85ed.encode(original)) == original

    original = b"\xff\xff\xff"
    assert base85ed.decode(base85ed.encode(original)) == original


def test_10_all_modulo_lengths_roundtrip():
    """
    Test roundtrip for lengths 0 through 12 to exhaustively cover all modulo 4 boundaries.
    """
    for length in range(13):
        original = bytes([i % 256 for i in range(length)])
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original, f"Failed at length {length}"


def test_11_max_32bit_value_roundtrip():
    """
    Test the absolute maximum 32-bit value (4 bytes of 0xFF)
    to ensure no overflow occurs during the encode/decode cycle.
    """
    original = b"\xff\xff\xff\xff"
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert decoded == original
    assert len(encoded) == 5


def test_12_large_payload_roundtrip():
    """
    Test roundtrip with a large payload (e.g., 10,000 bytes)
    to ensure chunking logic holds up at scale without state leakage.
    """
    original = bytes([i % 256 for i in range(10000)])
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert decoded == original
    assert len(encoded) == 12500


def test_13_decode_rejects_whitespace():
    """
    Test that common Base85 formatting characters are correctly rejected.
    """
    with pytest.raises(ValueError, match="Invalid Base85 character"):
        base85ed.decode(b"F}\n")

    with pytest.raises(ValueError, match="Invalid Base85 character"):
        base85ed.decode(b"F}\r")

    with pytest.raises(ValueError, match="Invalid Base85 character"):
        base85ed.decode(b"F} ")


def test_14_encode_type_enforcement():
    """
    Test that @beartype correctly rejects string inputs for encode.
    """
    with pytest.raises(Exception):
        base85ed.encode("not a bytes object")  # type: ignore


def test_15_decode_type_enforcement():
    """
    Test that @beartype correctly rejects string inputs for decode.
    """
    with pytest.raises(Exception):
        base85ed.decode("not a bytes object")  # type: ignore


def test_16_single_byte_all_values():
    """
    Test all single-byte values (0–255) for roundtrip correctness
    """
    for i in range(256):
        original = bytes([i])
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original, f"Failed for byte {i}"


def test_17_two_byte_patterns():
    """
    Test deterministic patterns of 2-byte sequences
    """
    patterns = [
        b"\x00\x00",
        b"\xff\x00",
        b"\x00\xff",
        b"\xff\xff",
        b"\x12\x34",
        b"\xab\xcd",
    ]
    for original in patterns:
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original


def test_18_prefix_suffix_integrity():
    """
    Test that prefix/suffix bytes are preserved in longer payloads
    """
    original = b"\x01" + bytes(range(1, 50)) + b"\xff"
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert decoded == original


def test_19_random_small_samples():
    """
    Test random small payloads for robustness
    """
    random.seed(42)
    for _ in range(200):
        length = random.randint(1, 20)
        original = bytes(random.randint(0, 255) for _ in range(length))
        encoded = base85ed.encode(original)
        decoded = base85ed.decode(encoded)
        assert decoded == original


def test_20_mixed_invalid_char_sequences():
    """
    Test decoding of mixed invalid sequences inside payloads
    """
    with pytest.raises(ValueError):
        base85ed.decode(b"F}A\nB")

    with pytest.raises(ValueError):
        base85ed.decode(b"@@@ \xff")

    with pytest.raises(ValueError):
        base85ed.decode(b"\tF}K")