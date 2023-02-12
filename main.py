# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i - 4))
    
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1 
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position 
    return "Success"


def main():
    text = input().strip()
    result = find_mismatch(text)
    if isinstance(result, int):
        print(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
    
