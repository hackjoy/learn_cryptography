# Hex is a base 16 number system - used as a simpler representation of binary - e.g. 8 bits binary can be represented by 2 hex digits.
# Hex is useful for cipher texts which often have unprintable bytes - so we convert it to hex so that it is easily shared
# Hex itself is an ascii shareable string. base64 is another common encoding for sharing ciphertext

hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
byte_array = bytearray.fromhex(hex_string).decode('ascii')
print(byte_array)


