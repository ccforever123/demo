#coding:utf-8
import requests
import re
import pymysql

def get_source(url):
	r =requests.get(url)
	r.encoding = r.apparent_encoding
	return r.text, r.url

def get_data(current_url):
	page = 1
	num = 1
	job_result = []
	r = requests.get(current_url)
	while r.status_code == 200:
		page_url = '?pageindex=%d&maprange=3&islocation=0' % page
		print('Page:' , page)
		url = current_url[:46] + page_url
		#print(url)
		r = requests.get(url)
		source = get_source(url)[0]
		reg_job_info = re.compile(r' <a class=\"boxsizing\" data-link=\"(.*?)\">.*?<div class=\"job-name fl \">(.*?)</div>.*? <div class=\"fl\">(.*?)</div>.*?<div class="comp-name fl">(.*?)</div>.*?<span class=\"ads\">(.*?)</span>.*?<div class=\"time fr\">(.*?)</div>.*?', re.S)
		job_info_list = reg_job_info.findall(source)
		if job_info_list != []:
			for job in job_info_list:
				job_result.append([num])
				for i in job:
					job_result[num-1].append(i)
				if '-' in job_result[num-1][3]:
					low, high = job_result[num - 1][3].split('-')
					if low[-1] == '千':
						low = int(float(low[:-1])*1000)
					elif low[-1] == '万':
						low = int(float(low[:-1])*10000)
					if high[-1] == '千':
						high = int(float(high[:-1])*1000)
					elif high[-1] == '万':
						high = int(float(high[:-1])*10000)
					job_result[num-1][3] = low
					job_result[num - 1].insert(4, high)
				else:
					job_result[num - 1].insert(4, job_result[num-1][3])
				save_to_sql(job_result[num-1])
				num+=1
#			for i in job_result:
#				print(i)
			page+=1
		else:
			break

def save_to_sql(job_result):
	job_id = job_result[0]
	link = 'https://m.zhaopin.com' + job_result[1]
	title = job_result[2]
	low = job_result[3]
	high = job_result[4]
	company = job_result[5]
	place = job_result[6]
	up_time = job_result[7]
	db = pymysql.Connect('localhost','root', '123456','test', charset="utf8")
	cursor = db.cursor()
	'''
	cursor.execute("DROP TABLE IF EXISTS job_list")

	create_sql = """CREATE TABLE job_list (
		         job_id  INT NOT NULL,
		         link  VARCHAR(255),
		         title  VARCHAR(255),
		         company  VARCHAR(255),
		         low  VARCHAR(255),
		         high  VARCHAR(255),
		         place  VARCHAR(255),
		         up_time  VARCHAR(255))"""
	cursor.execute(create_sql)
	'''
	find_sql = "SELECT * FROM job_list WHERE link=%s"
	if cursor.execute(find_sql, link) == 0:
		insert_sql = "INSERT INTO job_list VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		try:
			print(job_result)
			cursor.execute(insert_sql, (job_id, link, title, place, low, high, company, up_time))
			db.commit()
			#print('===%s 添加成功===' % job_result)
		except:
			db.rollback()
			print('===！！！%s 添加失败！！！===' % job_result)
	#else:
		#print('%s 已存在' % job_result)
		#cursor.close()
		#db.close()
		#return 1
	cursor.close()
	db.close()

def main():
	kw = '项目经理'
	url_head = 'https://m.zhaopin.com'
	request_url = '/searchjob/search?KeyWord=%s&JobType=&Industry=&pageIndex=1&isSchoolJob=0&Location=542&SF_2_100_32=2' % kw
	source, current_url = get_source(url_head+request_url)
	get_data(current_url)

if __name__ == '__main__':
    main()