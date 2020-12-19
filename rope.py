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

    def __len__(self):
        return len(str(self))


class String(Rope):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def delete(self, start, end):
        left = self.substring(0, start)
        right = self.substring(end, len(self))
        return left.concatenate(right)


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


# Testing framework


def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    print(actual, "didn't equal", expected)
    raise Exception


equals(to_rope("abc"), "abc")
equals(to_rope("abcde").substring(1, 4), "bcd")
equals(to_rope("abcde").substring(1, 4).substring(1, 2), "c")
equals(to_rope("abc").concatenate("de"), "abcde")
equals(to_rope("abcde").delete(1, 4), "ae")

assert len(to_rope("abcde")) == 5
assert len(to_rope("abcde").substring(1, 4)) == 3