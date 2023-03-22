#end state: $0=0 $1=6
#procedure: line 6 jump, line 10 jump, line 8 jump

addi $0 $0 0
addi $1 $1 1
j 2
addi $0 $0 1
j 5
addi $1 $1 5
j -3