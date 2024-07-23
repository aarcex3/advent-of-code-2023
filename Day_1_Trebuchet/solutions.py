import re

# Define regex pattern for word-to-digit conversion
WORD_TO_DIGIT = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
    "hundred": "100",
}

# Regex to match words representing numbers
NUMBER_WORDS_REGEX = re.compile(
    r"""(?=(one))|
        (?=(two))|
        (?=(three))|
        (?=(four))|
        (?=(five))|
        (?=(sixteen|six))|
        (?=(seventeen|seven))|
        (?=(eighteen|eight))|
        (?=(nineteen|nine))|
        (?=(ten))|
        (?=(eleven))|
        (?=(twelve))|
        (?=(thirteen))|
        (?=(fourteen))|
        (?=(fifteen))|
        (?=(twenty))|
        (?=(thirty))|
        (?=(forty))|
        (?=(fifty))|
        (?=(sixty))|
        (?=(seventy))|
        (?=(eighty))|
        (?=(ninety))|
        (?=(hundred))|
        (?=(\d+))""",
    re.VERBOSE,
)


def solution_part_1(puzzles: list[str]) -> int:
    puzzles = [re.sub(r"\D", "", puzzle.strip()) for puzzle in puzzles]
    return sum(
        int(puzzle * 2) if len(puzzle) == 1 else int(puzzle[0] + puzzle[-1])
        for puzzle in puzzles
    )


# with open("puzzles.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(solution_part_1(lines))


def extract_matches(texts: list[str]) -> list[str]:
    """
    Extract the numbers written as words and convert them into their numeric value
    """
    matches = []
    for text in texts:
        match = re.findall(NUMBER_WORDS_REGEX, text)
        filtered_matches = [item_i for item in match for item_i in item if item_i]
        numbers = [WORD_TO_DIGIT.get(word, word) for word in filtered_matches]
        matches.append("".join(numbers))
    return matches


def solution_part_2(puzzles: list[str]) -> int:
    extracted_matches = extract_matches(puzzles)
    return solution_part_1(extracted_matches)


# Uncomment the following lines to read from a file and print results
# with open("puzzles.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(solution_part_2(lines))
