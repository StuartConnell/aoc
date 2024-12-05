from typing import List
from pprint import pprint


def get_inputs() -> List[List[str]]:
    lines = []
    with open("data.txt") as f:
        lines = f.readlines()

    lines_for_searching = [list(line) for line in lines]
    return lines_for_searching


def filter_inputs(inputs: List[List[str]]) -> List[List[str]]:

    filtered = []
    for inp in inputs:
        line = [c for c in inp if c != "\n"]
        filtered.append(line)
    return filtered


def count_horizontal_xmas(lines: List[List[str]]) -> int:
    count = 0

    for line in lines:
        for i, c in enumerate(line):
            if i + 3 >= len(line):
                break

            if c == "X":
                if line[i+1] == "M" and line[i+2] == "A" and line[i+3] == "S":
                    count += 1
            elif c == "S":
                if line[i+1] == "A" and line[i+2] == "M" and line[i+3] == "X":
                    count += 1
    return count


def count_vertical_xmas(lines: List[List[str]]) -> int:
    count = 0

    for i, l in enumerate(lines):
        if i + 3 >= len(lines):
            break

        for j, c in enumerate(l):
            if c == "X":
                if lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                    count += 1
            elif c == "S":
                if lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                    count += 1
    return count


def count_diagonal_xmas(lines: List[List[str]]) -> int:
    count = 0

    height = len(lines)
    line_length = len(lines[0])
    for i, l in enumerate(lines):

        if i + 3 >= height:
            break

        for j, c in enumerate(l):

            if c == "X":

                if j >= 3:
                    if lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                        count += 1

                if j < line_length - 3:
                    if lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                        count += 1

            elif c == "S":
                if j >= 3:
                    if lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                        count += 1

                if j < line_length - 3:
                    if lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                        count += 1

    return count


def main():
    inputs = get_inputs()
    filtered = filter_inputs(inputs)
    horizontal_count = count_horizontal_xmas(filtered)
    vertical_count = count_vertical_xmas(filtered)
    diagonal_count = count_diagonal_xmas(filtered)

    print(f"Horizontal: {horizontal_count}")
    print(f"Vertical: {vertical_count}")
    print(f"Diagonal: {diagonal_count}")
    print(f"Total: {horizontal_count + vertical_count + diagonal_count}")


if __name__ == '__main__':
    main()
