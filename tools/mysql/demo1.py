import pymysql

db = pymysql.connect('localhost', 'root', '123456', 'test')
cursor = db.cursor()

#create table = user
cursor.execute('drop table if EXISTS USER ')
sql="""CREATE TABLE IF NOT EXISTS `user` ( 
      `id` int(11) NOT NULL AUTO_INCREMENT, 
      `name` varchar(255) NOT NULL, 
      `age` int(11) NOT NULL, 
      PRIMARY KEY (`id`) 
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
cursor.execute(sql)

#insert data into 'user'
sql="""INSERT INTO user (name, age) VALUES
('test1', 11),
('test2', 21),
('test3', 31),
('test4', 41)"""

try:
	#run sql
	cursor.execute(sql)
	#commit to server
	db.commit()
	print('success')
except:
	#rollback if error
	print('error')
	db.rollback()

#update id=1
sql = """UPDATE user SET age=100 WHERE id=1"""
try:
	cursor.execute(sql)
	db.commit()
	print('success')
except:
	db.rollback()
	print('error')