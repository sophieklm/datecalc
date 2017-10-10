# -- imports --
from datetime import date, timedelta

# -- functions --
def lex(input):
    return [("WordToken", input)]

def parse(tokens):
    tok = tokens[0]
    return ("WordToken", tok[1])

# -- tests --
assert lex("today") == [("WordToken", "today")]

def p(x):
    return parse(lex(x))

assert p("today") == ("WordToken", "today")

# -- main --
