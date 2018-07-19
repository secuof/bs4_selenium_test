from selenium import webdriver
from bs4 import BeautifulSoup
import sys


# Defind call webdriver
def get_webdriver():
	driver = webdriver.Chrome('/home/insignary/app/chromedriver')
	driver.implicitly_wait(6)
	return driver


def key_send(driver, url, elements):
	
	driver.get(url)

	for element in elements:
		(name, send_msg) = element
		try:
			found = driver.find_element_by_name(name)
		except:
			return (name, send_msg)


		driver.find_element_by_name(name).send_keys(send_msg)
	return None


if __name__ == '__main__':

	elements = [
	('id', 'Input your Naver PW'),
	('pw', 'Input the your PW'),
	]
	
	url = 'https://nid.naver.com/nidlogin.login'
	
	driver = get_webdriver()
	
	result = key_send(driver, url, elements)
	
	if result is not None:
		(name, send_msg) = result
		print('error', name, send_msg)
		sys.exit(1)
	else:
		driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
		print('success')
	






		


	

#def auth_naver(url):
## Input the Naver ID / PW and Login
#driver.get('https://nid.naver.com/nidlogin.login')
#driver.find_element_by_name('id').send_keys('insignary@naver.com')
#driver.find_element_by_name('pw').send_keys('1204office')
#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
#
#
##t = driver.find_elements_by_class_name('count')
## <strong class="count"><span class="num1">1<span class="bg"></span></span><span class="num2">2<span class="bg"></span></span><span class="num2">2<span class="bg"></span></span></strong>
##print(t)
#driver.get('https://analytics.naver.com/summary/dashboard.html')
#html = driver.page_source
#soup = BeautifulSoup(html, 'html.parser')
##print(soup.prettify())
##visit_count = soup.select('#visitorSummary > strong > span.num1')
#v_count = soup.find_all('strong', {'class':'count'})
#for v in v_count:
#	attrs = v.find_all('span')
#	s = ''
#	for att in attrs:
#		s += att.getText()
#	print (int(s))
## visit_count1 = soup.select('visitorSummary > strong')
#
#print(type(visit_count))
#print(visit_count)
# print(type(visit_count1))
# print(visit_count1)
# print()
#
# # for n in visit_count:
# #     print(n.text.strip())
