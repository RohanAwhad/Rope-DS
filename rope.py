# Rope

# Todo
# insert
# delete
# substring
# concat


def to_rope(string):
    return String(string)


class Rope:
    def substring(self, start, end):
        return Substring(self, start, end)

    def concatenate(self, right):
        return Concatenation(self, right)


class String(Rope):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string


class Substring(Rope):
    def __init__(self, rope, start, end):
        self.rope = rope
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.rope)[self.start : self.end]


class Concatenation(Rope):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + str(self.right)


assert str(to_rope("abc")) == "abc"
assert str(to_rope("abcde").substring(1, 4)) == "bcd"
assert str(to_rope("abcde").substring(1, 4).substring(1, 2)) == "c"
assert str(to_rope("abc").concatenate("de")) == "abcde"
