# SKELETON ASSEMBLER WRITTEN BY JOHN RIEFFEL
# MODIFY AND ADD YOUR NAME FOR CSC270 FINAL PROJECT

import sys


opcodeDict = {'add':'00000', 'addi':'10000', 'and':'00001', 'andi':'10001', 
	      'or':'00010', 'ori':'10010', 'sub':'00011', 'subi':'10011', 
		  'sw':'11000', 'lw':'10100', 'beq':'01111', 'j':'01110', 
		  'slt':'01011', 'sgt':'00111'}

noop = '100000000000000000000000000'

def ConvertAssemblyToMachineCode(inline):
	'''given a string corresponding to a line of assembly,
	strip out all the comments, parse it, and convert it into
	a string of binary values'''

	outstring = ''

	if inline.find('#') != -1:
		inline = inline[0:inline.find('#')] #get rid of anything after a comment
	if inline != '':
		words = inline.split() #assuming syntax words are separated by space, not comma
		operation = words[0]
		operands = words[1:]
		outstring += opcodeDict[operation]
		if operation == 'j':
			outstring += '000000'
		for operand in operands:
			if operand[0] == '$':	#registers
				outstring += int2bs(operand[1:],3)
			elif operand.find('(') != -1:	#offset+register
				offandreg = operand.split('(')
				off = offandreg[0]
				reg = offandreg[1]
				outstring += int2bs(reg[1:2], 3)
				outstring += int2bs(off, 16)
			else:	#immediate val
				outstring += int2bs(operand, 16)
	
	if inline.count('$') == 3:	#adding unused immediate bits if R type
		outstring += '0000000000000'
			 
	return outstring	
 		

def AssemblyToHex(infilename,outfilename):
	'''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
	then save that machinecode to an outputfile'''
	outlines = []
	with open(infilename) as f:
		lines = [line.rstrip() for line in f.readlines()]  #get rid of \n whitespace at end of line
		for curline in lines:
			outstring = ConvertAssemblyToMachineCode(curline)	
			if outstring != '':
				outlines.append(outstring)

	f.close()

	with open(outfilename,'w') as of:
		of.write('v2.0 raw')
		of.write("\n")
		for outline in outlines:
			hexoutline = bs2hex(outline)
			of.write(hexoutline)
			of.write(' ')
			if outline[:5] == '01111':	#adding in NOOP if branch instruction
				hexnoop = bs2hex(noop)
				of.write(hexnoop)
				of.write(' ')

	of.close()		


def int2bs(s, n):
    """ Converts an integer string to a 2s complement binary string.

        Args: s = Integer string to convert.to 2s complement binary.
              n = Length of outputted binary string.
        
        Example Input: stpd("4", 4)
        Example Output: "0100"

        Example Input: stpd("-3", 16)
        Example Output: "1111111111111101" """
    x = int(s)                              # Convert string to integer, store in x.
    if x >= 0:                              # If not negative, use python's binary converter and strip the "0b"
        ret = str(bin(x))[2:]
        return ("0"*(n-len(ret)) + ret)     # Pad with 0s to length.
    else:
        ret = 2**n - abs(x)                 # If negative, convert to 2s complement integer
        return bin(ret)[2:]                 # Convert to binary using python's binary converter and strip the "0b"
    

def bs2hex(v):
	""" Converts a binary string into hex.

		Args: v = Binary string to convert to hex

		Example Input: bs2hex("1010000010001111") 
		Example Output: "a08f" """
	out = (hex(int(v,2))[2:])

	return out


if __name__ == "__main__":
	#in order to run this with command-line arguments
	# we need this if __name__ clause
	# and then we need to read in the subsequent arguments in a list.
	
	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler

	#print ('Number of arguments:', len(sys.argv), 'arguments.')
	#print ('Argument List:', str(sys.argv))

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args	
	if (len(sys.argv) != 3):
		print('usage: python FinalAssembler.py test.asm output.hex')
		exit(0)
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	AssemblyToHex(inputfile,outputfile)
