#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week One"""

class ListDivideException:
    pass

def listDivide(numbers, divide=2):
    """Validates Data for Matchmaking

    Args:
        numbers (list): list of numbers
        divide (int): The mini number of players needed for matches

    Returns:
        divisibleCounter: counter of numbers divisible by divide
    """
    #print numbers

    divisibleCounter = 0
    for x in numbers:
        if x % divide == 0:
            divisibleCounter += 1

    return divisibleCounter


def testListDivide():
    if listDivide([1,2,3,4,5]) != 2:
        raise ListDivideException

    if listDivide([2,4,6,8,10]) != 5:
        raise ListDivideException

    if listDivide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException

    if listDivide([]) != 0:
        raise ListDivideException

    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

testListDivide()