import iml_global
from urls import urls
import warnings
from pprint import pprint

#crawl_list
import wevity

if __name__ == '__main__':
	warnings.filterwarnings("ignore")
	print("start")
	for i in urls:
		code = i.split("_")[0]
		code += ".proc('" + urls[i] + "')"
		post_list = eval(code)
		pprint(post_list)