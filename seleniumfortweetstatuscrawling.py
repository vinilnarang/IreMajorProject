import time
import sys
import codecs
from twython import Twython, TwythonError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


uid = sys.argv[1]

APP_KEY = "g1sBsjOkO6Ik2xQLWjPweg";
APP_SECRET = "RFADPSzcGEaPW3E5qQHxBiscydxrQkjqS2oPYgIIOzI";
OAUTH_TOKEN = "2359516250-RUL2dUtGx8PQzn3PPufVL5ZZZgB2yOEQAfg40AP";
OAUTH_TOKEN_SECRET ="v1WbJ44YQ5WYPPgXNDxe9P7E3HNtqdVKSjw1l7gMYIobJ";
usr = ""
username = ""
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

output = twitter.lookup_user(user_id=uid)
data = output[0]
username=data["screen_name"]

browser = webdriver.Firefox()
#browser = webdriver.Chrome(executable_path="/home/santosh/Documents/chromedriver")
#browser.get("https://twitter.com/search?src=typd&q=%40BarackObama")
browser.get("https://twitter.com/"+username)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 50

while no_of_pagedowns:
	elem.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
	no_of_pagedowns-=1
#post_elems = browser.find_element_by_css_selector(".username.js-action-profile-name");

post_elems = browser.find_elements_by_class_name("js-tweet-text")

#post_elems = browser.find_elements_by_class_name("session[BarackObama]")

#post_elems = browser.find_elements_by_css_selector("[class='session[BarackObama]']")
f = codecs.open(username+".txt",'w',"UTF-8")
#f=open(username+".txt","w","UTF-8")
for post in post_elems:
	if post.text:
		f.write(post.text+"\n")
f.close()
  
browser.close()
