def to_rope(string):
    return String(string)


class Rope:
    def substring(self, start, end):
        return Substring(self, start, end)

    def concatenate(self, right):
        return Concatenation(self, right)

    def delete(self, start, end):
        left = self[0:start]
        right = self[end : len(self)]
        return left + right

    def insert(self, rope, index):
        left = self[0:index]
        right = rope + self[index : len(self)]
        return left.concatenate(right)

    def __len__(self):
        return len(str(self))

    def __add__(self, right):
        return self.concatenate(right)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.substring(index, index + 1)
        return self.substring(index.start, index.stop)


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
