from xmlrpc.client import ExpatParser

from main import BooksCollector
import pytest

class TestBooksCollector:
    # !!! Прошу обратить внимание, что в тесте используется метод get_books_rating, которого нет в классе BooksCollector
    # что приводит к ошибке -> AttributeError: 'BooksCollector' object has no attribute 'get_books_rating'
    # В задании не было сказано дописать метод, поэтому комментирую тест

    # def test_add_new_book_add_two_books(self):
    #     collector = BooksCollector()
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('book_name', ['Пересадочная станция', 'Гарри Поттер', 'Маленький принц'])
    def test_add_new_book_added_one_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'books',
        [
            ['Пересадочная станция', 'Гарри Поттер', 'Маленький принц', 'Человек, который смеётся'],
            ['Пересадочная станция', 'Гарри Поттер', 'Маленький принц'],
            ['Пересадочная станция', 'Гарри Поттер'],
        ]
    )
    def test_add_new_book_added_several_books(self, books):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)

        assert len(collector.books_genre) == len(books)

    @pytest.mark.parametrize('book_name', ['Очень длинное название книги для проверки условия на длину', ''])
    def test_add_new_book_invalid_length_no_books_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert collector.books_genre == {}

    @pytest.mark.parametrize(
        'book_name,book_genre',
        [
            ['Пересадочная станция', 'Фантастика'],
            ['Гарри Поттер', 'Фантастика'],
            ['Понкрат', 'Детективы'],
        ]
    )
    def test_set_book_genre_genre_is_set(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    @pytest.mark.parametrize('book_name', ['Пересадочная станция', 'Гарри Поттер', 'Маленький принц'])
    def test_get_book_genre_one_book_without_genre_not_found(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre_returned_books(self):
        collector = BooksCollector()
        book_name_1 = 'Пересадочная станция'
        book_name_2 = 'Заповедник гоблинов'
        book_genre = 'Фантастика'
        expected_result = [book_name_1, book_name_2]

        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        collector.set_book_genre(book_name_1, book_genre)
        collector.set_book_genre(book_name_2, book_genre)

        assert collector.get_books_with_specific_genre(book_genre) == expected_result

    def test_get_books_with_specific_genre_genre_not_in_genres_books_not_found(self):
        collector = BooksCollector()
        book_name = 'Пересадочная станция'
        book_genre = 'Фантастика'
        search_genre = 'Драма'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_with_specific_genre(search_genre) == []

    def test_get_books_genre_returned_books_with_genres(self):
        collector = BooksCollector()
        book_name = 'Пересадочная станция'
        book_genre = 'Фантастика'
        expected_result = {book_name: book_genre}

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_returned_children_books(self):
        collector = BooksCollector()
        book_name = 'Приключения Лося'
        book_genre = 'Комедии'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_for_children() == [book_name]

    def test_add_book_in_favorites_one_book_added(self):
        collector = BooksCollector()
        book_name = 'Пересадочная станция'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == [book_name]

    def test_delete_book_from_favorites_book_is_deleted(self):
        collector = BooksCollector()
        book_name = 'Пересадочная станция'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_returned_all_favourite_books(self):
        collector = BooksCollector()
        book_name_1 = 'Пересадочная станция'
        book_name_2 = 'Заповедник гоблинов'
        expected_result = [book_name_1, book_name_2]

        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        collector.add_book_in_favorites(book_name_1)
        collector.add_book_in_favorites(book_name_2)

        assert collector.get_list_of_favorites_books() == expected_result

    # Добавлена позитивная проверка после ревью - получаем жанр книги по её имени
    def test_get_book_genre_returned_genre(self):
        collector = BooksCollector()
        book_name = 'Пересадочная станция'
        book_genre = 'Фантастика'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre
