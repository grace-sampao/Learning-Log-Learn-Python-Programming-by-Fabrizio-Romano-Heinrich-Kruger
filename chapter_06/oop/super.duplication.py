class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

# Three of the input parameters for `Book` are duplicated in `Ebook`.
# This is bad practice ∵ two sets of instructions are doing the same thing.
# Any change in the signature of `Book.__init__()`  will not be reflected in `Ebook`.
# Normally, changes in a base class should be reflected in its children.
