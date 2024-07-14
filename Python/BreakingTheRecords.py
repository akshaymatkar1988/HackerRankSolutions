#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_count = getList(scores, "max")
    min_count = getList(scores, "min")
    
    return [max_count, min_count]
    
def getList(scoreList: list, ops: str):
    
    last_known = scoreList[0]
    count = 0
    for score in scoreList:
        if ops == "max":
            if score > last_known:
                last_known = score
                count += 1
        elif ops == "min":
            if score < last_known:
                last_known = score
                count += 1
        else:
            return 0
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
