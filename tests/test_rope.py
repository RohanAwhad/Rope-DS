from src.rope import to_rope


def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    print(actual, "didn't equal", expected)
    raise Exception


def test_casting():
    equals(to_rope("abc"), "abc")


def test_slicing_rope():
    equals(to_rope("abcde").substring(1, 4), "bcd")


def test_slicing_sliced_rope():
    equals(to_rope("abcde").substring(1, 4).substring(1, 2), "c")


def test_concatenate():
    equals(to_rope("abc").concatenate("de"), "abcde")


def test_delete():
    equals(to_rope("abcde").delete(1, 4), "ae")


def test_len_of_rope():
    assert len(to_rope("abcde")) == 5


def test_len_of_sliced_rope():
    assert len(to_rope("abcde").substring(1, 4)) == 3


def test_insert_rope():
    equals(to_rope("abe").insert(to_rope("cd"), 2), "abcde")


def test_concatenate_string_with_add_symbol():
    equals(to_rope("abc") + "de", "abcde")


def test_concatenate_rope_with_add_symbol():
    equals(to_rope("abc") + to_rope("de"), "abcde")


def test_slicing_rope_with_brackets():
    equals(to_rope("abcde")[1:4], "bcd")


def test_slicing_concatenated_rope_with_brackets():
    equals((to_rope("abc") + to_rope("de"))[1:4], "bcd")


def test_indexing_with_brackets():
    equals(to_rope("abcde")[2], "c")


def test_indexing_concatenated_rope_with_brackets():
    equals((to_rope("abc") + to_rope("de"))[2], "c")
