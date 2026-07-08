

# =============================
# Модуль 1: Конфигурация и локализация
# =============================

LANGUAGES = {
    "en": {
        "welcome": "Welcome to the Movie Finder!",
        "menu": "\nChoose an option:\n1 - Search by keyword\n2 - Search by genre and year\n3 - View most popular queries\n4 - Exit\nYour choice: ",
        "enter_keyword": "Enter a title keyword (in English): ",
        "enter_genre": "Enter genre (Action, Animation, Children, Classics, Comedy, Documentary, Drama, Family, Foreign, Games, Horror, Music, New, Sci-Fi, Sports, Travel): ",
        "enter_year": "Enter release year (1990-2025): ",
        "found_results": "Found {count} movies. Showing first 10:",
        "save_prompt": "Do you want to save all results to a CSV file? (yes/no): ",
        "file_saved": "Results saved to 'search_results.csv'.",
        "invalid_command": "Invalid choice. Please select 1–4.",
        "top_queries": "Most popular search queries:",
        "select_language": "Choose language / Выберите язык / Sprache wählen (en/ru/de): ",
        "input_error": "Input error. Try again.",
        "db_error": "Database connection error.",
        "exit": "Exiting the program. Goodbye!"
    },
    "ru": {
        "welcome": "Добро пожаловать в Поиск Фильмов!",
        "menu": "\nВыберите опцию:\n1 - Поиск по ключевому слову\n2 - Поиск по жанру и году\n3 - Популярные запросы\n4 - Выход\nВаш выбор: ",
        "enter_keyword": "Введите ключевое слово названия(на английском): ",
        "enter_genre": "Введите жанр (Action, Animation, Children, Classics, Comedy, Documentary, Drama, Family, Foreign, Games, Horror, Music, New, Sci-Fi, Sports, Travel): ",
        "enter_year": "Введите год выхода фильма (1990-2025): ",
        "found_results": "Найдено {count} фильмов. Показываю первые 10:",
        "save_prompt": "Сохранить все результаты в CSV файл? (yes/no): ",
        "file_saved": "Результаты сохранены в 'search_results.csv'.",
        "invalid_command": "Неверный выбор. Введите число от 1 до 4.",
        "top_queries": "Самые популярные поисковые запросы:",
        "select_language": "Choose language / Выберите язык / Sprache wählen (en/ru/de): ",
        "input_error": "Ошибка ввода. Попробуйте снова.",
        "db_error": "Ошибка подключения к базе данных.",
        "exit": "Выход из программы. До свидания!"
    },
    "de": {
        "welcome": "Willkommen beim Filmsucher!",
        "menu": "\nWählen Sie eine Option:\n1 - Nach Stichwort suchen\n2 - Nach Genre und Jahr suchen\n3 - Beliebte Suchanfragen anzeigen\n4 - Beenden\nIhre Wahl: ",
        "enter_keyword": "Geben Sie ein Titelschlüsselwort ein (auf Englisch): ",
        "enter_genre": "Geben Sie das Genre ein (Action, Animation, Children, Classics, Comedy, Documentary, Drama, Family, Foreign, Games, Horror, Music, New, Sci-Fi, Sports, Travel): ",
        "enter_year": "Geben Sie das Erscheinungsjahr ein (1990-2025): ",
        "found_results": "{count} Filme gefunden. Erste 10 werden angezeigt:",
        "save_prompt": "Möchten Sie alle Ergebnisse in eine CSV-Datei speichern? (yes/no): ",
        "file_saved": "Ergebnisse wurden in 'search_results.csv' gespeichert.",
        "invalid_command": "Ungültige Wahl. Bitte wählen Sie zwischen 1 und 4.",
        "top_queries": "Beliebteste Suchanfragen:",
        "select_language": "Choose language / Выберите язык / Sprache wählen (en/ru/de): ",
        "input_error": "Eingabefehler. Bitte erneut versuchen.",
        "db_error": "Datenbankverbindungsfehler.",
        "exit": "Programm wird beendet. Auf Wiedersehen!"
    }
}

COLUMN_HEADERS = {
    "en": ["Title", "Year", "Genre"],
    "ru": ["Название", "Год", "Жанр"],
    "de": ["Titel", "Jahr", "Genre"]
}

