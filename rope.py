# Rope

# Todo
# insert
# delete
# substring
# concat


def to_rope(string):
    return string


class Rope:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string


assert str(to_rope("abc")) == "abc"
