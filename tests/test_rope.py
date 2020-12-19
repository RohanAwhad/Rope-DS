from src.rope import to_rope


def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    print(actual, "didn't equal", expected)
    raise Exception


def test_casting():
    equals(to_rope("abc"), "abc")


equals(to_rope("abcde").substring(1, 4), "bcd")
equals(to_rope("abcde").substring(1, 4).substring(1, 2), "c")
equals(to_rope("abc").concatenate("de"), "abcde")
equals(to_rope("abcde").delete(1, 4), "ae")

assert len(to_rope("abcde")) == 5
assert len(to_rope("abcde").substring(1, 4)) == 3

equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")

equals(to_rope("abc") + "de", "abcde")
equals(to_rope("abc") + to_rope("de"), "abcde")

equals(to_rope("abcde")[1:4], "bcd")
equals((to_rope("abc") + to_rope("de"))[1:4], "bcd")
equals(to_rope("abcde")[2], "c")
equals((to_rope("abc") + to_rope("de"))[2], "c")
