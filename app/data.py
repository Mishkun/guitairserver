codes = []
mobile_clients = {} 

from random import randrange 
def generate_code():
    code = str(randrange(9999+1))
    while code in codes:
        code = str(randrange(9999+1))
    codes.append(code)
    return code

song = []
bpm = 126
SONGFILE_NAME = 'C:\\Users\\Михаил\\Google Диск\\HACK-a-TRON\\NewGuitAir\\GuitAirServer\\app\\static\\highway_to_hell.txt'
def load_song():
    with open(SONGFILE_NAME) as songfile:
        song = [[int(x) for x in line.split()] for line in songfile]

    
