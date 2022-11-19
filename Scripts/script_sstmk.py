import requests
import socket
from bs4 import BeautifulSoup

url = ('https://www.sstmk.ru')

response = requests.get(url)
if response.status_code == 200:
    print(f'Cайт {url} работает корректно!!!!')


def get_ip_hostname():
    hostname = 'www.sstmk.ru'
    return f'IP address: {socket.gethostbyname(hostname)}'


def get_data(url):
    headers = {"accept" : "*/*"}
    r = requests.get(url=url,headers=headers)

    with open("index.html", 'w',encoding="utf-8") as file:
        file.write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    numbers = soup.find('div',class_ ="phone-number")
    num = numbers.find('a').get("href")[5:]
    if len(num[:-1]) == 10:
        return print('8({0}{1}{2}){3}{4}{5}-{6}{7}-{8}{9}'.format(*[i for i in num if i.isdigit()][1:]))


def main():
    print(get_ip_hostname())
    get_data('https://www.sstmk.ru')

if __name__ == '__main__':
    main()

