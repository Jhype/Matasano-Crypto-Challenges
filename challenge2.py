from binascii import hexlify, unhexlify

def decodeHex(string1, string2):
	byte1, byte2 = unhexlify(string1), unhexlify(string2)
	return byte1, byte2

def stringXOR(bytes1, bytes2):
	xor =  bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
	return xor

def main():
	string = "1c0111001f010100061a024b53535009181c"
	toxor = "686974207468652062756c6c277320657965"

	string1, string2 = decodeHex(string, toxor)
	print stringXOR(string1, string2)

if __name__ == "__main__":
	main()
