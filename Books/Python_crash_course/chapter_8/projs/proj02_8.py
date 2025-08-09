def books():
    top_10_books = []
    for i in range(10):
        new_favorite_book = input("please enter your book number {}: ".format(i + 1))
        top_10_books.append(new_favorite_book)

    for index, book in enumerate(top_10_books, start=1):
        print("your book number {} is: {}".format(index, book))

books()
