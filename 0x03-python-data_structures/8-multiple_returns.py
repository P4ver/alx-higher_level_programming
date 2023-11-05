#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        ntuple_a1 = len(sentence)
        ntuple_a2 = sentence[0]
        return ntuple_a1, ntuple_a2
    else:
        return (0, None)
