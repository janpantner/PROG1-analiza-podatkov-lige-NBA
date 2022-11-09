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

# <tr class="italic_text partial_table" ><th scope="row" class="right " data-stat="ranker" 
# csk="22" >22</th><td class="left " data-append-csv="bosweto01" data-stat="player" csk="Boswell,Tom" >
# <a href="/players/b/bosweto01.html">Tom Boswell</a></td><td class="center " data-stat="pos" >PF</td>
# <td class="right " data-stat="age" >26</td><td class="left " data-stat="team_id" >
# <a href="/teams/DEN/1980.html">DEN</a></td><td class="right " data-stat="g" >18</td>
# <td class="right iz" data-stat="gs" ></td><td class="right non_qual" data-stat="mp_per_g" >29.0</td>
# <td class="right non_qual" data-stat="fg_per_g" >4.0</td><td class="right non_qual" 
# data-stat="fga_per_g" >7.5</td><td class="right non_qual" data-stat="fg_pct" >.533</td>
# <td class="right non_qual" data-stat="fg3_per_g" >0.1</td><td class="right non_qual" 
# data-stat="fg3a_per_g" >0.1</td><td class="right non_qual" data-stat="fg3_pct" >.500</td>
# <td class="right non_qual" data-stat="fg2_per_g" >3.9</td><td class="right non_qual" 
# data-stat="fg2a_per_g" >7.4</td><td class="right non_qual" data-stat="fg2_pct" >.534</td>
# <td class="right non_qual" data-stat="efg_pct" >.537</td><td class="right non_qual" 
# data-stat="ft_per_g" >3.2</td><td class="right non_qual" data-stat="fta_per_g" >3.9</td>
# <td class="right non_qual" data-stat="ft_pct" >.829</td><td class="right non_qual" 
# data-stat="orb_per_g" >2.2</td><td class="right non_qual" data-stat="drb_per_g" >4.1</td>
# <td class="right non_qual" data-stat="trb_per_g" >6.3</td><td class="right non_qual" 
# data-stat="ast_per_g" >2.6</td><td class="right non_qual" data-stat="stl_per_g" >0.3</td>
# <td class="right non_qual" data-stat="blk_per_g" >0.4</td><td class="right non_qual" 
# data-stat="tov_per_g" >2.2</td><td class="right non_qual" data-stat="pf_per_g" >3.1</td>
# <td class="right non_qual" data-stat="pts_per_g" >11.3</td></tr>

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