#!/usr/bin/python3

import sys

from transition_table import TransitionTable, InvalidSymbol

def tokenize(s):
    try:
        if len(s) == 0:
            raise StopIteration

        tt = TransitionTable()
        for pos, c in enumerate(s):
            if tt.accept(c):
                continue

            yield tt.current_token()
            tt.reset(c)

        yield tt.current_token()

    except InvalidSymbol as e:
        print("Invalid symbol {} occured at position: {}".format(e.symbol(),
                                                                 pos+1))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit(0)

    s = sys.argv[1]

    for tok in tokenize(s):
        print(tok)
        
