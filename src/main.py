import iml_global
from urls import urls
import warnings
from pprint import pprint
import json
#crawl_list
import wevity
import detizen

if __name__ == '__main__':
	warnings.filterwarnings("ignore")
	post_list = []
	print("start")
	for i in urls:
		print("\n# " + i + " Crawling...")
		code = i.split("_")[0]
		code += ".proc('" + urls[i] + "')"
		post_list += eval(code)
	with open("output/" + i + '.json', 'w') as outfile:
		json.dump(post_list, outfile)