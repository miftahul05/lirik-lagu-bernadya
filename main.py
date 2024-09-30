from time import sleep
import time
import sys

def print_lirik():
    line = [
        ("apa sudah ada kabar lain yang kau tunggu?",0.10),
        ("sudah adakah yang gantikan ku?",0.09),
        ("yang khawatirkan mu setiap waktu",0.07),
        ("yang cerita tentang apapun sampai hal-hal tak perlu",0.10),
        ]
    delays=[2, 2.3, 3.2, 1,] 
    
    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lirik()
            
        
        
        