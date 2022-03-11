import requests
from bs4 import BeautifulSoup
from os import getcwd
from os.path import join
from json import dump


def venezuela():
    url = 'https://es.wikipedia.org/wiki/ISO_3166-2:VE'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    states = soup.find('table').find('table')
    iso_codes =  [iso_code.string[:-1] for iso_code in states.find_all('th')]
    states = [state.string for state in states.find_all('a')]
    dictionary = (dict(zip(states, iso_codes)))
    create_json('./venezuela-states.json', dictionary)

def colombia():
    url = 'https://es.wikipedia.org/wiki/ISO_3166-2:CO'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    states = [soup.find('table').find('a').string]
    states.extend([a.string for a in soup.find('table').next_sibling.next_sibling.next_sibling.next_sibling.find_all('a')])
    iso_codes =  [iso_code.string for iso_code in soup.find_all('code')]
    dictionary = (dict(zip(states, iso_codes)))
    create_json('./colombia-states.json', dictionary)

def chile():
    url = 'https://es.wikipedia.org/wiki/ISO_3166-2:CL'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    states = [a.string for a in soup.find('table').find('tbody').find_all('a', title=True)]
    iso_codes = [tt.string for index, tt in enumerate(soup.find('table').find('tbody').find_all('tt')) if index % 2 == 0]
    dictionary = (dict(zip(states, iso_codes)))
    create_json('./chile-states.json', dictionary)

def create_json(path, dictionary):
    with open(join(getcwd(), path) , 'w') as file:
        dump(dictionary,file,indent=4, ensure_ascii=False)

def main():
    chile()

if __name__ == '__main__':
    main()