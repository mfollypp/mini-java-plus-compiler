

Production: `PROG`  ->  `['MAIN', 'CLASSE_LIST']`


Analyzing Element: `MAIN` of production


Production: `MAIN`  ->  `['class', 'IDENTIFIER', '{', 'public', 'static', 'void', 'main', '(', 'String', '[', ']', 'IDENTIFIER', ')', '{', 'CMD_LIST', '}', '}']`


Analyzing Element: `class` of production

- Consuming token with value: `class` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `class`                            
- Current token index: 0

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `Factorial` and kind: `IDENTIFIER` (consumed inside production: `MAIN`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 1

Analyzing Element: `{` of production

- Consuming token with value: `{` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `{`                            
- Current token index: 2

Analyzing Element: `public` of production

- Consuming token with value: `public` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `public`                            
- Current token index: 3

Analyzing Element: `static` of production

- Consuming token with value: `static` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `static`                            
- Current token index: 4

Analyzing Element: `void` of production

- Consuming token with value: `void` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `void`                            
- Current token index: 5

Analyzing Element: `main` of production

- Consuming token with value: `main` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `main`                            
- Current token index: 6

Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `(`                            
- Current token index: 7

Analyzing Element: `String` of production

- Consuming token with value: `String` and kind: `RESERVED` (consumed inside production: `MAIN`)                            
- Expected token with value: `String`                            
- Current token index: 8

Analyzing Element: `[` of production

- Consuming token with value: `[` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `[`                            
- Current token index: 9

Analyzing Element: `]` of production

- Consuming token with value: `]` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `]`                            
- Current token index: 10

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `a` and kind: `IDENTIFIER` (consumed inside production: `MAIN`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 11

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `)`                            
- Current token index: 12

Analyzing Element: `{` of production

- Consuming token with value: `{` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `{`                            
- Current token index: 13

Analyzing Element: `CMD_LIST` of production


Production: `CMD_LIST`  ->  `['CMD', 'CMD_LIST']`


Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`System.out.println`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

Expected production element:`if`, but current token is:`System.out.println`
- Heading back to grammar production: `CMD` ->  `['while', '(', 'EXP', ')', 'CMD']`


Analyzing Element: `while` of production

Expected production element:`while`, but current token is:`System.out.println`
- Heading back to grammar production: `CMD` ->  `['System.out.println', '(', 'EXP', ')', ';']`


Analyzing Element: `System.out.println` of production

- Consuming token with value: `System.out.println` and kind: `RESERVED` (consumed inside production: `CMD`)                            
- Expected token with value: `System.out.println`                            
- Current token index: 14

Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `CMD`)                            
- Expected token with value: `(`                            
- Current token index: 15

Analyzing Element: `EXP` of production


Production: `EXP`  ->  `['REXP', 'EXP_1']`


Analyzing Element: `REXP` of production


Production: `REXP`  ->  `['AEXP', 'REXP_1']`


Analyzing Element: `AEXP` of production


Production: `AEXP`  ->  `['MEXP', 'AEXP_1']`


Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `3` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 16
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

- Consuming token with value: `*` and kind: `OPERATOR` (consumed inside production: `MEXP_1`)                            
- Expected token with value: `*`                            
- Current token index: 17

Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`4`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`4`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`4`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`4`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `4` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 18
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`+`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

- Consuming token with value: `+` and kind: `OPERATOR` (consumed inside production: `AEXP_1`)                            
- Expected token with value: `+`                            
- Current token index: 19

Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `3` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 20
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`-`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`-`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

- Consuming token with value: `-` and kind: `OPERATOR` (consumed inside production: `AEXP_1`)                            
- Expected token with value: `-`                            
- Current token index: 21

Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`(`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`(`
- Heading back to grammar production: `PEXP` ->  `['this', 'PEXP_1']`


Analyzing Element: `this` of production

Expected production element:`this`, but current token is:`(`
- Heading back to grammar production: `PEXP` ->  `['new', 'IDENTIFIER', '(', ')', 'PEXP_1']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`(`
- Heading back to grammar production: `PEXP` ->  `['(', 'EXP', ')', 'PEXP_1']`


Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `PEXP`)                            
- Expected token with value: `(`                            
- Current token index: 22

Analyzing Element: `EXP` of production


Production: `EXP`  ->  `['REXP', 'EXP_1']`


Analyzing Element: `REXP` of production


Production: `REXP`  ->  `['AEXP', 'REXP_1']`


Analyzing Element: `AEXP` of production


Production: `AEXP`  ->  `['MEXP', 'AEXP_1']`


Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`3`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `3` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 23
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`+`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

- Consuming token with value: `+` and kind: `OPERATOR` (consumed inside production: `AEXP_1`)                            
- Expected token with value: `+`                            
- Current token index: 24

Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`2`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`2`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`2`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`2`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `2` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 25
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`)`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`)`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`)`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`)`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `PEXP`)                            
- Expected token with value: `)`                            
- Current token index: 26

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`)`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`)`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`)`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`)`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`)`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`)`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`)`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`)`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `CMD`)                            
- Expected token with value: `)`                            
- Current token index: 27

Analyzing Element: `;` of production

- Consuming token with value: `;` and kind: `OPERATOR` (consumed inside production: `CMD`)                            
- Expected token with value: `;`                            
- Current token index: 28
- Exiting grammar production: `CMD`

Analyzing Element: `CMD_LIST` of production


Production: `CMD_LIST`  ->  `['CMD', 'CMD_LIST']`


Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`}`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

Expected production element:`if`, but current token is:`}`
- Heading back to grammar production: `CMD` ->  `['while', '(', 'EXP', ')', 'CMD']`


Analyzing Element: `while` of production

Expected production element:`while`, but current token is:`}`
- Heading back to grammar production: `CMD` ->  `['System.out.println', '(', 'EXP', ')', ';']`


Analyzing Element: `System.out.println` of production

Expected production element:`System.out.println`, but current token is:`}`
- Heading back to grammar production: `CMD` ->  `['IDENTIFIER', 'CMD_ID']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`}`
- Heading back to grammar production: `CMD`
- Heading back to grammar production: `CMD_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `CMD_LIST`
- Exiting grammar production: `CMD_LIST`

Analyzing Element: `}` of production

- Consuming token with value: `}` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `}`                            
- Current token index: 29

Analyzing Element: `}` of production

- Consuming token with value: `}` and kind: `OPERATOR` (consumed inside production: `MAIN`)                            
- Expected token with value: `}`                            
- Current token index: 30
- Exiting grammar production: `MAIN`

Analyzing Element: `CLASSE_LIST` of production


Production: `CLASSE_LIST`  ->  `['CLASSE', 'CLASSE_LIST']`


Analyzing Element: `CLASSE` of production


Production: `CLASSE`  ->  `['class', 'IDENTIFIER', 'CLASSE_EXT', '{', 'VAR_LIST', 'METODO_LIST', '}']`


Analyzing Element: `class` of production

Unexpected end of input, expected `class`
- Heading back to grammar production: `CLASSE`
- Heading back to grammar production: `CLASSE_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `CLASSE_LIST`
- Exiting grammar production: `PROG`