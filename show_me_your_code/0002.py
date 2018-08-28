# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import random
import pymysql

def save_to_sql(id, code):
	db = pymysql.connect('localhost', 'root', '123456', 'python_test', charset='utf8')
	cursor = db.cursor()
#	cursor.execute('DROP TABLE IF EXISTS ACTIVE_KEY')
#	create_sql = '''
#	CREATE TABLE ACTIVE_KEY(
#			code_id  INT NOT NULL,
#	        code  VARCHAR(255),
#	        code_status  VARCHAR(255))'''
#	cursor.execute(create_sql)

	find_sql = 'SELECT * FROM ACTIVE_KEY WHERE code="%s"' % code
	if cursor.execute(find_sql) == 0:
		insert_sql = 'INSERT INTO ACTIVE_KEY(code_id, code) VALUES (%s, %s)'
		try:
			cursor.execute(insert_sql, (id, code))
			db.commit()
			print('%s : %s 添加成功。' % (id, code))
		except Exception as e:
			db.rollback()
			print('\033[1;31;47m%s : %s 添加失败！\033[0m %s' % (id, code, e))
	else:
		print('%s 已存在，更新中。' % code)
	cursor.close()
	db.close()

def main():
	choice = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
	id = 1
	while id < 201:
		code = ''
		code_sample = random.sample(choice, 10)
		for j in code_sample:
			code += j
		save_to_sql(id, code)
		id += 1

if __name__ == '__main__':
    main()