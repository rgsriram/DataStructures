#!/bin/python3

import heapq
import os
import sys


#
# Complete the runningMedian function below.
#

def addNumber(number, highers, lowers):
    if len(lowers) <= 0 or number < lowers[0]:
        lowers.append(number)
        heapq._heapify_max(lowers)
    else:
        highers.append(number)
        heapq.heapify(highers)


def rebalance(highers, lowers):
    if len(lowers) > len(highers) and (len(lowers) - len(highers) >= 2):
        highers.append(heapq._heappop_max(lowers))
        heapq.heapify(highers)

    elif len(lowers) < len(highers) and (len(highers) - len(lowers) >= 2):
        lowers.append(heapq.heappop(highers))
        heapq._heapify_max(lowers)


def getMedian(highers, lowers):
    bigger_heap = lowers if len(lowers) > len(highers) else highers
    smaller_heap = highers if len(lowers) > len(highers) else lowers

    if len(bigger_heap) == len(smaller_heap):
        return (bigger_heap[0] + smaller_heap[0]) / 2.0

    return float(bigger_heap[0])


def runningMedian(a):
    highers = []  # Min heap
    lowers = []  # Max heap

    medians = []

    for number in a:
        addNumber(number, lowers, highers)
        rebalance(lowers, highers)
        medians.append(getMedian(lowers, highers))

    return medians


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
