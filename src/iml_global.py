import sys
import datetime
sys.path.insert(0,'./')
sys.path.insert(0,'./crawlers')

def today():
	now = datetime.datetime.now()
	date = now.strftime("%Y-%m-%d %H:%M:%S")
	return date
def mday(day):
	now = datetime.datetime.now() - datetime.timedelta(days = day)
	date = now.strftime("%Y-%m-%d %H:%M:%S")

	return date
def date_format(date_str):
	if len(date_str) == 10:
		return date_str + " 00:00:00"

def domain(url):
	return url.split('/')[0] + '//' + url.split('/')[2]