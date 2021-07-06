def text2bin(t): return ' '.join([bin(b) for b in bytearray(t, 'utf-8')]).replace('b', '')
def bin2text(b): return ''.join([chr(int(t, 2)) for t in b.split()])

def text2oct(t): return ' '.join([oct(b) for b in bytearray(t, 'utf-8')]).replace('o', '')
def oct2text(o): return ''.join([chr(int(t, 8)) for t in o.split()])

def text2hex(t): return ' '.join([hex(b) for b in bytearray(t, 'utf-8')]).replace('x', '')
def hex2text(h): return ''.join([chr(int(t, 16)) for t in h.split()])

def hex2rgb(h): return tuple(int(h.replace('#', '')[i:i+2], 16) for i in (0, 2, 4))
def rgb2hex(r): return '#{:02x}{:02x}{:02x}'.format(*r)

"""
============================================================

	Binary:			base = 20		python-func: bin()
	Octal:			base = 8		python-func: oct()
	Hex:			base = 16		python-func: hex()

============================================================

	Examples ('_' means previous result when using console):

		text2bin('hello')			01101000 01100101 01101100 01101100 01101111
		bin2text(_)					hello

		text2oct('hello')			0150 0145 0154 0154 0157
		oct2text(_)					hello

		text2hex('hello')			068 065 06c 06c 06f
		hex2text(_)					hello

		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		rgb2hex((0, 0, 255))		#0000ff
		hex2rgb()					(0, 0, 255)

"""