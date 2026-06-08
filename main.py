import random
import string

class LinkShortener:
    def __init__(self):
        self.links = {}
      
    def _generate_code(self, length=4):
        """Метод для создания уникального случайного кода"""
        characters = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(characters, k=length))
            if code not in self.links:
                return code
    
    def add_link(self, long_url):
        """Добавление новой ссылки"""
        for code, url in self.links.items():
            if url == long_url:
                return code
                
        code = self._generate_code()
        self.links[code] = long_url
        return code
      
    def get_long_url(self, short_code):
        """Получение длинной ссылки по коду"""
        return self.links.get(short_code, None)

    def code_exists(self, short_code):
        """Проверка существования кода"""
        return short_code in self.links
   
    def print_all_links(self):
        """Вывод всех ссылок в исходном порядке""" 
        if not self.links:
            print("Хранилище пусто.")
            return
        print("\n--- Список всех ссылок ---")
        for code, url in self.links.items():
            print(f"{code} -> {url}")

    def print_sorted_links(self):
        """Вывод всех ссылок, отсортированных по короткому коду"""
        if not self.links:
            print("Хранилище пусто.")
            return
        print("\n--- Ссылки, отсортированные по короткому коду ---")
        sorted_pairs = sorted(self.links.items())
        for code, url in sorted_pairs:
            print(f"{code} -> {url}")

# Пример работы программы 
if __name__ == "__main__":
    shortener = LinkShortener()

    # Добавление ссылок
    code1 = shortener.add_link("https://www.osh.by/?p=102797")
    code2 = shortener.add_link("https://www.istockphoto.com/photos/low-cortisol")
    code3 = shortener.add_link("https://google.com")
    
    print(f"Добавлены ссылки. Созданные коды: {code1}, {code2}, {code3}")

    # Проверка существования и получение
    test_code = code1
    if shortener.code_exists(test_code):
        print(f"\nКод {test_code} существует! Исходная ссылка: {shortener.get_long_url(test_code)}")

    # Вывод всех ссылок
    shortener.print_all_links()

    # Вывод отсортированных ссылок
    shortener.print_sorted_links()
