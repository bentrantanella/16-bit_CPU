# CSC-270 Final Project: Track A
# Ben Trantanella
## FinalAssembler.py

The purpose of this program is to read in an assembly file and output a hex file of the converted instructions.
The assembly file contains a list of instructions based on the functionality of my CPU, supporting the following operators:

- Basic ALU operations (add, logical or, logical and, sub)
- Immediate instructions of all ALU ops
- Store word and load word
- Branch-if-equal
- Jump
- Set-less-than and set-greater-than

Each instruction contains two parts, the operator and the operand(s). This assembler works by first splitting the instruction
at each space, with the first element being the operator and everything else the operands. Each operator has a specific
5-digit binary mapping, stored in the global dictionary 'opcodeDict'. For the operands, in my model there are three types of
elements that occur. Registers, immediate values, and offset/base register. Each has it's own case for being translated to
binary, with registers being 3 bits long and immediate values being 16 bits long. The offset/base regsiter is split into it's
respective parts and treated the same. All of these binary conversions are collected in one 27-bit instruction word, which is
then converted to hexadecimal and written to the output file.

There are a few special cases within the assembler that are worth noting. First, in the case of 'R' type instructions where
all of the operands are registers, bits 0-12 are filled in with zeros and then ignored by the CPU. Next, since jump instructions
are only two elements long (ex. j 10), we must fill in the middle bits between the op code and the immediate value with zeros
which are once again ignored. Finally, since branch-if-equal instructions come with the control hazard of needing to stall for
one cycle before knowing which instruction to fetch next, we must add in a 'NOOP', or no operation. This is represented by the
assembly line: `addi $0 $0 0` or the hex value: `4000000`, which essentaily does nothing.

Overall the goal of this program is to easily convert my created assembly language code into hexadecimal format, with the ability
to load that directly into my CPU and run the instructions successfully.

