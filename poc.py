import requests
from bs4 import BeautifulSoup
import webbrowser
import sys
def main():
	serias = raw_input("enter searias : ")
	site =  "pirateproxy.one"
	query = "%20".join(serias.split(" "))
	url = "https://{site}/search/{query}/0/99/0".format(site=site, query=query)
	print "trying {0}".format(url)
	results_page = requests.get(url)
	print "code = {0}".format(results_page.status_code)
	save_html(results_page, "result.html")	
	soup = BeautifulSoup(results_page.text)
	links = soup.findAll('a')
	for link in links:
		if site in links:
			print link


def save_html(result_poge, file_name):
	with open(file_name, "wb") as html_file:
		for character in str(result_poge.text):
			html_file.write(character)





if __name__ == "__main__":
	main()
