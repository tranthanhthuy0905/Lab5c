import re


class ConditionalExp:
    def parsing(inputVal):
        identifier_pattern = "[a-z]{1}[a-zA-Z0-9_]*"
        number_pattern = "[+-]?([0-9]*[.]?)[0-9]+"
        conditional_pattern = "(<=)|(>=)|(!=)|(==)|(<)|(>)"
        arithmetic_pattern = "[+\-*/]"
        logical_pattern = "(\&\&)|(\|\|)"
        expression_pattern = "[NX]( AOp [NX])*;"
        statement_pattern = "X = E|LOOP|SELECT"
        codeblock_pattern = "(S[ ]?)+"
        condStatement_pattern = "[NX]( AOp [NX])* COp [NX]( AOp [NX])*( LOp [NX]( AOp [NX])* COp [NX]( AOp [NX])*)* "
        _IF = "if"
        _ELSE = "else"
        select_pattern = "_IF (CS) {CB} (_ELSE {CB})?"

        check_identifier = re.sub(identifier_pattern, "X", inputVal)
        check_number = re.sub(number_pattern, "N", check_identifier)
        check_arithmetic = re.sub(arithmetic_pattern, "AOp", check_number)

        check_expression = re.sub(expression_pattern, "E", check_arithmetic)
        check_statement = re.sub(statement_pattern, "S", check_expression)
        check_codeblock = re.sub(codeblock_pattern, "CB", check_statement)

        check_conditional = re.sub(conditional_pattern, "COp", check_arithmetic)
        check_logical = re.sub(logical_pattern, "LOp", check_conditional)

        check_condStatement = re.sub(
            condStatement_pattern, "CS", check_logical)

        print(check_condStatement)
    parsing("num + 30 - 823 >= 23 || num == 82")
