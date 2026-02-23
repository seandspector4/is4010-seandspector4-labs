class Book:
    def __init__(self, title, author, year):
        # Store the parameters as instance attributes
        self.title = title
        self.author = author
        self.year = year

      # Create the __str__ dunder method to return a user friendly string with the title, author, and publication year.
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    

    #The book class needs method called get_age() that takes no parameters (except self) and calculates and returns the book age based on the year it was published. Assume it is currently 2025.
    def get_age(self):
        current_year = 2025
        return current_year - self.year

        print(f"Age of the book: {Book.get_age()} years")

    #There needs to be a child class of Book called EBook. It inherits from Book. The Ebook's __init__ method should take all of the same parameters as Book, but also a new one called fil_size (int, representing megabytes). In this method, use the super() function.

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    #Override the __str__ method in Ebook. This new __str__ method should call the parent's __str__ methos using the super() function to get the base string and add file size info to it. The output should have all book details and the file size.
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - File Size: {self.file_size} MB"


 #At the bottom of the file, create main execution block(if __name == '__main__':) to test. In this block, create at least 1 instance of the Book class and print() to the console to verify the __str__ method is working.
if __name__ == '__main__':
    book = Book("1984", "George Orwell", 1948)
    print(book)
    #Also add an instance of the Ebook class  and print it to the console. Make sure to call the get_age() method.
    ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 2)
    print(ebook)
    print(f"Age of the ebook: {ebook.get_age()} years")