books = input().split('&')
command = input()
while command != "Done":
    tokens = command.split(' | ')
    todo = tokens[0]
    if todo == "Add Book":
        book = tokens[1]
        if book not in books:
            books.insert(0, book)
    elif todo == "Take Book":
        book = tokens[1]
        for b in books:
            if b == book:
                books.remove(b)
    elif todo == "Swap Books":
        first = tokens[1]
        second = tokens[2]
        first_index = 0
        second_index = 0
        if first in books and second in books:
            for i, b in enumerate(books):
                if b == first:
                    first_index = i
            for i, b in enumerate(books):
                if b == second:
                    second_index = i
        new_first = books[first_index]
        books[first_index] = second
        books[second_index] = new_first
    elif todo == "Insert Book":
        book = tokens[1]
        books.append(book)
    elif todo == "Check Book":
        index = int(tokens[1])
        if 0 <= index <= len(books):
            print(books[index])
    command = input()
print(', '.join(books))