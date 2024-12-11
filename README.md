# mini-java-plus-compiler


## GRAMÁTICA AMBÍGUA:

E -> E + E | E * E | (E) | id

## REMOVENDO AMBIGUIDADE:

E -> E + T | T

T -> T * F | F

F -> (E) | id

---

## GRAMÁTICA RECURSIVA À ESQUERDA:

E -> E + T | T

T -> T * F | F

F -> (E) | id

## REMOVENDO RECURSIVIDADE À ESQUERDA:

E -> T E'

E' -> + T E' | ε

T -> F T'

T' -> * F T' | ε

F -> (E) | id

---

## GRAMÁTICA NÃO FATORADA À ESQUERDA:

STMT -> if (EXPR) { STMT } | if (EXPR) { STMT } else { STMT }

## FATORANDO À ESQUERDA:

STMT -> if (EXPR) { STMT } SENAO

SENAO -> else { STMT } | ε