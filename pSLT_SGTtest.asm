#end state: $2=1 $5=1
#procedure: line 6 true, line 7 false, line 8 false, line 9 true

addi $0 $0 0
addi $1 $1 1
slt $2 $0 $1
slt $3 $1 $0
sgt $4 $0 $1
sgt $5 $1 $0