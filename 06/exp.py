"""Exception演示

语法:
IndentationError
SyntaxError
NameError

数据访问:
IndexError
ValueError
TypeError
KeyError
"""

import traceback

def add(x, y):
    result = None

    try:
        result = int(x) + int(y)
    except Exception as err:
        traceback.print_exc()
        print(str(err))
    else:
        print('everything is ok')
    finally:
        print('clear up')

    return result
