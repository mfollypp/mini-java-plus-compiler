.data
num_aux: .word 0
.text
main:
li $v0, 10
syscall
ComputeFac:
jr $ra