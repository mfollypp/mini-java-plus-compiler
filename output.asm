.text
main:
move $a0, None
li $v0, 1
syscall
li $v0, 10
syscall
Teste:
sw 0 0($sp)
addiu $sp, $sp, -4
sw 0 0($sp)
addiu $sp, $sp, -4
jr $ra
Fac:
sw 0 0($sp)
addiu $sp, $sp, -4
jr $ra