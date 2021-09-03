import selenium,sys,time,os,re
import requests
from time import gmtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

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

def main(error):
    realtime_scan = False
    os.system('cls' if os.name == 'nt' else 'clear')
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
    if error is None:
        browser.get(website)
        input(timenow()+'Press enter when online game started...')
        infoextract()
        run()
    else:
        log(error)
        browser.get(website)
        input(timenow()+'Press enter when online game started...')
        infoextract()
        run()

def gamelivecheck():
    try:
        gamebuttons = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div[1]')
        if 'Rematch' in (gamebuttons.text):
            main('Game ended.')
        else:
            pass
    except NoSuchElementException:
        main("Unable to hook into game buttons. Are you sure the game has begun?")

def infoextract(): # to only be executed at the very beginning of a game
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
        if 'computer' in browser.current_url:
            main(f'Bot matches are currently {bcolors.UNDERLINE}unsupported.{bcolors.ENDC}')
        else:
            main('Online game not found.')
    
    try:
        flipcheck = browser.find_element_by_xpath('//*[@id="'+game_id+'"]').get_attribute("class")
        if flipcheck == 'board':
            selfWhite = True
            enemyBlack = True
        if flipcheck == 'board flipped':
            selfBlack = True
            enemyWhite = True
    except NoSuchElementException:
        main('Unable to hook into game board.')
    

    global current_coords_self_pieces
    global previous_coords_self_pieces
    global difference_coords_self_pieces
    global current_coords_enemy_pieces
    global previous_coords_enemy_pieces
    global difference_coords_enemy_pieces
    if selfWhite==True:
        class current_coords_self_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class previous_coords_self_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []

        class difference_coords_self_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class current_coords_enemy_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class previous_coords_enemy_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class difference_coords_enemy_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []


    if selfBlack==True:
        class current_coords_self_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class previous_coords_self_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []

        class difference_coords_self_pieces: # consider coordinates as (x,y)
            bp = []
            br = []
            bn = []
            bb = []
            bq = []
            bk = []
        
        class current_coords_enemy_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []
        
        class previous_coords_enemy_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []

        class difference_coords_enemy_pieces: # consider coordinates as (x,y)
            wp = []
            wr = []
            wn = []
            wb = []
            wq = []
            wk = []

    log('Game framework hooked, interpretting parameters...')
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

def opponentturncheck():
    opponentturn = True
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
            main('Unable to hook into game timer.')


def get_coords():

    if selfWhite==True:
        log(f'Reading {bcolors.UNDERLINE}normal{bcolors.ENDC} gameboard...')
        (previous_coords_self_pieces.wp).clear()
        (previous_coords_self_pieces.wr).clear()
        (previous_coords_self_pieces.wn).clear()
        (previous_coords_self_pieces.wb).clear()
        (previous_coords_self_pieces.wq).clear()
        (previous_coords_self_pieces.wk).clear()

        (previous_coords_enemy_pieces.bp).clear()
        (previous_coords_enemy_pieces.br).clear()
        (previous_coords_enemy_pieces.bn).clear()
        (previous_coords_enemy_pieces.bb).clear()
        (previous_coords_enemy_pieces.bq).clear()
        (previous_coords_enemy_pieces.bk).clear()

        (previous_coords_self_pieces.wp).extend((current_coords_self_pieces.wp).copy())
        (previous_coords_self_pieces.wr).extend((current_coords_self_pieces.wr).copy())
        (previous_coords_self_pieces.wn).extend((current_coords_self_pieces.wn).copy())
        (previous_coords_self_pieces.wb).extend((current_coords_self_pieces.wb).copy())
        (previous_coords_self_pieces.wq).extend((current_coords_self_pieces.wq).copy())
        (previous_coords_self_pieces.wk).extend((current_coords_self_pieces.wk).copy())

        (previous_coords_enemy_pieces.bp).extend((current_coords_enemy_pieces.bp).copy())
        (previous_coords_enemy_pieces.br).extend((current_coords_enemy_pieces.br).copy())
        (previous_coords_enemy_pieces.bn).extend((current_coords_enemy_pieces.bn).copy())
        (previous_coords_enemy_pieces.bb).extend((current_coords_enemy_pieces.bb).copy())
        (previous_coords_enemy_pieces.bq).extend((current_coords_enemy_pieces.bq).copy())
        (previous_coords_enemy_pieces.bk).extend((current_coords_enemy_pieces.bk).copy())



        (current_coords_self_pieces.wp).clear()
        (current_coords_self_pieces.wr).clear()
        (current_coords_self_pieces.wn).clear()
        (current_coords_self_pieces.wb).clear()
        (current_coords_self_pieces.wq).clear()
        (current_coords_self_pieces.wk).clear()

        (difference_coords_self_pieces.wp).clear()
        (difference_coords_self_pieces.wr).clear()
        (difference_coords_self_pieces.wn).clear()
        (difference_coords_self_pieces.wb).clear()
        (difference_coords_self_pieces.wq).clear()
        (difference_coords_self_pieces.wk).clear()

        (current_coords_enemy_pieces.bp).clear()
        (current_coords_enemy_pieces.br).clear()
        (current_coords_enemy_pieces.bn).clear()
        (current_coords_enemy_pieces.bb).clear()
        (current_coords_enemy_pieces.bq).clear()
        (current_coords_enemy_pieces.bk).clear()

        (difference_coords_enemy_pieces.bp).clear()
        (difference_coords_enemy_pieces.br).clear()
        (difference_coords_enemy_pieces.bn).clear()
        (difference_coords_enemy_pieces.bb).clear()
        (difference_coords_enemy_pieces.bq).clear()
        (difference_coords_enemy_pieces.bk).clear()
    
    if selfBlack==True:
        log(f'Reading {bcolors.UNDERLINE}flipped{bcolors.ENDC} gameboard...')
        (previous_coords_self_pieces.bp).clear()
        (previous_coords_self_pieces.br).clear()
        (previous_coords_self_pieces.bn).clear()
        (previous_coords_self_pieces.bb).clear()
        (previous_coords_self_pieces.bq).clear()
        (previous_coords_self_pieces.bk).clear()

        (previous_coords_enemy_pieces.wp).clear()
        (previous_coords_enemy_pieces.wr).clear()
        (previous_coords_enemy_pieces.wn).clear()
        (previous_coords_enemy_pieces.wb).clear()
        (previous_coords_enemy_pieces.wq).clear()
        (previous_coords_enemy_pieces.wk).clear()

        (previous_coords_self_pieces.bp).extend((current_coords_self_pieces.bp).copy())
        (previous_coords_self_pieces.br).extend((current_coords_self_pieces.br).copy())
        (previous_coords_self_pieces.bn).extend((current_coords_self_pieces.bn).copy())
        (previous_coords_self_pieces.bb).extend((current_coords_self_pieces.bb).copy())
        (previous_coords_self_pieces.bq).extend((current_coords_self_pieces.bq).copy())
        (previous_coords_self_pieces.bk).extend((current_coords_self_pieces.bk).copy())

        (previous_coords_enemy_pieces.wp).extend((current_coords_enemy_pieces.wp).copy())
        (previous_coords_enemy_pieces.wr).extend((current_coords_enemy_pieces.wr).copy())
        (previous_coords_enemy_pieces.wn).extend((current_coords_enemy_pieces.wn).copy())
        (previous_coords_enemy_pieces.wb).extend((current_coords_enemy_pieces.wb).copy())
        (previous_coords_enemy_pieces.wq).extend((current_coords_enemy_pieces.wq).copy())
        (previous_coords_enemy_pieces.wk).extend((current_coords_enemy_pieces.wk).copy())

        (current_coords_self_pieces.bp).clear()
        (current_coords_self_pieces.br).clear()
        (current_coords_self_pieces.bn).clear()
        (current_coords_self_pieces.bb).clear()
        (current_coords_self_pieces.bq).clear()
        (current_coords_self_pieces.bk).clear()

        (difference_coords_self_pieces.bp).clear()
        (difference_coords_self_pieces.br).clear()
        (difference_coords_self_pieces.bn).clear()
        (difference_coords_self_pieces.bb).clear()
        (difference_coords_self_pieces.bq).clear()
        (difference_coords_self_pieces.bk).clear()

        (current_coords_enemy_pieces.wp).clear()
        (current_coords_enemy_pieces.wr).clear()
        (current_coords_enemy_pieces.wn).clear()
        (current_coords_enemy_pieces.wb).clear()
        (current_coords_enemy_pieces.wq).clear()
        (current_coords_enemy_pieces.wk).clear()

        (difference_coords_enemy_pieces.wp).clear()
        (difference_coords_enemy_pieces.wr).clear()
        (difference_coords_enemy_pieces.wn).clear()
        (difference_coords_enemy_pieces.wb).clear()
        (difference_coords_enemy_pieces.wq).clear()
        (difference_coords_enemy_pieces.wk).clear()

    no_element_counter = 0
    pieces_counter = 0
    for i in range(1,40):
        try:
            retrieve_pieces = browser.find_element_by_xpath('//*[@id="'+game_id+'"]/div['+str(i)+']')
            selected_piece = retrieve_pieces.get_attribute("class")
            piece_type = selected_piece.split(' ')[2-1]
            piece_position = re.findall("\d+", selected_piece)[0]
            pieces_counter+=1
            if piece_type == 'wp':
                if selfWhite==True:
                    (current_coords_self_pieces.wp).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wp).append(','.join(piece_position))
            elif piece_type == 'wr':
                if selfWhite==True:
                    (current_coords_self_pieces.wr).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wr).append(','.join(piece_position))
            elif piece_type == 'wn':
                if selfWhite==True:
                    (current_coords_self_pieces.wn).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wn).append(','.join(piece_position))
            elif piece_type == 'wb':
                if selfWhite==True:
                    (current_coords_self_pieces.wb).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wb).append(','.join(piece_position))
            elif piece_type == 'wq':
                if selfWhite==True:
                    (current_coords_self_pieces.wq).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wq).append(','.join(piece_position))
            elif piece_type == 'wk':    
                if selfWhite==True:
                    (current_coords_self_pieces.wk).append(','.join(piece_position))
                if selfBlack==True:
                    (current_coords_enemy_pieces.wk).append(','.join(piece_position))
            if piece_type == 'bp':
                if selfBlack==True:
                    (current_coords_self_pieces.bp).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bp).append(','.join(piece_position))
            elif piece_type == 'br':
                if selfBlack==True:
                    (current_coords_self_pieces.br).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.br).append(','.join(piece_position))
            elif piece_type == 'bn':
                if selfBlack==True:
                    (current_coords_self_pieces.bn).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bn).append(','.join(piece_position))
            elif piece_type == 'bb':
                if selfBlack==True:
                    (current_coords_self_pieces.bb).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bb).append(','.join(piece_position))
            elif piece_type == 'bq':
                if selfBlack==True:
                    (current_coords_self_pieces.bq).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bq).append(','.join(piece_position))
            elif piece_type == 'bk':
                if selfBlack==True:
                    (current_coords_self_pieces.bk).append(','.join(piece_position))
                if selfWhite==True:
                    (current_coords_enemy_pieces.bk).append(','.join(piece_position))

        except (NoSuchElementException, IndexError):
            no_element_counter+=1
            if no_element_counter == 39:
                main('Unable to hook into game pieces.') 
            else:
                pass
    log(str(pieces_counter)+' pieces found.')

def playerturncheck():
    playerturn = True
    log('Waiting for your next turn...')
    while(True):
        prevselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-bottom"]/div/div[3]/span').text
        time.sleep(1.5)
        newselftime = browser.find_element_by_xpath('//*[@id="board-layout-player-bottom"]/div/div[3]/span').text
        if newselftime == prevselftime:
            break
        else:
            pass

def find_difference(a, b):
    a_list = a.split(",")
    b_list = b.split(",")
    a_x = int(a_list[0])
    a_y = int(a_list[1])
    b_x = int(b_list[0])
    b_y = int(b_list[1])
    return str(abs(a_x - b_x)) +','+ str(abs(a_y - b_y))


def differentiatepos():
    if selfWhite==True:
        try:
            for i in range((len(current_coords_self_pieces.wp))):
                (difference_coords_self_pieces.wp).append(find_difference(previous_coords_self_pieces.wp[i], current_coords_self_pieces.wp[i]))
        except IndexError:
            (difference_coords_self_pieces.wp).append('Currently Unavailable.')
    if selfBlack==True:
        try:
            for i in range((len(current_coords_self_pieces.bp))):
                (difference_coords_self_pieces.bp).append(find_difference(previous_coords_self_pieces.bp[i], current_coords_self_pieces.bp[i]))
        except IndexError:
            (difference_coords_self_pieces.bp).append('Currently Unavailable.')

def outputpawnpos():
    if selfWhite==True:
        print(' ')
        spaced('Your previous white pawns were placed at: '+str(previous_coords_self_pieces.wp))
        spaced('Your current white pawns are placed at: '+str(current_coords_self_pieces.wp))
        spaced('Your difference in moves amongst white pawns: '+str(difference_coords_self_pieces.wp))
        spaced("Enemy's previous black pawns were placed at: "+str(previous_coords_enemy_pieces.bp))
        spaced("Enemy's current black pawns are placed at: "+str(current_coords_enemy_pieces.bp))
        print(' ')
    if selfBlack==True:
        print(' ')
        spaced('Your previous black pawns were placed at: '+str(previous_coords_self_pieces.bp))
        spaced('Your current black pawns are placed at: '+str(current_coords_self_pieces.bp))
        spaced('Your difference in moves amongst black pawns: '+str(difference_coords_self_pieces.bp))
        spaced("Enemy's previous white pawns were placed at: "+str(previous_coords_enemy_pieces.wp))
        spaced("Enemy's current white pawns are placed at: "+str(current_coords_enemy_pieces.wp))
        print(' ')

def run():
    realtime_scan = True
    while(True):
        gamelivecheck()
        opponentturncheck()
        get_coords()
        differentiatepos()
        outputpawnpos()
        playerturncheck()

if __name__ == "__main__":
    sys.exit(main(None))