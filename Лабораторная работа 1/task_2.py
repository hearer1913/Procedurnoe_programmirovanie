# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_diskette = 1.44
pages = 100
lines = 50
symbols = 25
volume_of_symbol = 4

one_book = pages * lines * symbols * volume_of_symbol
volume_of_diskette = volume_of_diskette * 1024 * 1024
count_of_books = int(volume_of_diskette/one_book)
print("Количество книг, помещающихся на дискету:", count_of_books)
