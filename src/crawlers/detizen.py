import req
from iml_global import *
def proc(url):
	index = 1
	result = []
	while(True):
		print("## " + str(index) + " Page")
		temp, quit = get_posts(url + str(index))
		result += temp
		if quit: break
		index += 1
	return result

def get_posts(url):
	result = []	
	soup = req.get_soup(url)
	##########soup = soup.select("ul.basic-list > li")
	print(soup)
	for tag in soup:
		tag_ = tag.select("div.main-info > h4 > a")
		post_url = domain(url) + tag_.attrs['href']
		temp = get_post(post_url)
		if temp is None: return result, True
		print(temp['title'], temp['date'])
		result += [temp]
	return result, False

def get_post(url):
	soup = req.get_soup(url)
	title = soup.select("span.on")[0].get_text()
	date = soup.find("th", text = "기간").next_sibling.get_text()
	date = date_format(date.split("~ ")[1][:10])
	content = soup.select("ul.summary-info")[0].get_text()
	if today() > date: return None
	return {"title":title,
			"date":date,
			"content":content}