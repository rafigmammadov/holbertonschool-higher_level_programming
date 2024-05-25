#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        result_tuple = (0, None)
    else:
        result_tuple = (len(sentence), sentence[:1])

    return result_tuple
