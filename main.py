import requests


def main():
    url_template = 'https://wttr.in/{}'
    payload = {"m": "",
               "M": "",
               "n": "",
               "q": "",
               "T": "",
               "lang": "ru"}
    locations = ('svo', 'Череповец', 'Лондон')

    for location in locations:
        url = url_template.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
