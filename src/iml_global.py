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
def date_format(year, month, day, hour = "00", min = "00", sec = "00"):
	string = year + "-" + month + "-" + day
	string += " " + hour + ":" + min + ":" + sec
	return string

def domain(url):
	return url.split('/')[0] + '//' + url.split('/')[2]