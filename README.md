Тесты для add_new_book
test_add_new_book_add_one_book — добавление одной новой книги, проверка что книга появилась в словаре
test_add_new_book_add_two_books — добавление двух разных книг
test_add_new_book_add_duplicate_book — попытка добавить уже существующую книгу (не должна дублироваться)
test_add_new_book_add_book_with_empty_name — попытка добавить книгу с пустым именем (не должна добавиться)
test_add_new_book_add_book_with_max_length_name — добавление книги с именем длиной ровно 40 символов (граничное значение, должна добавиться)
test_add_new_book_add_book_with_too_long_name — попытка добавить книгу с именем длиной 41+ символов (не должна добавиться)
Тесты для set_book_genre
test_set_book_genre_correct_genre — установка корректного жанра существующей книге
test_set_book_genre_incorrect_genre — попытка установить жанр, не входящий в список допустимых
test_set_book_genre_for_nonexistent_book — попытка установить жанр несуществующей книге
Тесты для get_book_genre
test_get_book_genre_correct_name — получение жанра существующей книги
test_get_book_genre_nonexistent_book — получение жанра для несуществующей книги (должно быть None)
test_get_book_genre_without_genre_set — получение жанра книги, которой жанр ещё не присвоен (пустая строка)
Тесты для get_books_with_specific_genre
test_get_books_with_specific_genre_one_book — получение списка книг по жанру, когда подходит одна книга
test_get_books_with_specific_genre_several_books — получение списка книг по жанру, когда подходит несколько книг
test_get_books_with_specific_genre_no_matches — получение списка книг по жанру, если ни одна не подходит (пустой список)
test_get_books_with_specific_genre_incorrect_genre — запрос по несуществующему жанру
Тесты для get_books_genre
test_get_books_genre_returns_dict — проверка, что метод возвращает весь словарь книг с жанрами
test_get_books_genre_empty_dict — проверка на пустом словаре
Тесты для get_books_for_children
test_get_books_for_children_only_children_genres — книги с "детскими" жанрами (Фантастика, Мультфильмы, Комедии) попадают в список
test_get_books_for_children_exclude_age_rated — книги с жанрами Ужасы/Детективы не попадают в список
test_get_books_for_children_without_genre — книги без установленного жанра не попадают в список
test_get_books_for_children_empty_list — если подходящих книг нет, возвращается пустой список
Тесты для add_book_in_favorites
test_add_book_in_favorites_add_one_book — добавление одной книги в избранное
test_add_book_in_favorites_add_duplicate — попытка добавить книгу дважды (не должна дублироваться)
test_add_book_in_favorites_nonexistent_book — попытка добавить несуществующую книгу в избранное
Тесты для delete_book_from_favorites
test_delete_book_from_favorites_existing_book — удаление книги, находящейся в избранном
test_delete_book_from_favorites_nonexistent_book — попытка удалить книгу, которой нет в избранном (без ошибок)
Тесты для get_list_of_favorites_books
test_get_list_of_favorites_books_correct_list — проверка корректности возвращаемого списка избранных книг
test_get_list_of_favorites_books_empty_list — проверка, что список пуст, если ничего не добавлено