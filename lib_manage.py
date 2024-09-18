# Creating Class for Library


class Libary():
    def __init__(self,List_of_books,Library_name):
        self.lend_data = {}
        self.List_of_books = List_of_books
        self.Library_name = Library_name

        for books in self.List_of_books:
            self.lend_data[books] =None
            # none means No author have lend this book
       
    def Display_books(self):
        for index , books in enumerate(self.List_of_books):
            print(f"{index} > {books}")

    def lend_book(self, book_name, author_name):
        if book_name in self.List_of_books:
            if self.lend_data[book_name] is None:
                print(self.lend_data)
                self.lend_data[book_name] = author_name
                print(self.lend_data)
            else:
                print(
                    f"Sorry This Book is lend by {self.lend_data[book_name]}")
        else:
            print("You Have Written wrong Book Name")

    def Return_book(self,book_name, author_name):
        if book_name in self.List_of_books:
            if (self.lend_data[book_name] is not None and self.lend_data[book_name]==author_name):
                self.lend_data[book_name] = None
                print("Return successful")
                print(self.lend_data)
            else:
                print("Sorry This Book is Lend ")
        else:
            print("You Have Written wrong Book Name")

    def Add_book(self,book_name):
        self.List_of_books.append(book_name)
        self.lend_data[book_name] = None

    def Delete_book(self,book_name):
        self.List_of_books.remove(book_name)
        self.lend_data.pop(book_name)


# creating function

def main():
    List_of_books = ['java', 'php','python', 'javascript']
    Library_name = 'National Library'
    Secret_key = 123456

    mylibary = Libary(List_of_books,Library_name)

    print("Welcome to National Library\n 'Q' for Exit \n Display books Press 'D' \n Lend book press 'L' \n Return book using 'R' \n Add book using 'A' \n Delete book using 'DEL'")

    Exit = False
    while(Exit is not True):
        _input= input("Options:")
        print("--------")

        if _input == "Q":
            Exit= True

        elif _input == "D":
            mylibary.Display_books()

        elif _input == "L":
            Book_name = input("Which Book Do you want to lend:")
            Author_name = input("Enter Your Name :")

            mylibary.lend_book(Book_name, Author_name)

        elif _input == "R":
            Book_name = input("Which Book Do you want to Return:")
            Author_name = input("Enter Your Name :")

            mylibary.Return_book(Book_name, Author_name)

        elif _input == "A":
            Book_name = input("Which Book Do you want to Add:")
            mylibary.Add_book(Book_name)
        elif _input == "DEL":
            password = int(input("Enter Password"))
            if(Secret_key==password):
                Book_name = input("Enter Book Name")
                mylibary.Delete_book(Book_name)

       

if __name__ == "__main__":
    main()
