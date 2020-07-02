#!/usr/bin/python

import re

# For testing
#txt="0000000000400f63 <main+0x9f> mov    rbx,rax"

# If needed, changing the name of the function analyzing
# TODO: receive the name of the function to analyze in command line
funName='main'
pattern='<{}\+0x[0-9a-fA-F]+>'.format(funName)

hexaPattern = re.compile(pattern)

finalFileName='convertedDump'
finalFileObj=open(finalFileName, 'w')

with open('disasuaf', 'r') as reader:
	line=reader.readline()
	# If not EOF
	while line!='':
		#print(line,end='')
		line=reader.readline()
		match=re.search(hexaPattern, line)
		if match:
			start,end=match.span()
			num=int(line[start+6:end-1],16)
			finalFileObj.write("{}{}{}".format(line[:start+6], num, line[end-1:]))

