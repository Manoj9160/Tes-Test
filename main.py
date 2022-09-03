import sys
from parse import parse_input
from logic import Solver, ChessBoard
from output import output_solutions


def main():
    """
    This function runs the process end-to-end: stdin parsing -> find solutions -> output in stdout
    :return: None
    """
    statements = parse_input(sys.stdin.readlines())
    results = Solver(ChessBoard(size=8)).solve(statements)
    output_solutions(results)


# call with: echo "B2 E3" | python main.py
if __name__ == '__main__':
    main()
