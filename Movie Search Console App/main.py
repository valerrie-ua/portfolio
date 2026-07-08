import sys
from tabulate import tabulate

from localization import LANGUAGES, COLUMN_HEADERS
from db_utils import connect_db, search_by_keyword, search_by_genre_year
from log_utils import log_query, get_popular_queries
from csv_export import export_to_csv



# =============================
# Модуль 6: Взаимодействие с пользователем
# =============================


def display_results_table(results, lang):
    headers = COLUMN_HEADERS.get(lang, COLUMN_HEADERS["en"])
    rows = [[r['title'], r['year'], r['genre']] for r in results[:10]]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))


def main():
    print("\n" + "=" * 50)
    lang = input(LANGUAGES["en"]["select_language"]).strip().lower()
    if lang not in LANGUAGES:
        lang = "en"
    t = LANGUAGES[lang]

    print("\n" + "=" * 50)
    print(f"🎬 {t['welcome']} 🎬".center(50))
    print("=" * 50)

    movie_db = connect_db('X', 'X', 'X', 'X')
    if not movie_db:
        print(t["db_error"])
        return

    log_db = connect_db('X', 'X', 'X', 'X')
    if not log_db:
        print(t["db_error"])
        return

    movie_cursor = movie_db.cursor()
    log_cursor = log_db.cursor()

    while True:
        try:
            print("\n" + "-" * 50)
            print(t["menu"]
                .replace("1 -", "1 - 🔍")
                .replace("2 -", "2 - 🎞️")
                .replace("3 -", "3 - 📊")
                .replace("4 -", "4 - ❌"))

            choice = input().strip()

            if choice == "1":
                print()
                keyword = input(t["enter_keyword"]).strip()
                results = search_by_keyword(movie_cursor, keyword)
                log_query(log_cursor, log_db, f"keyword:{keyword}")

                print("\n" + t["found_results"].format(count=len(results)) + "\n")
                if results:
                    display_results_table(results, lang)
                    print()
                    save = input(t["save_prompt"]).strip().lower()
                    if save == "yes":
                        export_to_csv(results)
                        print(t["file_saved"])
                else:
                    print("¯\\_(ツ)_/¯ No results found.")

            elif choice == "2":
                print()
                genre = input(t["enter_genre"]).strip()
                year = input(t["enter_year"]).strip()
                if not year.isdigit():
                    print(t["input_error"])
                    continue
                results = search_by_genre_year(movie_cursor, genre, int(year))
                log_query(log_cursor, log_db, f"genre:{genre},year:{year}")

                print("\n" + t["found_results"].format(count=len(results)) + "\n")
                if results:
                    display_results_table(results, lang)
                    print()
                    save = input(t["save_prompt"]).strip().lower()
                    if save == "yes":
                        export_to_csv(results)
                        print(t["file_saved"])
                else:
                    print("¯\\_(ツ)_/¯ No results found.")

            elif choice == "3":
                queries = get_popular_queries(log_cursor)
                print("\n📊 " + t["top_queries"] + "\n")
                for q in queries:
                    print(f"{q['query_text']} - {q['count']}")

            elif choice == "4":
                print("\n" + t["exit"] + "\n")
                break

            else:
                print(t["invalid_command"])

        except Exception as e:
            print(t["input_error"])
            print("Debug error:", e)

    movie_db.close()
    log_db.close()




# =============================
# Запуск
# =============================

if __name__ == "__main__":
    main()



