grammar = {
    "PROG": [
        ["MAIN", "CLASSE_LIST"]
    ],
    "CLASSE_LIST": [
        ["CLASSE", "CLASSE_LIST"], 
        [""]
    ],
    "MAIN": [
        ["class", "IDENTIFIER", "{", "public", "static", "void", "main", "(", "String", "[", "]", "IDENTIFIER", ")", "{", "CMD_LIST", "}", "}"]
    ],
    "CLASSE": [
        ["class", "IDENTIFIER", "CLASSE_EXT", "{", "VAR_LIST", "METODO_LIST", "}"]
    ],
    "CLASSE_EXT": [
        ["extends", "IDENTIFIER"], 
        [""]
    ],
    "VAR_LIST": [
        ["VAR", "VAR_LIST"],
        [""]
    ],
    "METODO_LIST": [
        ["METODO", "METODO_LIST"], 
        [""]
    ],
    "VAR": [
        ["TIPO", "IDENTIFIER", ";"]
    ],
    "METODO": [
        ["public", "TIPO", "IDENTIFIER", "(", "PARAMS", ")", "{", "VAR_LIST", "CMD_LIST", "return", "EXP", ";", "}"]
    ],
    "PARAMS": [
        ["PARAM", "PARAM_LIST"], 
        [""]
    ],
    "PARAM": [
        ["TIPO", "IDENTIFIER"]
    ],
    "PARAM_LIST": [
        [",", "PARAM", "PARAM_LIST"], 
        [""]
    ],
    "TIPO": [
        ["int", "TIPO_1"],
        ["boolean"],
        ["IDENTIFIER"]
    ],
    "TIPO_1": [
        ["[", "]"],
        [""]
    ],
    "CMD_LIST": [
        ["CMD", "CMD_LIST"],
        [""]
    ],
    "CMD": [
        ["{", "CMD_LIST", "}"],
        ["if", "(", "EXP", ")", "CMD", "CMD_ELSE"],
        ["while", "(", "EXP", ")", "CMD"],
        ["System.out.println", "(", "EXP", ")", ";"],
        ["IDENTIFIER", "CMD_ID"]
    ],
    "CMD_ELSE": [
        ["else", "CMD"], 
        [""]
    ],
    "CMD_ID": [
        ["=", "EXP", ";"], 
        ["[", "EXP", "]", "=", "EXP", ";"]
    ],
    "EXP": [
        ["REXP", "EXP_1"]
    ],
    "EXP_1": [
        ["&&", "REXP", "EXP_1"], 
        [""]
    ],
    "REXP": [
        ["AEXP", "REXP_1"]
    ],
    "REXP_1": [
        ["<", "AEXP"], 
        ["==", "AEXP"], 
        ["!=", "AEXP"], 
        [""]
    ],
    "AEXP": [
        ["MEXP", "AEXP_1"]
    ],
    "AEXP_1": [
        ["+", "MEXP", "AEXP_1"], 
        ["-", "MEXP", "AEXP_1"], 
        [""]
    ],
    "MEXP": [
        ["SEXP", "MEXP_1"]
    ],
    "MEXP_1": [
        ["*", "SEXP", "MEXP_1"], 
        [""]
    ],
    "SEXP": [
        ["!", "SEXP"],
        ["-", "SEXP"],
        ["true"],
        ["false"],
        ["NUMBER"],
        ["null"],
        ["new", "int", "[", "EXP", "]"],
        ["PEXP", "SEXP_1"]
    ],
    "SEXP_1": [
        [".", "length"],
        ["[", "EXP", "]"],
        [""]
    ],
    "PEXP": [
        ["IDENTIFIER", "PEXP_1"],
        ["this", "PEXP_1"],
        ["new", "IDENTIFIER", "(", ")", "PEXP_1"],
        ["(", "EXP", ")", "PEXP_1"]
    ],
    "PEXP_1": [
        [".", "IDENTIFIER", "PEXP_2"],
        [""]
    ],
    "PEXP_2": [
        ["(", "EXPS", ")", "PEXP_1"],
        ["PEXP_1"],
    ],
    "EXPS": [
        ["EXP", "EXPS_LIST"], 
        [""]
    ],    
    "EXPS_LIST": [
        [",", "EXP", "EXPS_LIST"], 
        [""]
    ]
}