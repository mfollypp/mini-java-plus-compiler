.text
main:
sw 0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw 0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw 0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw 0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
move $a0, $a0
li $v0, 1
syscall
li $v0, 10
syscall
Fac:
jr $ra