#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @brief convert decimal code to Hanming code
# @version 1.0
# @date 2018-08-13

def hanming(code):
	code = bin(int(code))
	code = str(code)[2:]
#	print('待生成数据码：%s' % code)
	while len(code) < 12:
		code = '0' + code
	code_list = list(code)
	code_1 = int(code_list[0]) ^ int(code_list[1]) ^ int(code_list[3]) ^ int(code_list[4]) ^ int(code_list[6]) ^ int(code_list[8]) ^ int(code_list[10]) ^ int(code_list[11])
	code_2 = int(code_list[0]) ^ int(code_list[2]) ^ int(code_list[3]) ^ int(code_list[5]) ^ int(code_list[6]) ^ int(code_list[9]) ^ int(code_list[10])
	code_4 = int(code_list[1]) ^ int(code_list[2]) ^ int(code_list[3]) ^ int(code_list[7]) ^ int(code_list[8]) ^ int(code_list[9]) ^ int(code_list[10])
	code_8 = int(code_list[4]) ^ int(code_list[5]) ^ int(code_list[6]) ^ int(code_list[7]) ^ int(code_list[8]) ^ int(code_list[9]) ^ int(code_list[10])
	code_16 = int(code_list[11])
	code_list.insert(0, str(code_1))
	code_list.insert(1, str(code_2))
	code_list.insert(3, str(code_4))
	code_list.insert(7, str(code_8))
	code_list.insert(15, str(code_16))
	hanming_code = ''.join(code_list)
	return hanming_code


def check_hanming(hanming_code):
	hanming_str = str(hanming_code)
	while len(hanming_str) < 17:
		hanming_str = '0'+hanming_str
	code_list = list(str(hanming_str))
	code_1 = int(code_list[0]) ^ int(code_list[2]) ^ int(code_list[4]) ^ int(code_list[6]) ^ int(code_list[8]) ^ int(code_list[10]) ^ int(code_list[12]) ^ int(code_list[14]) ^ int(code_list[16])
	code_2 = int(code_list[1]) ^ int(code_list[2]) ^ int(code_list[5]) ^ int(code_list[6]) ^ int(code_list[9]) ^ int(code_list[10]) ^ int(code_list[13]) ^ int(code_list[14])
	code_4 = int(code_list[3]) ^ int(code_list[4]) ^ int(code_list[5]) ^ int(code_list[6]) ^ int(code_list[11]) ^ int(code_list[12]) ^ int(code_list[13]) ^ int(code_list[14])
	code_8 = int(code_list[7]) ^ int(code_list[8]) ^ int(code_list[9]) ^ int(code_list[10]) ^ int(code_list[11]) ^ int(code_list[12]) ^ int(code_list[13]) ^ int(code_list[14])
	code_16 = int(code_list[15]) ^ int(code_list[16])
	checksum_list = [str(code_16), str(code_8), str(code_4), str(code_2), str(code_1)]
	code_checksum = int(''.join(checksum_list), 2)
	print('checksum={}'.format(code_checksum))
	try:
		if code_checksum != 0:
			if code_list[code_checksum-1] == '0':
				code_list[code_checksum-1] = '1'
			else:
				code_list[code_checksum-1] = '0'
	except Exception as e:
		if e == 'list index out of range':
			print(e)
	code = code_list[2] + code_list[4] + code_list[5] + code_list[6] + code_list[8] + code_list[9] + code_list[10]\
	       + code_list[11] + code_list[12] + code_list[13] + code_list[14] + code_list[16]
	return int(code, 2)


def main():
	select = input('您需要编码还是解码（编码0，解码1：')
	if select == '0':
		code = int(input('请输入待编码数据（0~4095）:'))
		hanming_code = hanming(code)
		print('已生成汉明码：%s' % hanming_code)
	else:
		hanming_code_2 = input('请输入待验证汉明码:')
		print('待验证汉明码：%s' % hanming_code_2)
		re_code = check_hanming(hanming_code_2)
		print('已还原数据码：%s' % re_code)


if __name__ == '__main__':
	main()
