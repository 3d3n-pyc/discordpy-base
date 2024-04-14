from datetime import datetime
import pytz
import json; debug = json.load(open('config.json', 'r', encoding='utf-8'))['debug']

class levels:
    info = '\x1b[34;1mINFO'
    debug = '\x1b[38;1mDEBUG'
    warning = '\x1b[33;1mWARNING'
    error = '\x1b[31mERROR'
    critical = '\x1b[41mCRITICAL'


def write(module, message, level):
    date = datetime.now(tz=pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d %H:%M:%S')
    
    levelName = level[7:]
    with open('data/logs.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{date} {levelName}     {module} {message}\n')
    
    if level == levels.debug and debug is False:
        return
    
    print(f'\x1b[30;1m{date} \x1b[0m{level}     \x1b[0m\x1b[35m{module} \x1b[0m{message}')