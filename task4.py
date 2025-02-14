class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published


    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}")


book1 = Book("The Nightingale", "Kristin Hannah", 2015)
book2 = Book("Educated: A Memoir", "Tara Westover", 2018)
book3 = Book("Steve Jobs", "Walter Isaacson", 2011)


book1.describe()
book2.describe()
book3.describe()

