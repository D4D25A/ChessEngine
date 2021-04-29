import selenium,sys,time,os,re
import requests
from time import gmtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

os.system('cls' if os.name == 'nt' else 'clear')

class bcolors:
    HEADER = '\033[95m'
    CYAN = '\u001b[36m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    MAGENTA = '\u001b[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def timenow():
    current = '['+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'] '
    return(current)

def log(text):
    livetime = timenow()
    print(livetime+text)

def spaced(text):
    print('                      '+text)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"./chromedriver", options=chrome_options)
home = os.path.expanduser('~')
website = ('https://www.chess.com/play/online/')

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
    browser.get(website)
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
        global game_id
        game_id = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[2]/captured-pieces').get_attribute("board-id")
    except NoSuchElementException:
        run()
    
    try:
        flipcheck = browser.find_element_by_xpath('//*[@id="'+game_id+'"]').get_attribute("class")
        if flipcheck == 'board':
            selfWhite = True
            enemyBlack = True
        if flipcheck == 'board flipped':
            selfBlack = True
            enemyWhite = True
    except NoSuchElementException:
        run()
    

    global current_coords_self_pieces
    global previous_coords_self_pieces
    global current_coords_enemy_pieces
    global previous_coords_enemy_pieces
    if selfWhite==True:
        class current_coords_self_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class previous_coords_self_pieces: # consider coordinates as [x,y]
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
        
        class previous_coords_enemy_pieces: # consider coordinates as [x,y]
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
        
        class previous_coords_self_pieces: # consider coordinates as [x,y]
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
        
        class previous_coords_enemy_pieces: # consider coordinates as [x,y]
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []


def game_status():
    try:
        gameoverbuttons = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div[1]')
        if 'Rematch' in (gameoverbuttons.text):
            run()
        else:
            pass
    except NoSuchElementException:
        run()
    statusscan = True
    while(True):
        try: 
            prevopponenettime = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[3]/span').text
            time.sleep(1.5)
            newopponenttime = browser.find_element_by_xpath('//*[@id="board-layout-player-top"]/div/div[3]/span').text
            if newopponenttime == prevopponenettime:
                break
            else:
                pass
        except NoSuchElementException:
            run()
    process()


def process():

    if selfWhite==True:
        log(f'Reading {bcolors.UNDERLINE}normal{bcolors.ENDC} gameboard...')
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
        log(f'Reading {bcolors.UNDERLINE}flipped{bcolors.ENDC} gameboard...')
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

    try:
        for i in range(1,33):
            retrieve_pieces = browser.find_element_by_xpath('//*[@id="'+game_id+'"]/div['+str(i)+']')
            selected_piece = retrieve_pieces.get_attribute("class")
            piece_type = selected_piece.split(' ')[2-1]
            piece_position = re.findall("\d+", selected_piece)
            if piece_type == 'wp':
                if selfWhite==True:
                    (current_coords_self_pieces.wp).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wp).append(int(piece_position[0]))
            elif piece_type == 'wr':
                if selfWhite==True:
                    (current_coords_self_pieces.wr).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wr).append(int(piece_position[0]))
            elif piece_type == 'wn':
                if selfWhite==True:
                    (current_coords_self_pieces.wn).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wn).append(int(piece_position[0]))
            elif piece_type == 'wb':
                if selfWhite==True:
                    (current_coords_self_pieces.wb).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wb).append(int(piece_position[0]))
            elif piece_type == 'wq':
                if selfWhite==True:
                    (current_coords_self_pieces.wq).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wq).append(int(piece_position[0]))
            elif piece_type == 'wk':    
                if selfWhite==True:
                    (current_coords_self_pieces.wk).append(int(piece_position[0]))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wk).append(int(piece_position[0]))
            if piece_type == 'bp':
                if selfBlack==True:
                    (current_coords_self_pieces.bp).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bp).append(int(piece_position[0]))
            elif piece_type == 'br':
                if selfBlack==True:
                    (current_coords_self_pieces.br).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.br).append(int(piece_position[0]))
            elif piece_type == 'bn':
                if selfBlack==True:
                    (current_coords_self_pieces.bn).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bn).append(int(piece_position[0]))
            elif piece_type == 'bb':
                if selfBlack==True:
                    (current_coords_self_pieces.bb).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bb).append(int(piece_position[0]))
            elif piece_type == 'bq':
                if selfBlack==True:
                    (current_coords_self_pieces.bq).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bq).append(int(piece_position[0]))
            elif piece_type == 'bk':
                if selfBlack==True:
                    (current_coords_self_pieces.bk).append(int(piece_position[0]))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bk).append(int(piece_position[0]))   
    except NoSuchElementException:
        run() 
    if selfWhite==True:
        log('Your white pawns are placed at: '+str(current_coords_self_pieces.wp))
        log("Enemy's black pawns are placed at: "+str(current_coords_enemy_pieces.bp))
    if selfBlack==True:
        log('Your black pawns are placed at: '+str(current_coords_self_pieces.bp))
        log("Enemy's white pawns are placed at: "+str(current_coords_enemy_pieces.wp))
    turntaken = True
    log('Waiting for your next turn...')
    while turntaken==True:
        prevselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-bottom"]/div/div[3]/span').text
        time.sleep(1.5)
        newselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-bottom"]/div/div[3]/span').text
        if newselftime == prevselftime:
            break
        else:
            pass
    game_status()

def run():
    input(timenow()+'Press enter when game started...')
    teamassign()
    log('Game hooked, interpretting parameters...')
    if selfWhite==True:
        print(' ')
        spaced('Game-ID: '+game_id)
        spaced('Your pieces are: White')
        spaced('Enemy pieces are: Black')
        print(' ')
    if selfBlack==True:
        print(' ')
        spaced('Game-ID: '+game_id)
        spaced('Your pieces are: Black')
        spaced('Enemy pieces are: White')
        print(' ')
        log('Waiting for your next turn...')
    game_status()

if __name__ == "__main__":
    sys.exit(main())