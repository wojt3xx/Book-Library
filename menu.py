import art
import library

is_on = True


def application():
    while is_on:
        print(art.art)
        print("-------------------------------------------------")
        print("Please, choose the option")
        print("1. See the available books")
        print("2. Add the book")
        print("3. Remove the book")
        print("4. Exit")
        print("-------------------------------------------------")

        customer_choice = input("Enter your choice(1/2/3/4): ")

        if customer_choice == "1":
            for i in library.books:
                print(i, "by", library.books[i])
        if customer_choice == "2":
            title = input("Please, enter the title of the book: ")
            author = input("Please, enter the author of the book: ")
            library.books[title] = author
            print("Added " + title + " by " + author + " to the library!")
        if customer_choice == "3":
            title = input("Please, enter the title of the book: ")
            library.books.pop(title)
            print("Removed " + title + " from the library!")
            print(library.books)
        if customer_choice == "4":
            print("Goodbye!")
            exit()


application()
