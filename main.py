import selenium,sys,time,os
import requests
from time import gmtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

os.system('cls' if os.name == 'nt' else 'clear')

def time():
    current = '['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '
    return(current)

def log(text):
    livetime = time()
    print(livetime+text)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"./chromedriver", options=chrome_options)
home = os.path.expanduser('~')
website = ('https://www.chess.com/play/computer')

name_white_pieces = ['wp','wr','wn','wb','wq','wk']
name_black_pieces = ['bp','br','bn','bb','bq','bk']


def main(args_list):
    if "-h" in args_list or "--help" in args_list:
        import _help

def main():

    ascii = """
 ██████╗██╗  ██╗███████╗███████╗███████╗███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ███████║█████╗  ███████╗███████╗█████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
██║     ██╔══██║██╔══╝  ╚════██║╚════██║██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
╚██████╗██║  ██║███████╗███████║███████║███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
           """


    print(ascii)
    print("\nVersion v0.01")
    print("A cheat engine for Chess.com\n")

    class abv_white_pieces:
        pawns = 'wp'
        rooks = 'wr'
        knights = 'wn'
        bishops = 'wb'
        queen = 'wq'
        king = 'wk'

    class abv_black_pieces:
        pawns = 'bp'
        rooks = 'br'
        knights = 'bn'
        bishops = 'bb'
        queen = 'bq'
        king = 'bk'
    
    run()

def teamassign(): # to only be executed at the very beginning of a game
    global selfWhite 
    global enemyBlack 
    global selfBlack 
    global enemyWhite
    selfWhite = False
    enemyBlack = False
    selfBlack = False
    enemyWhite = False
    
    try:
        browser.find_elements_by_class_name("piece wr square-11")
        selfWhite = True
        enemyBlack = True
    except NoSuchElementException:
        selfBlack = True
        enemyWhite = True
    

    global coords_self_pieces
    global coords_enemy_pieces
    if selfWhite==True:
        class coords_self_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class coords_enemy_pieces: # consider coordinates as [x,y]
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []

    if selfBlack==True:
        class coords_self_pieces: # consider coordinates as [x,y]
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class coords_enemy_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []

def interpret():
    log('Begin reading pieces...')
    for x in range(8):
        for y in range(8):
            for w_piece in name_white_pieces:
                try: 
                    browser.find_elements_by_class_name("piece "+w_piece+" square-"+str(x)+str(y))
                    if w_piece == 'wp':
                        if selfWhite==True:
                            (coords_self_pieces.wp).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wp).append(int('{}{}'.format(x, y)))
                    elif w_piece == 'wr':
                        if selfWhite==True:
                            (coords_self_pieces.wr).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wr).append(int('{}{}'.format(x, y)))
                    elif w_piece == 'wn':
                        if selfWhite==True:
                            (coords_self_pieces.wn).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wn).append(int('{}{}'.format(x, y)))
                    elif w_piece == 'wb':
                        if selfWhite==True:
                            (coords_self_pieces.wb).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wb).append(int('{}{}'.format(x, y)))
                    elif w_piece == 'wq':
                        if selfWhite==True:
                            (coords_self_pieces.wq).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wq).append(int('{}{}'.format(x, y)))
                    elif w_piece == 'wk':    
                        if selfWhite==True:
                            (coords_self_pieces.wk).append(int('{}{}'.format(x, y)))
                        if selfBlack==True:
                            (coords_enemy_pieces.wk).append(int('{}{}'.format(x, y)))
                except NoSuchElementException:
                    pass

            for b_piece in name_black_pieces:
                try:    
                    browser.find_elements_by_class_name("piece "+b_piece+" square-"+str(x)+str(y))
                    if b_piece == 'bp':
                        if selfBlack==True:
                            (coords_self_pieces.bp).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.bp).append(int('{}{}'.format(x, y)))
                    elif b_piece == 'br':
                        if selfBlack==True:
                            (coords_self_pieces.br).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.br).append(int('{}{}'.format(x, y)))
                    elif b_piece == 'bn':
                        if selfBlack==True:
                            (coords_self_pieces.bn).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.bn).append(int('{}{}'.format(x, y)))
                    elif b_piece == 'bb':
                        if selfBlack==True:
                            (coords_self_pieces.bb).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.bb).append(int('{}{}'.format(x, y)))
                    elif b_piece == 'bq':
                        if selfBlack==True:
                            (coords_self_pieces.bq).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.bq).append(int('{}{}'.format(x, y)))
                    elif b_piece == 'bk':
                        if selfBlack==True:
                            (coords_self_pieces.bk).append(int('{}{}'.format(x, y)))
                        if selfWhite==True:
                            (coords_enemy_pieces.bk).append(int('{}{}'.format(x, y)))    
                except NoSuchElementException:
                    pass
    log('Finish reading pieces...')

def run():
    browser.get(website)
    input(time()+'Press enter when game started...')
    teamassign()
    interpret()

    if selfWhite==True:
        print('Your white pawns are placed at: '+str(coords_self_pieces.wp))


if __name__ == "__main__":
    sys.exit(main())
