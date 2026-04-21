from datetime import datetime 

book_list = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Wuthering Heights",
    "Jane Eyre",
    "The Lord of the Rings",
    "Harry Potter and the Philosopher's Stone",
    "The Hobbit",
    "Moby Dick",
    "Brave New World",
    "The Picture of Dorian Gray",
    "Frankenstein",
    "Dracula",
    "Don Quixote",
    "War and Peace",
    "Crime and Punishment",
    "The Brothers Karamazov",
    "Anna Karenina"]

issued_book=[]
details_of_customer_with_books={}


def display_books():
    print("\nAvailble Books:\n",book_list)

def add_book():
    Add= input("\nEnter The Book Name:\n")
    book_list.append(Add)
    if Add in book_list:
        print('\nYOU HAVE SUCCESFULLY DONATED TO THE BOOK\n')
    else:
        print('\nTRY AGAIN\n')

def book_issue():
    print("\nAvailable Books in Library:\n")
    for b in book_list:
        print(b)
    Name=input("\nEnter Your Name\n")
    Contact_Detail=input("\nEnter Your Contact Number:\n")
    period=input("\nHow many days Do you want to keep th book:\n")
    Date_Detail=str(datetime.now())
    Issue=input("\nEnter the book name which book you want to issue:\n")

    if Issue in book_list:      
        issued_book.append(Issue)
        book_list.remove(Issue)
        details_of_customer_with_books[Contact_Detail]={"Name":Name,
                                                        "Time_Period":period,
                                                        "Issued_Book":Issue,
                                                        "Date":Date_Detail}
        print("Thanks to choose me for Reading")
    else:
        print(Issue,", Currently this book is not in the Library")

def book_return():
    Return= input("Enter the book name:")
    if Return in issued_book:
        issued_book.remove(Return)
        book_list.append(Return)
        print("Thanks for reading the book and choosin goue library")
    else: 
        print("This book is not issued till now")

print("Please Select Your Choice")
print("Press 1 to check available books in library\n" \
"Press 2 to donate any book\n" \
"Press 3 to Book issue\n" \
"Press 4 to return the issued book")


while True:
    customer_choice=int(input("\nEnter Your Choice:\n"))
    if customer_choice>=1 and customer_choice<=4:
        if customer_choice==1:
            display_books()
        elif customer_choice==2:
            add_book()
        elif customer_choice==3:
            book_issue()
        elif customer_choice==4:
            book_return()
    else:
        print("\nSelect the options carefully\n")
        pass

#print(details_of_customer_with_books)