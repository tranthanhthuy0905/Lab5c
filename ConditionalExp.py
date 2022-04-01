import re


class ConditionalExp:

    def parsing(inputVal):
        identifier_pattern = "[a-z]{1}[a-zA-Z0-9_]*"
        number_pattern = "[+-]?([0-9]*[.]?)[0-9]+"
        arithmetic_pattern = "[+\-*/]"
        conditional_pattern = "(<=)|(>=)|(!=)|(==)|(<)|(>)"
        logical_pattern = "(\&\&)|(\|\|)"
        condStatement_pattern = "X(AOp[NX])*COp([NX]AOp)*[NX](LOpX(AOp[NX])*COp([NX]AOp)*[NX])*"

        check_identifier = re.sub(identifier_pattern, "X", inputVal)
        check_number = re.sub(number_pattern, "N", check_identifier)
        deleting_space = re.sub("\s", "", check_number)
        check_arithmetic = re.sub(arithmetic_pattern, "AOp", deleting_space)

        check_conditional = re.sub(
            conditional_pattern, "COp", check_arithmetic)
        check_logical = re.sub(logical_pattern, "LOp", check_conditional)

        check_condStatement = re.sub(
            condStatement_pattern, "CS", check_logical)
        return check_condStatement
    #parsing("num + 30 - 823 >= 23 + term || num == 82 - 23")
