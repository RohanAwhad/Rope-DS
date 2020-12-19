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

    def delete(self, start, end):
        left = self.substring(0, start)
        right = self.substring(end, len(self))
        return left.concatenate(right)

    def insert(self, rope, index):
        left = self.substring(0, index)
        right = rope.concatenate(self.substring(index, len(self)))
        return left.concatenate(right)

    def __len__(self):
        return len(str(self))

    def __add__(self, right):
        return self.concatenate(right)


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

equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")

equals(to_rope("abc") + to_rope("de"), "abcde")