class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nItem ID: {self.item_id}\nChecked Out: {self.checked_out}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.pages = pages

    def display_info(self):
        info = super().display_info()
        return f"{info}\nPages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def display_info(self):
        info = super().display_info()
        return f"{info}\nDuration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_date):
        super().__init__(title, publisher, item_id)
        self.issue_date = issue_date

    def display_info(self):
        info = super().display_info()
        return f"{info}\nIssue Date: {self.issue_date}"

# Example usage:
if __name__ == "__main__":
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 101, 180)
    print(book.check_out())
    print(book.display_info())
    print(book.check_out())

    dvd = DVD("Inception", "Christopher Nolan", 201, 148)
    print(dvd.display_info())
    print(dvd.return_item())

    magazine = Magazine("National Geographic", "National Geographic Society", 301, "October 2022")
    print(magazine.check_out())
    print(magazine.display_info())
    print(magazine.return_item())
