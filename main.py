import requests


def main():
    url_template = 'https://wttr.in/{}?mMnqT&lang=ru'
    url_svo = url_template.format('svo')
    url_cherepovets = url_template.format('Череповец')
    url_london = url_template.format('Лондон')

    response_svo = requests.get(url_svo)
    response_svo.raise_for_status()
    print(response_svo.text)

    response_cherepovets = requests.get(url_cherepovets)
    response_cherepovets.raise_for_status()
    print(response_cherepovets.text)

    response_london = requests.get(url_london)
    response_london.raise_for_status()
    print(response_london.text)


if __name__ == '__main__':
    main()
