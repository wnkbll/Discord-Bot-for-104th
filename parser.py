import requests

from bs4 import BeautifulSoup

URL = 'https://www.battlemetrics.com/servers/arma3/13055598'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
           }


def get_html(url, params=None):
    """ 'requests.get(url, headers=HEADERS)' возвращает скрытый html-код по ссылке 'url', 'headers=HEADERS' позволяет
    нам передать 'user-agent' для того, чтобы сайт не подумал что запрос оправляется ботом, и избежать бана. """
    return requests.get(url, headers=HEADERS)


def get_content(html):
    """ Класс BeautifulSoap позволяет получить красивый html-код. Метод 'find' возвращает кусок дерева html-кода по
    искомому идентификатору и классу. Метод 'find_all' возвращает все элементы html-кода из дерева 'item' по
    идентификатору и классу, если он имеется. """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('table', class_='css-1y3vvw9')

    names = items.find_all('a', class_='css-zwebxb')
    times = items.find_all('time')

    return package_data(names, times)


def package_data(names, times):
    """ Класс 'zip' возвращает пары вида: "name из names", "time из times". Стоит заметить, что 'names' и 'times'
    пока что сырой html-код, соответственно 'name' и 'time' тоже являются сырым html-кодом. Метод 'get_text()'
    позволяет получить из кода читаемое значение типа 'str'. Проверяя вхождение подстроки '[104' в строку
    'name.get_text()', в изначально пустой массив 'players', методом 'append', добавляются словари формата
    {name: name.get_text(), 'time': time.get_text() }. В итоге, функция возвращает массив вида: [{},{},{},...]."""
    players = []

    for name, time in zip(names, times):
        if '[104' in name.get_text() or '[RC-104' in name.get_text():  # Вместо '[104' - любая искомая подстрока
            players.append({
                'name': name.get_text(),
                'time': time.get_text()
            })
    return players


def parse_main():
    """ Вызывает функцию 'get_html(URL)'. Если подключение по 'URL' прошло успешно, то 'html.status_code' возвращает
    занчение '200' типа 'integer', иначе возвращается номер ошибки. В случае успешного подключения вызывается функция
    'get_content(html.text)'. Метод 'text' позволяет получить html-код, без него html возвращает '<Response [id]>',
    где 'id' равен 'html.status_code', а html-код остаётся невидимым. """
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        return 'Error type =', html.status_code
