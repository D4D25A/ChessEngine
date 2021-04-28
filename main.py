import selenium,sys,time,os,re
import requests
from time import gmtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

os.system('cls' if os.name == 'nt' else 'clear')

def timenow():
    current = '['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '
    return(current)

def log(text):
    livetime = timenow()
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
    

    global current_coords_self_pieces
    global current_coords_enemy_pieces
    if selfWhite==True:
        class current_coords_self_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class current_coords_enemy_pieces: # consider coordinates as [x,y]
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []

    if selfBlack==True:
        class current_coords_self_pieces: # consider coordinates as [x,y]
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class current_coords_enemy_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []

def game_status():
    statusscan = True
    log('Waiting for player turn...')
    while(True):
        prevselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[3]/span').text
        time.sleep(1.5)
        newselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[3]/span').text
        if newselftime == prevselftime:
            pass
        else:
            break
    interpret()


def interpret():

    if selfWhite==True:
        (current_coords_self_pieces.wp).clear()
        (current_coords_self_pieces.wr).clear()
        (current_coords_self_pieces.wn).clear()
        (current_coords_self_pieces.wb).clear()
        (current_coords_self_pieces.wq).clear()
        (current_coords_self_pieces.wk).clear()

        (current_coords_enemy_pieces.bp).clear()
        (current_coords_enemy_pieces.br).clear()
        (current_coords_enemy_pieces.bn).clear()
        (current_coords_enemy_pieces.bb).clear()
        (current_coords_enemy_pieces.bq).clear()
        (current_coords_enemy_pieces.bk).clear()
    
    if selfBlack==True:
        (current_coords_self_pieces.bp).clear()
        (current_coords_self_pieces.br).clear()
        (current_coords_self_pieces.bn).clear()
        (current_coords_self_pieces.bb).clear()
        (current_coords_self_pieces.bq).clear()
        (current_coords_self_pieces.bk).clear()

        (current_coords_enemy_pieces.wp).clear()
        (current_coords_enemy_pieces.wr).clear()
        (current_coords_enemy_pieces.wn).clear()
        (current_coords_enemy_pieces.wb).clear()
        (current_coords_enemy_pieces.wq).clear()
        (current_coords_enemy_pieces.wk).clear()

    log('Begin reading pieces...')
    game_id = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[2]/captured-pieces').get_attribute("board-id")
    for i in range(1,33):
        retrieve_pieces = browser.find_element_by_xpath('//*[@id="'+game_id+'"]/div['+str(i)+']')
        selected_piece = retrieve_pieces.get_attribute("class")
        piece_type = selected_piece.split(' ')[2-1]
        piece_position = re.findall("\d+", selected_piece)
        if piece_type == 'wp':
            if selfWhite==True:
                (current_coords_self_pieces.wp).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wp).extend(piece_position)
        elif piece_type == 'wr':
            if selfWhite==True:
                (current_coords_self_pieces.wr).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wr).extend(piece_position)
        elif piece_type == 'wn':
            if selfWhite==True:
                (current_coords_self_pieces.wn).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wn).extend(piece_position)
        elif piece_type == 'wb':
            if selfWhite==True:
                (current_coords_self_pieces.wb).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wb).extend(piece_position)
        elif piece_type == 'wq':
            if selfWhite==True:
                (current_coords_self_pieces.wq).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wq).extend(piece_position)
        elif piece_type == 'wk':    
            if selfWhite==True:
                (current_coords_self_pieces.wk).extend(piece_position)
            if selfBlack==True:
                (current_coords_enemy_pieces.wk).extend(piece_position)
        if piece_type == 'bp':
            if selfBlack==True:
                (current_coords_self_pieces.bp).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.bp).extend(piece_position)
        elif piece_type == 'br':
            if selfBlack==True:
                (current_coords_self_pieces.br).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.br).extend(piece_position)
        elif piece_type == 'bn':
            if selfBlack==True:
                (current_coords_self_pieces.bn).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.bn).extend(piece_position)
        elif piece_type == 'bb':
            if selfBlack==True:
                (current_coords_self_pieces.bb).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.bb).extend(piece_position)
        elif piece_type == 'bq':
            if selfBlack==True:
                (current_coords_self_pieces.bq).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.bq).extend(piece_position)
        elif piece_type == 'bk':
            if selfBlack==True:
                (current_coords_self_pieces.bk).extend(piece_position)
            if selfWhite==True:
                (current_coords_enemy_pieces.bk).extend(piece_position)    
    log('Finish reading pieces...')
    log('Your white pawns are placed at: '+str(current_coords_self_pieces.wp))
    time.sleep(3) #temporary
    game_status()

def run():
    browser.get(website)
    input(timenow()+'Press enter when game started...')
    teamassign()
    game_status()

if __name__ == "__main__":
    sys.exit(main())
