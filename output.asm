.text
main:
move $a0, None
li $v0, 1
syscall
li $v0, 10
syscall
ComputeFac:
li $t0, 10
jr $ra