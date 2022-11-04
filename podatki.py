import requests
import os
import re

START_YEAR = 1980 # First year with 3pts
END_YEAR = 2022 # Currently last finished season

regular_season_summary_directory = 'podatki/regular-season-summary'

def url_regular_season_summary(year):
    '''Vrne url povzetka sezone v danem letu.'''
    return f'https://www.basketball-reference.com/leagues/NBA_{year}.html'

def file_regular_season_summary(year):
    return f'rseasonsummary{year}.html'


def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Napaka pri povezovanju do:", url)
        return None
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        print("Napaka pri prenosu strani:", url)
        return None

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def save_frontpage(year, directory):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    text = download_url_to_string(url_regular_season_summary(year))
    save_string_to_file(text, directory, file_regular_season_summary(year))
    return None

#####################################################################

def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as file_in:
        return file_in.read()



def page_to_stats(page_content):
    rx = re.compile(r'''<div class="table_container current" id='''
                    r'''"div_per_game-team">(.)*?</div><div class'''
                    r'''="table_container" id="div_per_game-opponent">''',
                    flags=re.DOTALL)
    pass









########################################

def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    for year in range(START_YEAR, END_YEAR + 1):
        save_frontpage(year, regular_season_summary_directory)

# if __name__ == '__main__':
#     main()