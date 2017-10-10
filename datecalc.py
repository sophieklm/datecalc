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
    if tok[0] == "NumberToken":
        next_tok = tokens[1]
        return (
            "LengthTree",
            tok[1],
            next_tok[1]
        )
    else:
        return ("WordTree", tok[1])

def evaluate(tree):
    if tree[0] == "LengthTree":
        return ("LengthValue", int(tree[1]))
    elif tree[0] == "WordTree":
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

assert p("today") == ("WordTree", "today")

def e(x):
    return evaluate(parse(lex(x)))

today = date.today()

assert e("today") == ("DateValue", today)

assert lex("tomorrow") == [("WordToken", "tomorrow")]

assert p("tomorrow") == ("WordTree", "tomorrow")

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

assert (
    p("2 days") ==
    ("LengthTree", "2", "days")
)

assert e("2 days") == ("LengthValue", 2)

print "All tests passing"

# -- main --
