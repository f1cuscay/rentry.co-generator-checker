import random as r
import requests, sys, time
from string import ascii_letters, digits
from colorama import Fore, init
init()


typing_speed = 70
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/typing_speed)

def main():
	
	sucess = 0
	slow_type('\nmade by f1cuscay\n')
	howmany = int(input('Введите количество ссылок: '))
	
	with open('Valid.txt', 'w') as valid:
		
		while sucess != howmany:
			code = ''.join(r.sample(ascii_letters + digits, 5))
			link = f'https://rentry.co/{code}'
			resp = requests.get(link).text

			if '404 not found' not in resp:
				print(f'{Fore.LIGHTGREEN_EX} Valid{Fore.RESET}  | {link}')
				valid.write(f'{link}\n')
				sucess += 1
			else:
				print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {link}')

	print('\nВалидные ссылки сохранены в Valid.txt')
	valid.close()
	input()


if __name__ == '__main__':
	main()
