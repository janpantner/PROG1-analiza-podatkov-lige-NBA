import orodja
import re

# url: 'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'

START_YEAR = 1980 # First year with 3pts
END_YEAR = 2022 # Currently last finished season


def shrani_sezono_v_html(year, vsili_prenos=False):
    url = f'https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html'
    html_datoteka = f'per_game{year}.html'
    orodja.shrani_spletno_stran(url, html_datoteka, vsili_prenos)
    return None

def poisci_igralce(ime_datoteke):
    with open(ime_datoteke, 'r', encoding='utf-8') as f:
        vsebina = f.read()

    #rx = re.compile(r'<tr class=\"(.)*?</tr>', flags=re.DOTALL)
    rx = re.compile(r'''data-stat="ranker" csk="(.)*?</tr''')
    igralci = re.findall(rx, vsebina)
    return igralci

def statistika_igralca(igralec):
    pass

#with open('per_game1980.html', 'r', encoding='utf-8') as f:
#    vsebina = f.read()
#
#with open('test', 'w', encoding='utf-8') as dat:
#    dat.write(vsebina)

#with open('per_game1980.html', 'r', encoding='utf-8') as f:
#        vsebina = f.read()
#
#    #rx = re.compile(r'<tr class=\"(.)*?</tr>', flags=re.DOTALL)
#rx = re.compile(r'''data-stat="ranker" csk="(.)*?</tr''', re.DOTALL)
#igralci = re.findall(rx, vsebina)
    

def main(redownload=True, reparse=True):
    for year in range (START_YEAR, END_YEAR + 1): # spremeni
        shrani_sezono_v_html(year)
    


if __name__ == '__main__':
    main()