import sys

def dump_sys():
	'''Show the paths searched on your system.'''
	print('Python is looking in:')
	for path in sys.path:
		print(path)

if __name__ == '__main__':
    dump_sys()
