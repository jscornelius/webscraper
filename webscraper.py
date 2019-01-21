from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



url = 'https://www.raeleeskitchen.com/recipes'
output = open('raeleeskitchen.txt','w')


browser = webdriver.Firefox()
browser.get(url)

def processRecipe():
	try:
		title = browser.find_element_by_class_name('BlogItem-title')
	except:
		return

	output.write("\n\n" + title.text.encode('utf8') + "\n")
	print(title.text)
	
	taglist = browser.find_elements_by_tag_name('p')
	for t in taglist:
		if (t.text == "By using this website, you agree to our use of cookies. We use cookies to provide you with a great experience and to help our website run effectively."):
			print("")
		else:
			output.write(t.text.encode('utf8') + "\n")
			print(t.text)

	browser.close()


def processPage():
	items = browser.find_elements_by_class_name('BlogList-item')
	for i in items:
		try:
			t = i.find_element_by_class_name('BlogList-item-image-link')
		except:
			return

		t.location_once_scrolled_into_view
		ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ALT).click(t).key_up(Keys.SHIFT).key_up(Keys.ALT).perform()

	for handle in browser.window_handles:
		if (handle != mainWindow):
			browser.switch_to.window(handle)
			browser.switch_to.window(browser.current_window_handle)
			time.sleep(2)
			processRecipe()


mainWindow = browser.window_handles[0]
processPage()

i = len(browser.window_handles)
print (i)

#for handle in browser.window_handles:
#	if (handle != mainWindow):
#		browser.switch_to.window(handle)
#		browser.switch_to.window(browser.current_window_handle)
#		time.sleep(2)
#		processRecipe()

browser.switch_to.window(mainWindow)
browser.switch_to.window(browser.current_window_handle)

nextpagelink = browser.find_element_by_class_name('BlogList-pagination-link')
nextpagelink.location_once_scrolled_into_view
nextpagelink.click()
processPage()

# close the browser and be done!
browser.close()
output.close()




