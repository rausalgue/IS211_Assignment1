#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week One - Part 2"""

class Book():
    type = "paperback"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self,):
        print(self.title + " written by " + self.author)


firstBook = Book("Of Mice and Men","John Steinbeck")

secondBook = Book("To Kill a Mockingbird","Harper Lee")

firstBook.display()

secondBook.display()
