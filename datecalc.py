# -- imports --
from datetime import date, timedelta

# -- functions --
def lex(input):
    return [("WordToken", input)]

def parse(tokens):
    tok = tokens[0]
    return ("WordToken", tok[1])

def evaluate(tree):
    return ("DateValue", date.today())

# -- tests --
assert lex("today") == [("WordToken", "today")]

def p(x):
    return parse(lex(x))

assert p("today") == ("WordToken", "today")

def e(x):
    return evaluate(parse(lex(x)))

today = date.today()

assert e("today") == ("DateValue", today)

assert lex("tomorrow") == [("WordToken", "tomorrow")]

assert p("tomorrow") == ("WordToken", "tomorrow")

# -- main --
