from settings import length, lang, descr_now
from projects import names, link, m_description, creators, main_lang, category, category_score, categories_list
import language

import math
import time
import pyfiglet
import random

current_lang = getattr(language, lang)


names_now = []
pages = 0
max_pages = math.ceil(len(names)/length) - 1
more = 0

answer = ''

for i in range(length):
		if i + (max_pages)* length >= len(names):
			more += 1

def wh_pg():
	global answer, names_now

	print()
	print()

	# names_now = []
	fer_st = []
	

	def correct_random1():
		rand = names[random.randint(0, len(names)-1)]
		if category[names.index(rand)] == categories_list[category_score.index(max(category_score))]:
			names_now.append(rand)
		else:
			correct_random1()
	
	def correct_random2():
		unique_sorted = sorted(set(category_score), reverse=True)
		r_max = unique_sorted[1] if len(unique_sorted) > 1 else None

		rand = names[random.randint(0, len(names)-1)]
		if category[names.index(rand)] == categories_list[category_score.index(r_max)]:
			names_now.append(rand)
		else:
			correct_random2()


	if names_now == []: # Система рекомендаций
		for i in range(length*4):
			rand = names[random.randint(0, len(names)-1)]
			if rand in fer_st:
				rand = names[random.randint(0, len(names)-1)]
				fer_st.append(rand)
				names_now.append(rand)
			else:
				fer_st.append(rand)
				names_now.append(rand)
	elif pages == len(names_now)/length:
		for i in range(3):
			a = 0
			b = 0
			for i in range(length):
				if random.randint(0, 1) == 1 and a < 3:
					a += 1
					correct_random1()
				elif random.randint(0, 1) == 1 and b < 2:
					b += 1
					correct_random2()
				else:
					rand = names[random.randint(0, len(names)-1)]
					names_now.append(rand)



		wh_pg()

	# if pages == max_pages:
	# 	for i in range(length-more):
	# 			names_now.append(names[i + pages * length])
	# else:
	# 	for i in range(length):
	# 			names_now.append(names[i + pages * length])

	def how_print():
		if descr_now:
			print(f'{i+1}. {names_now[pages*5+i]} - {m_description[pages*5+i]}')
		else:
			print(f'{i+1}. {names_now[pages*5+i]}')

	if pages == max_pages:
		for i in range(length-more):
			how_print()
	else:
		for i in range(length):
			how_print()

	print()
	for i in range(3):
		print(current_lang[i+1])


	answer = input(current_lang[0])
	answer_page()



def answer_page():
	global answer, pages
 

	if answer == 'f':
		if pages != max_pages:
			a = []
			pages += 1

			for i in range(length):
				now_ind = names.index(names_now[int(i)])
				category_score[categories_list.index(category[now_ind])] -= 1

			print(category_score)
			wh_pg()

		else:
			print(current_lang[5])
			answer = input(current_lang[0])
			answer_page()
	elif answer == 'b':
		if pages >= 0:
			pages -= 1
			wh_pg()
		else:
			wh_pg()
	elif answer == 'h':
		start()
	elif answer in ('1','2','3','4','5','6','7','8','9','10'):
		if int(answer) > length:
			print(current_lang[4])
			answer = input(current_lang[0])
			answer_page()
		else:
			now_ind = names.index(names_now[int(answer)-1])
			category_score[categories_list.index(category[now_ind])] += 10

			description()
	else:
		print(current_lang[4])
		answer = input(current_lang[0])
		answer_page()


def description():
	global answer

	now_ind = names.index(names_now[int(answer)-1])

	try:

		print()
		print(names[now_ind] + ' - ' + link[now_ind])
		print(m_description[now_ind])
		print()
		print(current_lang[7] + creators[now_ind])
		print(current_lang[8] + main_lang[now_ind])
		print()

		input(current_lang[9])
		wh_pg()

	except IndexError:
		print(current_lang[6])

		answer = input(current_lang[0])
		answer_page()


def settings_rec():
	print(current_lang[17])
	time.sleep(1)
	settings()


def settings_lang():
	global ex_lanf
	answer = input(current_lang[18])

	if answer in language.ex_lanf:
		language.ex_lanf = answer
		print(current_lang[20])
		time.sleep(1)
		settings()
	else:
		print(current_lang[19])
		time.sleep(1)
		settings()


def page_insp():
	global length, more, descr_now, answer

	print()
	print('1. ' + current_lang[21])
	print('2. ' + current_lang[22])
	print(current_lang[2])
	answer = input(current_lang[0])

	if answer == '1':
		answer = input(current_lang[23])
		if int(answer) >= 3 and int(answer) <= 10:
			print(current_lang[24])
			length  = int(answer)

			more = 0
			for i in range(length):
				if i + (max_pages)* length >= len(names):
					more += 1
			time.sleep(1)
			page_insp()

		else:
			print(current_lang[25])
			time.sleep(1)
			page_insp()
	
	elif answer == '2':
		answer = input('(f/t 0/1) ' + current_lang[0])
		if answer == 'f' or answer == '0':
			descr_now = False
			print(current_lang[24])
			time.sleep(1)
			page_insp()
		elif answer == 't' or answer == '1':
			descr_now = True
			print(current_lang[24])
			time.sleep(1)
			page_insp()
		else:
			print(current_lang[25])
			time.sleep(1)
			page_insp()

	elif answer == 'b':
			settings()
	else:
			print(current_lang[25])
			time.sleep(1)
			page_insp()


def settings():
	print()
	for i in range(3):
		print(str(i+1) + '. ' + current_lang[i+14])
	print(current_lang[2])

	answer = input(current_lang[0])

	if answer == '1':
		settings_rec()
	elif answer == '2':
		settings_lang()
	elif answer == '3':
		page_insp()
	elif answer == 'b':
		start()
	else:
		print(current_lang[4])
		time.sleep(1)
		settings()


def start():
	global answer

	print(pyfiglet.figlet_format("GIT-TOK"))
	print()
	for i in range(3):
		print(str(i+1) + '. ' + current_lang[i+10])

	answer = input(current_lang[0])

	if answer == '1':
		wh_pg()
	elif answer == '2':
		settings()
	elif answer == '3':
		print(current_lang[13])
		time.sleep(2)

start()