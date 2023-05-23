from pycalc.constants import *

def evaluateExpression(expression):
    """
    Evaluate expression in calculator display
    and return result.
    """
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
        
    return result
