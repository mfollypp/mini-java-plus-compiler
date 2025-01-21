.text
main:
sw $fp 0($sp)
addiu $sp $sp -4
li $a0 10
sw $a0 0($sp)
addiu $sp $sp -4
jal _Fac_ComputeFac
li $v0 1
syscall
li $v0 10
syscall
Fac:
jr $ra
_Fac_ComputeFac:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t0 4($sp)
addiu $sp $sp 4
slt $a0 $t0, $a0
beq $a0, $zero, else_0
li $a0 1
sw $a0 4($sp)
sw $a0 4($sp)
j end_if_0
else_0:
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t0 4($sp)
addiu $sp $sp 4
sub $a0 $t0, $a0
sw $a0 0($sp)
addiu $sp $sp -4
jal _Fac_ComputeFac
lw $t0 4($sp)
addiu $sp $sp 4
mul $a0 $t0 $a0
sw $a0 4($sp)
sw $a0 4($sp)
end_if_0:
lw $a0 4($sp)
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra