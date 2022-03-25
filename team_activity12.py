'''
Brother Alex Bedino

file_name = team_activity12.py

Scope = read through a file and organize data

'''
# defining the variables for comparison first

largest_num = 0
max_book = ()

with open("books_and_chapters.txt") as books_chapter:
    for books in books_chapter:
        sep_books = books.strip()
        sep_books = sep_books.split(":")
        scripture = sep_books[2]
        book = sep_books[0]
        chapter = sep_books[1]
        print (f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
print()
with open("books_and_chapters.txt") as books_chapter:

    for books in books_chapter:
        sep_books = books.strip()
        sep_books = sep_books.split(":")
        scripture = sep_books[2]
        book = sep_books[0]
        chapter = int(sep_books[1])
        if chapter > largest_num:
            largest_num = chapter
            max_book = book
    print (f"The book with the largest number of chapters in the scriptures is {max_book} and it has {largest_num} chapters")

# stretch challenge 1

with open("books_and_chapters.txt") as books_chapter:

    for books in books_chapter:
        sep_books = books.strip()
        sep_books = sep_books.split(":")
        scripture = sep_books[2]
        book = sep_books[0]
        chapter = int(sep_books[1])
        if scripture == ("Book of Mormon"):
            print (book)

# stretch challenge 2

book_m = ()
chapter_l = 0 

with open("books_and_chapters.txt") as books_chapter:

    for books in books_chapter:
        sep_books = books.strip()
        sep_books = sep_books.split(":")
        scripture = sep_books[2]
        book = sep_books[0]
        chapter = int(sep_books[1])
        if scripture == ("Book of Mormon"):
            if chapter > chapter_l:
                chapter_l = chapter
                book_m = book 

print (f"The book in the Book of Mormon with the largest number of chapters is {book_m}")

# stretch challenge 3

book_m = ()
chapter_l = 0 
query = input("Which book would you like to learn about? ")

with open("books_and_chapters.txt") as books_chapter:

    for books in books_chapter:
        sep_books = books.strip()
        sep_books = sep_books.split(":")
        scripture = sep_books[2]
        book = sep_books[0]
        chapter = int(sep_books[1])
        if scripture == query:
            if chapter > chapter_l:
                chapter_l = chapter
                book_m = book 

print (f"The book in {query} with the largest number of chapters is {book_m}")
