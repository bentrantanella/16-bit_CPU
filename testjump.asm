#My jump function treats the immediate values as
#offsets from the current PC
#All jumps are taken from PC+1 of jump instruction
#After this test is run $1 should contain 3


addi $1 $0 1
j 5
addi $1 $1 1 
addi $1 $1 1    #second jump, $1 = $1+1 = 3
j 4             #jump out
addi $1 $1 1
addi $1 $1 1
addi $1 $1 1    #first jump, $1 = $1+1 = 2
j -6	     