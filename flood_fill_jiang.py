from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

board_2 = [
    "......................",
    "......##########......",
    "......#....#...#......",
    "......#....#...#......",
    "......#....#...#####..",
    "....###....#.......#..",
    "....#......#.....###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # ensure the length of each row is same
    for r in range(1, len(input_board)):
        assert len(input_board[r]) == len(input_board[0])
    
    # when input out of the board
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board

    if input_board[x][y] == old:
        # replace old with new through string concatenation
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        # in four directions
        flood_fill(input_board, old, new, x + 1, y)
        flood_fill(input_board, old, new, x - 1, y)
        flood_fill(input_board, old, new, x, y + 1)
        flood_fill(input_board, old, new, x, y - 1)

    return input_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
modified_board_2 = flood_fill(input_board=board_2, old=".", new="~", x=5, y=12)

print('test case1')

for a in modified_board:
    print(a)


# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

print('test case2')
for a in modified_board_2:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#....#~~~#......
# ......#....#~~~#......
# ......#....#~~~#####..
# ....###....#~~~~~~~#..
# ....#......#~~~~~###..
# ....##############....

expected_output = [
    '......................',
    '......##########......',
    '......#~~~~~~~~#......',
    '......#~~~~~~~~#......',
    '......#~~~~~~~~#####..',
    '....###~~~~~~~~~~~~#..',
    '....#~~~~~~~~~~~~###..',
    '....##############....'
]

expected_output_2 = [
    '......................',
    '......##########......',
    '......#....#~~~#......',
    '......#....#~~~#......',
    '......#....#~~~#####..',
    '....###....#~~~~~~~#..',
    '....#......#~~~~~###..',
    '....##############....'
]

assert modified_board == expected_output
assert modified_board_2 == expected_output_2
