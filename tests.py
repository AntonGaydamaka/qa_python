from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_raiting()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
     # проверяем, что одну и ту же книгу нельзя добавить дважды
    def test_add_new_book_add_same_book_twice_added_once(self):
        collector = BooksCollector()
        # добавляем одну и ту же книгу два раза
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # проверяем, что добавилась только одна книга
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книга с названием длиннее 40 символов не добавляется
    def test_add_new_book_name_with_41_symbols_not_added(self):
        collector = BooksCollector()
        # пытаемся добавить книгу с названием из 41 символа
        collector.add_new_book('А' * 41)
        # проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    # проверяем, что книга с названием ровно 40 символов добавляется успешно
    def test_add_new_book_name_with_40_symbols_added(self):
        collector = BooksCollector()
        # добавляем книгу с названием из 40 символов
        collector.add_new_book('А' * 40)
        # проверяем, что книга добавилась
        assert len(collector.get_books_genre()) == 1

    # проверяем, что книгу с пустым названием нельзя добавить
    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        # пытаемся добавить книгу с пустым названием
        collector.add_new_book('')
        # проверяем, что книга не добавилась
        assert len(collector.get_books_genre()) == 0

    # проверяем, что при добавлении новой книги жанр у нее пустой
    def test_add_new_book_genre_is_empty(self):
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Война и мир')
        # проверяем, что жанр у книги пустой
        assert collector.get_book_genre('Война и мир') == ''

    # Тесты для set_book_genre
    
    # проверяем, что можно установить валидный жанр книге
    def test_set_book_genre_set_valid_genre(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Дюна')
        # устанавливаем жанр из списка доступных
        collector.set_book_genre('Дюна', 'Фантастика')
        # проверяем, что жанр установился
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # проверяем, что нельзя установить жанр, которого нет в списке доступных
    def test_set_book_genre_set_invalid_genre_not_set(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Дюна')
        # пытаемся установить жанр, которого нет в списке genre
        collector.set_book_genre('Дюна', 'Драма')
        # проверяем, что жанр остался пустым
        assert collector.get_book_genre('Дюна') == ''

    # проверяем, что нельзя установить жанр книге, которая не добавлена в коллекцию
    def test_set_book_genre_book_not_in_collection_genre_not_set(self):
        collector = BooksCollector()
        # пытаемся установить жанр книге, которой нет в коллекции
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        # проверяем, что метод get_book_genre вернул None для несуществующей книги
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тесты для get_book_genre
    
    # проверяем, что метод возвращает корректный жанр книги
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        # добавляем книгу и устанавливаем ей жанр
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        # проверяем, что метод вернул правильный жанр
        assert collector.get_book_genre('Оно') == 'Ужасы'

    # проверяем, что для несуществующей книги возвращается None
    def test_get_book_genre_book_not_exists_returns_none(self):
        collector = BooksCollector()
        # запрашиваем жанр книги, которой нет в коллекции
        # проверяем, что метод вернул None
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тесты для get_books_with_specific_genre
    
    # проверяем, что метод возвращает список книг с указанным жанром
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        # добавляем три книги
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Дюна')
        # устанавливаем жанры: две книги с жанром Ужасы, одна - Фантастика
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        # проверяем, что метод вернул обе книги жанра Ужасы
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Сияние']

    # проверяем, что если нет книг с указанным жанром, возвращается пустой список
    def test_get_books_with_specific_genre_no_books_returns_empty_list(self):
        collector = BooksCollector()
        # запрашиваем книги жанра Фантастика в пустой коллекции
        # проверяем, что метод вернул пустой список
        assert collector.get_books_with_specific_genre('Фантастика') == []

    # проверяем, что для невалидного жанра возвращается пустой список
    def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(self):
        collector = BooksCollector()
        # добавляем книгу с жанром Фантастика
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        # запрашиваем книги с жанром, которого нет в списке genre
        # проверяем, что метод вернул пустой список
        assert collector.get_books_with_specific_genre('Драма') == []

    # Тесты для get_books_genre
    
    # проверяем, что метод возвращает корректный словарь books_genre
    def test_get_books_genre_returns_correct_dictionary(self):
        collector = BooksCollector()
        # добавляем книгу и устанавливаем ей жанр
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        # проверяем, что метод вернул правильный словарь
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    # Тесты для get_books_for_children
    
    # проверяем, что метод не включает книги с возрастным рейтингом
    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        # добавляем три книги
        collector.add_new_book('Оно')
        collector.add_new_book('Шрек')
        collector.add_new_book('Шерлок Холмс')
        # устанавливаем жанры: Ужасы и Детективы - с возрастным рейтингом, Мультфильмы - без
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        # проверяем, что метод вернул только книгу без возрастного рейтинга
        assert collector.get_books_for_children() == ['Шрек']

    # проверяем, что книги без жанра не попадают в список для детей
    def test_get_books_for_children_books_without_genre_not_included(self):
        collector = BooksCollector()
        # добавляем книгу без жанра
        collector.add_new_book('Книга без жанра')
        # добавляем книгу с детским жанром
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        # проверяем, что в список попала только книга с установленным детским жанром
        assert collector.get_books_for_children() == ['Шрек']

    # проверяем, что для пустой коллекции возвращается пустой список
    def test_get_books_for_children_empty_collection_returns_empty_list(self):
        collector = BooksCollector()
        # запрашиваем книги для детей из пустой коллекции
        # проверяем, что метод вернул пустой список
        assert collector.get_books_for_children() == []

    # Тесты для add_book_in_favorites
    
    # проверяем, что можно добавить книгу в избранное
    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()
        # добавляем книгу в коллекцию
        collector.add_new_book('Дюна')
        # добавляем книгу в избранное
        collector.add_book_in_favorites('Дюна')
        # проверяем, что книга появилась в избранном
        assert 'Дюна' in collector.get_list_of_favorites_books()

    # проверяем, что одну книгу нельзя добавить в избранное дважды
    def test_add_book_in_favorites_same_book_twice_added_once(self):
        collector = BooksCollector()
        # добавляем книгу в коллекцию
        collector.add_new_book('Дюна')
        # пытаемся добавить книгу в избранное два раза
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        # проверяем, что в избранном только одна книга
        assert len(collector.get_list_of_favorites_books()) == 1

    # проверяем, что нельзя добавить в избранное книгу, которой нет в коллекции
    def test_add_book_in_favorites_book_not_in_collection_not_added(self):
        collector = BooksCollector()
        # пытаемся добавить в избранное книгу, которой нет в books_genre
        collector.add_book_in_favorites('Несуществующая книга')
        # проверяем, что избранное осталось пустым
        assert len(collector.get_list_of_favorites_books()) == 0

    # Тесты для delete_book_from_favorites
    
    # проверяем, что можно удалить книгу из избранного
    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        # добавляем книгу в коллекцию и в избранное
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        # удаляем книгу из избранного
        collector.delete_book_from_favorites('Дюна')
        # проверяем, что книги нет в избранном
        assert 'Дюна' not in collector.get_list_of_favorites_books()

    # проверяем, что удаление книги, которой нет в избранном, не вызывает ошибку
    def test_delete_book_from_favorites_book_not_in_favorites_no_error(self):
        collector = BooksCollector()
        # добавляем книгу только в коллекцию
        collector.add_new_book('Дюна')
        # пытаемся удалить книгу из избранного, хотя ее там нет
        collector.delete_book_from_favorites('Дюна')
        # проверяем, что избранное осталось пустым и ошибки не возникло
        assert len(collector.get_list_of_favorites_books()) == 0

    # Тесты для get_list_of_favorites_books
    
    # проверяем, что метод возвращает корректный список избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        # добавляем две книги в коллекцию
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        # добавляем обе книги в избранное
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Оно')
        # проверяем, что метод вернул список с обеими книгами
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Оно']

    # проверяем, что для пустого избранного возвращается пустой список
    def test_get_list_of_favorites_books_empty_favorites_returns_empty_list(self):
        collector = BooksCollector()
        # запрашиваем список избранного, не добавив ни одной книги
        # проверяем, что метод вернул пустой список
        assert collector.get_list_of_favorites_books() == []