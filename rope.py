# Rope

# Todo
# insert
# delete
# substring
# concat


def to_rope(string):
    return Rope(string)


class Rope:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def substring(self, start, end):
        return Substring(self, start, end)


class Substring:
    def __init__(self, rope, start, end):
        self.rope = rope
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.rope)[self.start : self.end]


assert str(to_rope("abc")) == "abc"
assert str(to_rope("abcde").substring(1, 4)) == "bcd"
