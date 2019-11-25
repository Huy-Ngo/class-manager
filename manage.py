from random import shuffle
from json import load
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--random', type=int, default=0)

args = parser.parse_args()


def gen_9_filter(student):
	if student['student-id'].split('-')[0] != 'BI9':
		return False
	else:
		return True


with open('./data/student-list.json', encoding='utf-8') as f:
	students = load(f)
	students = filter(gen_9_filter, students)
	students = list(students)

if args.random > 0:
	size = args.random
	shuffle(students)
	chosen_ones = students[:size]
	for i in range(size):
		surname = chosen_ones[i]["surname"]
		name = chosen_ones[i]["name"]
		std_id = chosen_ones[i]["student-id"]
		print(f'{i+1}. {std_id} \t {surname} {name}')
else:
	print('No task.')

# TODO:
# 1. Write tasks as functions
# 2. Implement grade calculation
