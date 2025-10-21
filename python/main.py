import winsound
import time
import sys

current_line : int = 0

def play_line(line: list) -> None:
    global current_line, code
    if len(line) == 0 or line[0].startswith('#') :
        return
    elif line[0] == 'sleep':
        time.sleep(float(line[1]))
    elif line[0] == 'beep':
        frequency : int = int(line[1])
        duration : int = int(line[2])
        winsound.Beep(max(37,min(frequency,32767)), duration)
    elif line[0] == 'jump':
        current_line = int(line[1]) - 2
    elif line[0] == 'for' :
        for i in range(int(line[1])) :
            arg0 : int = i * int(line[2]) + int(line[3])
            arg1 : int = i * int(line[4]) + int(line[5])
            arg2 : int = i * int(line[6]) + int(line[7])
            for j in range(int(line[8])) :
                play_line([str(word).strip() for word in code[current_line+j+1].replace('<arg0>', str(arg0)).replace('<arg1>', str(arg1)).replace('<arg2>', str(arg2)).split(' ') if word.strip() != '']) if code[current_line].strip() != ''else None
        current_line += int(line[8])

if len(sys.argv) > 1 :
    current_line : int = 0
    with open(sys.argv[1], 'r') as file :
        code = file.read().splitlines()
        while current_line < len(code) :
            line = code[current_line]
            play_line([str(word).strip() for word in line.split(' ') if word.strip() != '']) if line.strip() != ''else None
            current_line += 1            
else :
    while True :
        input_line : str = input('> ')
        if input_line.strip().lower() in ['exit', 'quit'] :
            break
        play_line([str(word).strip() for word in input_line.split(' ') if word.strip() != ''])
