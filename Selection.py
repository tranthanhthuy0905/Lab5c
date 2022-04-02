from calendar import c
import ConditionalExp
from ConditionalExp import *
import re


class Selection:

    def selectionParse(inputVal):

        _ELSEIF = "else if"
        _IF = "if"
        _ELSE = "else"
        _WH = "while"
        expression_pattern = "[NX](AOp[NX])*;"
        statement_pattern = "X=E|LOOP|SELECT"
        codeblock_pattern = "[{](S)+"
        if_else_pattern = "_IF\(CS\)\{CB\}(_ELSEIF\(CS\)\{CB\})*(_ELSE\{CB\})*"
        while_pattern = "_WH\(CS\)\{CB\}"
        isWhile = True
        
        check_while= re.sub(_WH, "_WH", inputVal)
        if check_while == inputVal:
            check_elseif = re.sub(_ELSEIF, "_ELSEIF", inputVal)
            check_if = re.sub(_IF, "_IF", check_elseif)
            check_else = re.sub(_ELSE, "_ELSE", check_if)
            check_condition = ConditionalExp.parsing(check_else)
            isWhile = False
        else:
            check_condition = ConditionalExp.parsing(check_while)
        check_expression = re.sub(expression_pattern, "E", check_condition)
        check_statement = re.sub(statement_pattern, "S", check_expression)
        check_codeblock = re.sub(codeblock_pattern, "{CB", check_statement)
        if isWhile:
            check_selection = re.sub(while_pattern, "SELECT", check_codeblock)
        else: 
            check_selection = re.sub(if_else_pattern, "SELECT", check_codeblock)
        print(check_selection)

    selectionParse("while (x>5){ x = x + 1; y = x; }")
    selectionParse("if (x > 5) {x = x + 1; y = 3/2;} else if (x > 2) {x = x - 1;} else {x = y;}")
