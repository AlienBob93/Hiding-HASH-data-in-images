# Prashant Rao
import string
import re
import Image
import binascii

## open file method
def separate(filename):
	with open(filename) as myfile:
		for line in myfile:
			all_strings = list(map(''.join, zip(*[iter(line)]*8)))       	
	myfile.close()
	return all_strings

## main
## load hash file as string
hashstr = separate('hash.txt')
ascii = []
for word in hashstr:
	ascii[len(ascii):] = [ord(x) for x in word]
size = 1000
#print (ascii)
for word in ascii:
	ascii0 = ascii[0:8]
	ascii1 = ascii[8:17]
	ascii2 = ascii[16:26]
	ascii3 = ascii[24:32]

ascii_hash = []
for x in range(0, 4):
	## creating a new black image
	#print (globals()['ascii%s' % x])
	globals()['img%s' % x] = Image.new('RGB',(size,size), "black")
	pixels = globals()['img%s' % x].load()	# create the pixel map
	k = 0
	for i in range(globals()['img%s' % x].size[0]):
		for j in range(globals()['img%s' % x].size[1]):
			if k < len(globals()['ascii%s' % x]):
				n = globals()['ascii%s' % x][k]
				pixels[i,j] = (i,j, n)
			else:
				pixels[i,j] = (i,j, k)
			k += 1
	## save generated image
	IMAGE = str('image%s.jpeg' % x)
	globals()['img%s' % x].save(IMAGE)	
	globals()['read_ascii%s' % x] = []
	## read hash from the images
	for i in range(globals()['img%s' % x].size[0]):
		for j in range(globals()['img%s' % x].size[1]):
			globals()['read_ascii%s' % x][len(globals()['read_ascii%s' % x]):] = pixels[i,j]
	globals()['ascii_hash%s' % x] = globals()['read_ascii%s' % x][2::3]
	globals()['ascii_hash%s' % x] = globals()['ascii_hash%s' % x][:8]
	globals()['ascii_hash%s' % x] = map(chr, globals()['ascii_hash%s' % x])
	globals()['ascii_hash%s' % x] = ''.join(globals()['ascii_hash%s' % x])
	ascii_hash[len(ascii_hash):] = globals()['ascii_hash%s' % x]	

## display results
ascii_hash = ''.join(ascii_hash)
print ('Recovered HASH',ascii_hash)
print ('\n')
print ('Original HASH',''.join(hashstr))
