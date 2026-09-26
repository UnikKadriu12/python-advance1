from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_into(self):
        pass


class Book(Printable):

    def __init__(self, title, author):
        self.title = title
        self.author = author


    # e implementojna metoden abstrakte
    def print_info(self):
        print(f"book : {self.title} by {self.author}")


book3456 = Book("atomic habits","james clear")

book3456.print_info()