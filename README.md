1. test_add_new_book_added_one_book - проверяет добавление новой книги
2. test_add_new_book_added_several_books - проверяет добавление нескольких книг
3. test_add_new_book_invalid_length_no_books_added - проверяет, что книги не добавляются, если имя пустое или превышает 40 символов.
4. test_set_book_genre_genre_is_set - проверяет корректную установку жанра книги
5. test_get_book_genre_one_book_without_genre_not_found - проверяет, что книга добавляется без жанра
6. test_get_books_with_specific_genre_returned_books - проверяет, что по указанному жанру возвращаются книги
7. test_get_books_with_specific_genre_genre_not_in_genres_books_not_found - проверяет, что если жанра нет в списке жанров, то вернеся пустой список книг
8. test_get_books_genre_returned_books_with_genres - проверяет, что если жанр есть в списке, то вернется список книг этого жанра
9. test_get_books_for_children_returned_children_books - проверяет, что метод возвращает список книг с жанрами для детей
10. test_add_book_in_favorites_one_book_added - проверяет добавление книги в список избранных
11. test_delete_book_from_favorites_book_is_deleted - проверяет удаление книги из избранного
12. test_get_list_of_favorites_books_returned_all_favourite_books - проверяет, что метод возвращает список всех избранных книг