

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

Expected production element:`!`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`new`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

- Consuming token with value: `new` and kind: `RESERVED` (consumed inside production: `SEXP`)                            
- Expected token with value: `new`                            
- Current token index: 16

Analyzing Element: `int` of production

Expected production element:`int`, but current token is:`Fac`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`new`
- Heading back to grammar production: `PEXP` ->  `['this', 'PEXP_1']`


Analyzing Element: `this` of production

Expected production element:`this`, but current token is:`new`
- Heading back to grammar production: `PEXP` ->  `['new', 'IDENTIFIER', '(', ')', 'PEXP_1']`


Analyzing Element: `new` of production

- Consuming token with value: `new` and kind: `RESERVED` (consumed inside production: `PEXP`)                            
- Expected token with value: `new`                            
- Current token index: 16

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `Fac` and kind: `IDENTIFIER` (consumed inside production: `PEXP`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 17

Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `PEXP`)                            
- Expected token with value: `(`                            
- Current token index: 18

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `PEXP`)                            
- Expected token with value: `)`                            
- Current token index: 19

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

- Consuming token with value: `.` and kind: `OPERATOR` (consumed inside production: `PEXP_1`)                            
- Expected token with value: `.`                            
- Current token index: 20

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `ComputeFac` and kind: `IDENTIFIER` (consumed inside production: `PEXP_1`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 21

Analyzing Element: `PEXP_2` of production


Production: `PEXP_2`  ->  `['(', 'EXPS', ')', 'PEXP_1']`


Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `PEXP_2`)                            
- Expected token with value: `(`                            
- Current token index: 22

Analyzing Element: `EXPS` of production


Production: `EXPS`  ->  `['EXP', 'EXPS_LIST']`


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

Expected production element:`!`, but current token is:`20`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`20`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`20`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`20`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `20` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 23
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`,`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`,`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`,`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`,`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `EXPS_LIST` of production


Production: `EXPS_LIST`  ->  `[',', 'EXP', 'EXPS_LIST']`


Analyzing Element: `,` of production

- Consuming token with value: `,` and kind: `OPERATOR` (consumed inside production: `EXPS_LIST`)                            
- Expected token with value: `,`                            
- Current token index: 24

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

Expected production element:`!`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `10` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
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

Analyzing Element: `EXPS_LIST` of production


Production: `EXPS_LIST`  ->  `[',', 'EXP', 'EXPS_LIST']`


Analyzing Element: `,` of production

Expected production element:`,`, but current token is:`)`
- Heading back to grammar production: `EXPS_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXPS_LIST`
- Exiting grammar production: `EXPS_LIST`
- Exiting grammar production: `EXPS`

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `PEXP_2`)                            
- Expected token with value: `)`                            
- Current token index: 26

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`)`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP_2`
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

- Consuming token with value: `class` and kind: `RESERVED` (consumed inside production: `CLASSE`)                            
- Expected token with value: `class`                            
- Current token index: 31

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `Fac` and kind: `IDENTIFIER` (consumed inside production: `CLASSE`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 32

Analyzing Element: `CLASSE_EXT` of production


Production: `CLASSE_EXT`  ->  `['extends', 'IDENTIFIER']`


Analyzing Element: `extends` of production

Expected production element:`extends`, but current token is:`{`
- Heading back to grammar production: `CLASSE_EXT` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `CLASSE_EXT`

Analyzing Element: `{` of production

- Consuming token with value: `{` and kind: `OPERATOR` (consumed inside production: `CLASSE`)                            
- Expected token with value: `{`                            
- Current token index: 33

Analyzing Element: `VAR_LIST` of production


Production: `VAR_LIST`  ->  `['VAR', 'VAR_LIST']`


Analyzing Element: `VAR` of production


Production: `VAR`  ->  `['TIPO', 'IDENTIFIER', ';']`


Analyzing Element: `TIPO` of production


Production: `TIPO`  ->  `['int', 'TIPO_1']`


Analyzing Element: `int` of production

Expected production element:`int`, but current token is:`public`
- Heading back to grammar production: `TIPO` ->  `['boolean']`


Analyzing Element: `boolean` of production

Expected production element:`boolean`, but current token is:`public`
- Heading back to grammar production: `TIPO` ->  `['IDENTIFIER']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`public`
- Heading back to grammar production: `TIPO`
- Heading back to grammar production: `VAR`
- Heading back to grammar production: `VAR_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `VAR_LIST`

Analyzing Element: `METODO_LIST` of production


Production: `METODO_LIST`  ->  `['METODO', 'METODO_LIST']`


Analyzing Element: `METODO` of production


Production: `METODO`  ->  `['public', 'TIPO', 'IDENTIFIER', '(', 'PARAMS', ')', '{', 'VAR_LIST', 'CMD_LIST', 'return', 'EXP', ';', '}']`


Analyzing Element: `public` of production

- Consuming token with value: `public` and kind: `RESERVED` (consumed inside production: `METODO`)                            
- Expected token with value: `public`                            
- Current token index: 34

Analyzing Element: `TIPO` of production


Production: `TIPO`  ->  `['int', 'TIPO_1']`


Analyzing Element: `int` of production

- Consuming token with value: `int` and kind: `RESERVED` (consumed inside production: `TIPO`)                            
- Expected token with value: `int`                            
- Current token index: 35

Analyzing Element: `TIPO_1` of production


Production: `TIPO_1`  ->  `['[', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`ComputeFac`
- Heading back to grammar production: `TIPO_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `TIPO_1`
- Exiting grammar production: `TIPO`

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `ComputeFac` and kind: `IDENTIFIER` (consumed inside production: `METODO`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 36

Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `METODO`)                            
- Expected token with value: `(`                            
- Current token index: 37

Analyzing Element: `PARAMS` of production


Production: `PARAMS`  ->  `['PARAM', 'PARAM_LIST']`


Analyzing Element: `PARAM` of production


Production: `PARAM`  ->  `['TIPO', 'IDENTIFIER']`


Analyzing Element: `TIPO` of production


Production: `TIPO`  ->  `['int', 'TIPO_1']`


Analyzing Element: `int` of production

- Consuming token with value: `int` and kind: `RESERVED` (consumed inside production: `TIPO`)                            
- Expected token with value: `int`                            
- Current token index: 38

Analyzing Element: `TIPO_1` of production


Production: `TIPO_1`  ->  `['[', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`num`
- Heading back to grammar production: `TIPO_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `TIPO_1`
- Exiting grammar production: `TIPO`

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num` and kind: `IDENTIFIER` (consumed inside production: `PARAM`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 39
- Exiting grammar production: `PARAM`

Analyzing Element: `PARAM_LIST` of production


Production: `PARAM_LIST`  ->  `[',', 'PARAM', 'PARAM_LIST']`


Analyzing Element: `,` of production

Expected production element:`,`, but current token is:`)`
- Heading back to grammar production: `PARAM_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PARAM_LIST`
- Exiting grammar production: `PARAMS`

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `METODO`)                            
- Expected token with value: `)`                            
- Current token index: 40

Analyzing Element: `{` of production

- Consuming token with value: `{` and kind: `OPERATOR` (consumed inside production: `METODO`)                            
- Expected token with value: `{`                            
- Current token index: 41

Analyzing Element: `VAR_LIST` of production


Production: `VAR_LIST`  ->  `['VAR', 'VAR_LIST']`


Analyzing Element: `VAR` of production


Production: `VAR`  ->  `['TIPO', 'IDENTIFIER', ';']`


Analyzing Element: `TIPO` of production


Production: `TIPO`  ->  `['int', 'TIPO_1']`


Analyzing Element: `int` of production

- Consuming token with value: `int` and kind: `RESERVED` (consumed inside production: `TIPO`)                            
- Expected token with value: `int`                            
- Current token index: 42

Analyzing Element: `TIPO_1` of production


Production: `TIPO_1`  ->  `['[', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`num_aux`
- Heading back to grammar production: `TIPO_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `TIPO_1`
- Exiting grammar production: `TIPO`

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num_aux` and kind: `IDENTIFIER` (consumed inside production: `VAR`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 43

Analyzing Element: `;` of production

- Consuming token with value: `;` and kind: `OPERATOR` (consumed inside production: `VAR`)                            
- Expected token with value: `;`                            
- Current token index: 44
- Exiting grammar production: `VAR`

Analyzing Element: `VAR_LIST` of production


Production: `VAR_LIST`  ->  `['VAR', 'VAR_LIST']`


Analyzing Element: `VAR` of production


Production: `VAR`  ->  `['TIPO', 'IDENTIFIER', ';']`


Analyzing Element: `TIPO` of production


Production: `TIPO`  ->  `['int', 'TIPO_1']`


Analyzing Element: `int` of production

Expected production element:`int`, but current token is:`if`
- Heading back to grammar production: `TIPO` ->  `['boolean']`


Analyzing Element: `boolean` of production

Expected production element:`boolean`, but current token is:`if`
- Heading back to grammar production: `TIPO` ->  `['IDENTIFIER']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`if`
- Heading back to grammar production: `TIPO`
- Heading back to grammar production: `VAR`
- Heading back to grammar production: `VAR_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `VAR_LIST`
- Exiting grammar production: `VAR_LIST`

Analyzing Element: `CMD_LIST` of production


Production: `CMD_LIST`  ->  `['CMD', 'CMD_LIST']`


Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`if`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

- Consuming token with value: `if` and kind: `RESERVED` (consumed inside production: `CMD`)                            
- Expected token with value: `if`                            
- Current token index: 45

Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `CMD`)                            
- Expected token with value: `(`                            
- Current token index: 46

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

Expected production element:`!`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num` and kind: `IDENTIFIER` (consumed inside production: `PEXP`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 47

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`<`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`<`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`<`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`<`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`<`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`<`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

- Consuming token with value: `<` and kind: `OPERATOR` (consumed inside production: `REXP_1`)                            
- Expected token with value: `<`                            
- Current token index: 48

Analyzing Element: `AEXP` of production


Production: `AEXP`  ->  `['MEXP', 'AEXP_1']`


Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `1` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 49
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
- Exiting grammar production: `AEXP`
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
- Current token index: 50

Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

Expected production element:`if`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['while', '(', 'EXP', ')', 'CMD']`


Analyzing Element: `while` of production

Expected production element:`while`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['System.out.println', '(', 'EXP', ')', ';']`


Analyzing Element: `System.out.println` of production

Expected production element:`System.out.println`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['IDENTIFIER', 'CMD_ID']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num_aux` and kind: `IDENTIFIER` (consumed inside production: `CMD`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 51

Analyzing Element: `CMD_ID` of production


Production: `CMD_ID`  ->  `['=', 'EXP', ';']`


Analyzing Element: `=` of production

- Consuming token with value: `=` and kind: `OPERATOR` (consumed inside production: `CMD_ID`)                            
- Expected token with value: `=`                            
- Current token index: 52

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

Expected production element:`!`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `1` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 53
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`;`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`;`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `;` of production

- Consuming token with value: `;` and kind: `OPERATOR` (consumed inside production: `CMD_ID`)                            
- Expected token with value: `;`                            
- Current token index: 54
- Exiting grammar production: `CMD_ID`
- Exiting grammar production: `CMD`

Analyzing Element: `CMD_ELSE` of production


Production: `CMD_ELSE`  ->  `['else', 'CMD']`


Analyzing Element: `else` of production

- Consuming token with value: `else` and kind: `RESERVED` (consumed inside production: `CMD_ELSE`)                            
- Expected token with value: `else`                            
- Current token index: 55

Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

Expected production element:`if`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['while', '(', 'EXP', ')', 'CMD']`


Analyzing Element: `while` of production

Expected production element:`while`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['System.out.println', '(', 'EXP', ')', ';']`


Analyzing Element: `System.out.println` of production

Expected production element:`System.out.println`, but current token is:`num_aux`
- Heading back to grammar production: `CMD` ->  `['IDENTIFIER', 'CMD_ID']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num_aux` and kind: `IDENTIFIER` (consumed inside production: `CMD`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 56

Analyzing Element: `CMD_ID` of production


Production: `CMD_ID`  ->  `['=', 'EXP', ';']`


Analyzing Element: `=` of production

- Consuming token with value: `=` and kind: `OPERATOR` (consumed inside production: `CMD_ID`)                            
- Expected token with value: `=`                            
- Current token index: 57

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

Expected production element:`!`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num` and kind: `IDENTIFIER` (consumed inside production: `PEXP`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 58

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`*`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`*`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`*`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

- Consuming token with value: `*` and kind: `OPERATOR` (consumed inside production: `MEXP_1`)                            
- Expected token with value: `*`                            
- Current token index: 59

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
- Current token index: 60

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

Expected production element:`!`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`this`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`this`
- Heading back to grammar production: `PEXP` ->  `['this', 'PEXP_1']`


Analyzing Element: `this` of production

- Consuming token with value: `this` and kind: `RESERVED` (consumed inside production: `PEXP`)                            
- Expected token with value: `this`                            
- Current token index: 61

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

- Consuming token with value: `.` and kind: `OPERATOR` (consumed inside production: `PEXP_1`)                            
- Expected token with value: `.`                            
- Current token index: 62

Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `ComputeFac` and kind: `IDENTIFIER` (consumed inside production: `PEXP_1`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 63

Analyzing Element: `PEXP_2` of production


Production: `PEXP_2`  ->  `['(', 'EXPS', ')', 'PEXP_1']`


Analyzing Element: `(` of production

- Consuming token with value: `(` and kind: `OPERATOR` (consumed inside production: `PEXP_2`)                            
- Expected token with value: `(`                            
- Current token index: 64

Analyzing Element: `EXPS` of production


Production: `EXPS`  ->  `['EXP', 'EXPS_LIST']`


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

Expected production element:`!`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`num`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num` and kind: `IDENTIFIER` (consumed inside production: `PEXP`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 65

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`-`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`-`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`-`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
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
- Current token index: 66

Analyzing Element: `MEXP` of production


Production: `MEXP`  ->  `['SEXP', 'MEXP_1']`


Analyzing Element: `SEXP` of production


Production: `SEXP`  ->  `['!', 'SEXP']`


Analyzing Element: `!` of production

Expected production element:`!`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`1`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `1` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 67
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`,`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`,`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`,`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`,`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`,`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `EXPS_LIST` of production


Production: `EXPS_LIST`  ->  `[',', 'EXP', 'EXPS_LIST']`


Analyzing Element: `,` of production

- Consuming token with value: `,` and kind: `OPERATOR` (consumed inside production: `EXPS_LIST`)                            
- Expected token with value: `,`                            
- Current token index: 68

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

Expected production element:`!`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`10`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

- Consuming token with value: `10` and kind: `NUMBER` (consumed inside production: `SEXP`)                            
- Expected token with value: `NUMBER`                            
- Current token index: 69
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

Analyzing Element: `EXPS_LIST` of production


Production: `EXPS_LIST`  ->  `[',', 'EXP', 'EXPS_LIST']`


Analyzing Element: `,` of production

Expected production element:`,`, but current token is:`)`
- Heading back to grammar production: `EXPS_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXPS_LIST`
- Exiting grammar production: `EXPS_LIST`
- Exiting grammar production: `EXPS`

Analyzing Element: `)` of production

- Consuming token with value: `)` and kind: `OPERATOR` (consumed inside production: `PEXP_2`)                            
- Expected token with value: `)`                            
- Current token index: 70

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`)`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP_2`
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
- Current token index: 71

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`;`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`;`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`;`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`;`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`;`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `;` of production

- Consuming token with value: `;` and kind: `OPERATOR` (consumed inside production: `CMD_ID`)                            
- Expected token with value: `;`                            
- Current token index: 72
- Exiting grammar production: `CMD_ID`
- Exiting grammar production: `CMD`
- Exiting grammar production: `CMD_ELSE`
- Exiting grammar production: `CMD`

Analyzing Element: `CMD_LIST` of production


Production: `CMD_LIST`  ->  `['CMD', 'CMD_LIST']`


Analyzing Element: `CMD` of production


Production: `CMD`  ->  `['{', 'CMD_LIST', '}']`


Analyzing Element: `{` of production

Expected production element:`{`, but current token is:`return`
- Heading back to grammar production: `CMD` ->  `['if', '(', 'EXP', ')', 'CMD', 'CMD_ELSE']`


Analyzing Element: `if` of production

Expected production element:`if`, but current token is:`return`
- Heading back to grammar production: `CMD` ->  `['while', '(', 'EXP', ')', 'CMD']`


Analyzing Element: `while` of production

Expected production element:`while`, but current token is:`return`
- Heading back to grammar production: `CMD` ->  `['System.out.println', '(', 'EXP', ')', ';']`


Analyzing Element: `System.out.println` of production

Expected production element:`System.out.println`, but current token is:`return`
- Heading back to grammar production: `CMD` ->  `['IDENTIFIER', 'CMD_ID']`


Analyzing Element: `IDENTIFIER` of production

Expected production element:`IDENTIFIER`, but current token is:`return`
- Heading back to grammar production: `CMD`
- Heading back to grammar production: `CMD_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `CMD_LIST`
- Exiting grammar production: `CMD_LIST`

Analyzing Element: `return` of production

- Consuming token with value: `return` and kind: `RESERVED` (consumed inside production: `METODO`)                            
- Expected token with value: `return`                            
- Current token index: 73

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

Expected production element:`!`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['-', 'SEXP']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['true']`


Analyzing Element: `true` of production

Expected production element:`true`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['false']`


Analyzing Element: `false` of production

Expected production element:`false`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['NUMBER']`


Analyzing Element: `NUMBER` of production

Expected production element:`NUMBER`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['null']`


Analyzing Element: `null` of production

Expected production element:`null`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['new', 'int', '[', 'EXP', ']']`


Analyzing Element: `new` of production

Expected production element:`new`, but current token is:`num_aux`
- Heading back to grammar production: `SEXP` ->  `['PEXP', 'SEXP_1']`


Analyzing Element: `PEXP` of production


Production: `PEXP`  ->  `['IDENTIFIER', 'PEXP_1']`


Analyzing Element: `IDENTIFIER` of production

- Consuming token with value: `num_aux` and kind: `IDENTIFIER` (consumed inside production: `PEXP`)                            
- Expected token with value: `IDENTIFIER`                            
- Current token index: 74

Analyzing Element: `PEXP_1` of production


Production: `PEXP_1`  ->  `['.', 'IDENTIFIER', 'PEXP_2']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`;`
- Heading back to grammar production: `PEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `PEXP_1`
- Exiting grammar production: `PEXP`

Analyzing Element: `SEXP_1` of production


Production: `SEXP_1`  ->  `['.', 'length']`


Analyzing Element: `.` of production

Expected production element:`.`, but current token is:`;`
- Heading back to grammar production: `SEXP_1` ->  `['[', 'EXP', ']']`


Analyzing Element: `[` of production

Expected production element:`[`, but current token is:`;`
- Heading back to grammar production: `SEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `SEXP_1`
- Exiting grammar production: `SEXP`

Analyzing Element: `MEXP_1` of production


Production: `MEXP_1`  ->  `['*', 'SEXP', 'MEXP_1']`


Analyzing Element: `*` of production

Expected production element:`*`, but current token is:`;`
- Heading back to grammar production: `MEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `MEXP_1`
- Exiting grammar production: `MEXP`

Analyzing Element: `AEXP_1` of production


Production: `AEXP_1`  ->  `['+', 'MEXP', 'AEXP_1']`


Analyzing Element: `+` of production

Expected production element:`+`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['-', 'MEXP', 'AEXP_1']`


Analyzing Element: `-` of production

Expected production element:`-`, but current token is:`;`
- Heading back to grammar production: `AEXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `AEXP_1`
- Exiting grammar production: `AEXP`

Analyzing Element: `REXP_1` of production


Production: `REXP_1`  ->  `['<', 'AEXP']`


Analyzing Element: `<` of production

Expected production element:`<`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['==', 'AEXP']`


Analyzing Element: `==` of production

Expected production element:`==`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['!=', 'AEXP']`


Analyzing Element: `!=` of production

Expected production element:`!=`, but current token is:`;`
- Heading back to grammar production: `REXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `REXP_1`
- Exiting grammar production: `REXP`

Analyzing Element: `EXP_1` of production


Production: `EXP_1`  ->  `['&&', 'REXP', 'EXP_1']`


Analyzing Element: `&&` of production

Expected production element:`&&`, but current token is:`;`
- Heading back to grammar production: `EXP_1` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `EXP_1`
- Exiting grammar production: `EXP`

Analyzing Element: `;` of production

- Consuming token with value: `;` and kind: `OPERATOR` (consumed inside production: `METODO`)                            
- Expected token with value: `;`                            
- Current token index: 75

Analyzing Element: `}` of production

- Consuming token with value: `}` and kind: `OPERATOR` (consumed inside production: `METODO`)                            
- Expected token with value: `}`                            
- Current token index: 76
- Exiting grammar production: `METODO`

Analyzing Element: `METODO_LIST` of production


Production: `METODO_LIST`  ->  `['METODO', 'METODO_LIST']`


Analyzing Element: `METODO` of production


Production: `METODO`  ->  `['public', 'TIPO', 'IDENTIFIER', '(', 'PARAMS', ')', '{', 'VAR_LIST', 'CMD_LIST', 'return', 'EXP', ';', '}']`


Analyzing Element: `public` of production

Expected production element:`public`, but current token is:`}`
- Heading back to grammar production: `METODO`
- Heading back to grammar production: `METODO_LIST` ->  `['']`


Analyzing Element: `""` of production

- Exiting grammar production: `METODO_LIST`
- Exiting grammar production: `METODO_LIST`

Analyzing Element: `}` of production

- Consuming token with value: `}` and kind: `OPERATOR` (consumed inside production: `CLASSE`)                            
- Expected token with value: `}`                            
- Current token index: 77
- Exiting grammar production: `CLASSE`

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
- Exiting grammar production: `CLASSE_LIST`
- Exiting grammar production: `PROG`