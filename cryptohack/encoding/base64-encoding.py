# Common encoding scheme - represent binary data as an ASCII string using 64 characters.
# 1 base64 char encodes 6 bits.
# This is web safe
import base64

hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

byte_array = bytearray.fromhex(hex_string)
b64 = base64.standard_b64encode(byte_array)

print(b64)