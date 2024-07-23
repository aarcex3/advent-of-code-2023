from Day_1_Trebuchet.solutions import solution_part_1, solution_part_2


def test_solution_part_1():
    with open("example_part_1.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert solution_part_1(lines) == 142


def test_solution_part_2():
    with open("example_part_2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert solution_part_2(lines) == 281
