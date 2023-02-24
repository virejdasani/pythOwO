import re

# Regular expressions to match patterns in Python code
var_regex = r"please\s+(\w+)\s*=\s*(.+)"
if_regex = r"IF\s+(.+)\s+THEN\s+(.+?)(?:\s+EWIF\s+(.+)\s+THEN\s+(.+?))*(?:\s+EWSE\s+(.+?))?"
for_regex = r"FOR\s+(\w+)\s*=\s*(\d+)\s+TO\s+(\d+)\s+THEN\s+(.+)\s+END"
func_regex = r"FUNCTION\s+(\w+)\((.*?)\)\s*->\s*(.+)"

def owofy_file(file_path):
    with open(file_path) as f:
        code = f.read()

    # Replace variables
    code = re.sub(var_regex, r"please \1 = \2", code)
    
    # Replace conditionals
    code = re.sub(if_regex, lambda m: f"IF {owofy_expression(m.group(1))} THEN {owofy_expression(m.group(2))} {'EWIF ' + owofy_expression(m.group(3)) + ' THEN ' + owofy_expression(m.group(4)) if m.group(3) else ''} {'EWSE ' + owofy_expression(m.group(5)) if m.group(5) else ''}", code, flags=re.DOTALL)
    
    # Replace loops
    code = re.sub(for_regex, r"FOR \1 = \2 TO \3 THEN\n    \4\nEND", code)
    
    # Replace functions
    code = re.sub(func_regex, r"FUNCTION \1(\2) ->\n    " + owofy_expression(r"\3").replace("\n", "\n    "), code)

    # Add PythOwO documentation
    code = f"""\
# Documentation

## General
# To open the Python shell, run `python shwell.py`.
# Executing code from a file can be done by running `run("{file_path}.pyowo")` from the shell.

{code}"""

    # Write the PythOwO code to a new file
    with open(f"{file_path}.pyowo", "w") as f:
        f.write(code)
def owofy_expression(expression):
    # Replace common Python keywords and operators
    expression = expression.replace(" and ", " awnd ")
    expression = expression.replace(" or ", " owo ")
    expression = expression.replace(" not ", " nyot ")
    expression = expression.replace("==", " eqwals ")
    expression = expression.replace("!=", " nyot eqwals ")
    expression = expression.replace("<=", " wess than or eqwals ")
    expression = expression.replace(">=", " mowe than or eqwals ")
    expression = expression.replace("<", " wess than ")
    expression = expression.replace(">", " mowe than ")
    expression = expression.replace("+", " plus ")
    expression = expression.replace("-", " minus ")
    expression = expression.replace("*", " times ")
    expression = expression.replace("/", " divided by ")
    expression = expression.replace("%", " mod ")
    expression = expression.replace("**", " to the powew of ")
    
    # Replace variables and function calls
    expression = re.sub(r"\b(\w+)\b", r"please \1", expression)
    expression = re.sub(r"\b(\w+)\((.*?)\)\b", r"\1(\2)", expression)
    
    # Add OwOs and UwUs
    expression = expression.replace("r", "w")
    expression = expression.replace("l", "w")
    expression = expression.replace("ove", "uv")
    expression = expression.replace("no", "nu")
    expression = expression.replace(" mo", " mowo")
    expression = expression.replace(".", " uwu. UwU")
    expression = expression.replace("?", " OwO?")

    return expression
