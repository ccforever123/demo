#Date Recorder Version: 1.0

import datetime
import json

def read_data():
	with open('data.json', encoding='utf-8') as f:
		dict = json.load(f)
		for item in dict:
			value_y = dict[item][:4]
			value_m = dict[item][4:6]
			value_d = dict[item][6:]
			print('%s : %s-%s-%s' % (item, value_y, value_m, value_d))
		return dict

def continue_write(dict):
	def input_data(dict):
		title = input('标题:')
		date = input('日期:')
		dict[title] = date
		with open('data.json', 'w') as f:
			f.write(json.dumps(dict))
	continue_write = (input('输入新数据?(Y/N):')).upper()
	if continue_write == 'Y':
		input_data(dict)
	elif continue_write == 'N':
		return None
	else:
		main()
	main()

def date_counter(dict):
	today = datetime.datetime.today()
	for item in dict:
		value_y = int(dict[item][:4])
		value_m = int(dict[item][4:6])
		value_d = int(dict[item][6:])
		counter = (today - datetime.datetime(value_y, value_m, value_d)).days
		print('%s 距今天已经过去 %s 天了' % (item, counter))

def main():
	birth_dict = read_data()
	continue_write(birth_dict)
	date_counter(birth_dict)

if __name__ == '__main__':
	print('--------START--------')
	main()
	print('---------END---------')










