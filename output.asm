.text
main:
sw $fp 0($sp)
sw $a0 0($sp)
addiu $sp, $sp, -4
addiu $sp, $sp, -4
li $a0, 10
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
jal _Fac_ComputeFac_ComputeFac
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
li $v0, 1
syscall
li $v0, 10
syscall
Fac:
jr $ra
_Fac_ComputeFac_ComputeFac:
move $fp $sp
sw $ra 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0, 4($fp)
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $t0 4($sp)
addiu $sp, $sp, 4
mul $a0, $t0, $a0
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0, 8($sp)
sw $a0, 8($sp)
lw $a0, 8($sp)
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
sw $a0 0($sp)
addiu $sp, $sp, -4
lw $a0 4($sp)
addiu $sp, $sp, 4
jr $ra