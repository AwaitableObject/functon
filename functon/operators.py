import operator

BINARY_OPERATORS = {}

for op_name in operator.__all__: # type: ignore
    func = getattr(operator, op_name)
    func_doc = func.__doc__

    a_index = func_doc.find(" a ")
    b_index = func_doc.find(" b.", a_index)

    if a_index == 7 and b_index != -1:
        op = func_doc[a_index + 2 : b_index].strip()
        BINARY_OPERATORS[op] = func
