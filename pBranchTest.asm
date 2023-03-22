#end state: $0=17 $1=11
#procedure: line 6 not taken, line 10 taken, line 6 taken, line 10 not taken, line 11 not taken.

addi $0 $0 0
addi $1 $1 1
beq $0 $1 2
add $0 $0 $1
addi $0 $0 5
addi $1 $1 5
beq $0 $1 -5
beq $0 $1 1
add $0 $0 $1

