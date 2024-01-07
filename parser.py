import requests
from bs4 import BeautifulSoup

def parse_page(url,keyword):
    # Отправляем запрос на страницу
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при запросе страницы: {response.status_code}")
        return

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все блоки с указанным классом
    article_blocks = soup.find_all('h2', class_='tm-title tm-title_h2')

    # Извлекаем информацию из каждого блока
    for block in article_blocks:
        # Находим ссылку внутри блока
        link = block.find('a', class_='tm-title__link')['href']

        # Извлекаем текст подписи
        caption = block.find('span').text

        # Выводим результат
        if keyword.lower() in caption.lower():
            print(f"{caption}")
            print(f"https://habr.com{link}")
            print('')

# Использование
print('Введит ключевое слово или оставьте поле пустым чтобы спарсить всё.\n')
kw=input('> ')
if kw == '':
   kw = ' '

url = "https://habr.com/ru/feed/"
parse_page(url,kw)
for i in range(2, 50):
    url = "https://habr.com/ru/feed/page"+str(i)+"/"
    parse_page(url,kw)
