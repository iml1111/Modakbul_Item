import req
from iml_global import *

def proc(url):
	index = 0
	result = []
	while(True):
		print("## " + str(index) + " Page")
		temp, quit = get_posts(url + str(index))
		if quit or (not temp) or index > 40: break
		result += temp
		index += 10
	return result

def get_posts(url):
	result = []	
	soup = req.get_soup(url)
	soup = soup.select("a.jobtitle")
	for tag in soup:
		post_url = domain(url) + tag.attrs["href"]
		temp = {"title":tag.get_text(), 
				"date":today(),
				"content":"인디드 취업 정보",
				"url":post_url}
		if temp is None: return result, True
		print(temp['title'], temp['date'])
		result += [temp]
	return result, False