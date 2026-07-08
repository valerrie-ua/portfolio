import csv
import os



# =============================
# Модуль 5: CSV-экспорт
# =============================

def generate_unique_filename(base_name="search_results", extension=".csv"):
    i = 0
    filename = f"{base_name}{extension}"
    while os.path.exists(filename):
        i += 1
        filename = f"{base_name}({i}){extension}"
    return filename


def export_to_csv(results):
    filename = generate_unique_filename()
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "year", "genre"])
        writer.writeheader()
        writer.writerows(results)