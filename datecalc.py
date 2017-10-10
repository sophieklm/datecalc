# -- imports --
from datetime import date, timedelta

# -- functions --
def make_token(word):
    if word[0] in "0123456789":
        return ("NumberToken", word)
    else:
        return ("WordToken", word)

def lex(input):
    return [
        make_token(word)
        for word in input.split(" ")
    ]

def parse(tokens):
    tok = tokens[0]
    return ("WordToken", tok[1])

def evaluate(tree):
    if tree[1] == "today":
        return ("DateValue", date.today())
    elif tree[1] == "tomorrow":
        return (
            "DateValue",
            date.today() + timedelta(days=1)
    )

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

def days(n):
    return timedelta(days=n)

assert (
    e("tomorrow") == ("DateValue", today + days(1))
)

assert (
    lex("2 days") ==
    [
        ("NumberToken", "2"),
        ("WordToken", "days")
    ]
)

print "All tests passing"

# -- main --
