from Day_2_Cube_Conundrum.solution import solution_part_1, solution_part_2


def test_solutions():
    with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.read()
    assert solution_part_1(lines) == 8
    assert solution_part_2(lines) == 2286
