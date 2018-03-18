#!/usr/bin/env python3

import sys


def salary_calculator(id_salary):
	salary = 0
	tax = 0.00
	for _id,salary in id_salary.items():
		salary = salary * (1-0.165) - 3500
		if salary <= 0:
			tax = 0.00
			print("{}:{:.2f}".format(_id,tax))
	
		if salary > 0 and salary <=1500:
			tax = salary * 0.03
			print("{}:{:.2f}".format(_id,tax))

		if salary > 1500 and salary <= 4500:
			tax = salary * 0.1
			print("{}:{:.2f}".format(_id,tax))

		if salary > 4500 and salary <= 9000:
			tax = salary * 0.2
			print("{}:{:.2f}".format(_id,tax))

		if salary > 9000 and salary <= 35000:
			tax = salary * 0.25
			print("{}:{:.2f}".format(_id,tax))

		if salary >35000 and salary <= 55000:
			tax = salary * 0.3
			print("{}:{:.2f}".format(_id,tax))

		if salary > 55000 and salary <= 80000:
			tax = salary * 0.35
			print("{}:{:.2f}".format(_id,tax))

		if salary > 80000:
			tax = salary * 0.45
			print("{}:{:.2f}".format(_id,tax))

def split_salary(id_salary):
	
	
	return dict_id_salary

if __name__ == '__main__':
	
	try:
		if len(sys.argv) < 2:
			raise ValueError()
	except ValueError:		
		print("Parament Error")

		
	argvs = sys.argv[1:]
	print(argvs)
	dict_id_salary = {}
	for argv in argvs:
		list_id_salary = argv.split(":")
		print(list_id_salary)
		
		try:
			salary = int(list_id_salary[1])
			print(salary)

			if salary%1 != 0:
				raise ValueError()
		
			dict_id_salary[list_id_salary[0]] = list_id_salary[1]

		except ValueError:
			print("Parament Error")
	
	salary_calculator(dict_id_salary)
	

	



























































