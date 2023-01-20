

from bs4 import BeautifulSoup
import requests
from PIL import Image
from selenium import webdriver
import time
from datetime import datetime as d
from selenium.webdriver.common.by import By
import io
import os



#setting up the variables
PATH = "E:\\HARDHAT PROJECTS\\chromedriver.exe" #put the location of your chromedriver.exe here
WebDR = webdriver.Chrome(PATH)

def downloadingImageFromURLs(download_path, url, file_name):
	try:
		time = d.now()
		current_time = time.strftime('%H:%M:%S')
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)



		file_path = download_path + file_name

		with open(file_path, 'wb') as f:
			if image.height > 640 or image.width > 640:
				image.save(f, 'JPEG')
		print("download Successful")
	except Exception as e:
		print('FAILED -', e)





#this function is modelled to get the links/URLs of the images from the google images page


def selectingURLs(WebDR, delay, max_images,url):


	def SCROLLINGDOWN(WebDR):
		WebDR.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	#url = "https://www.google.com/search?q=m1a1+abram+tanks+in+war&rlz=1C1GCEA_enPK974PK974&sxsrf=AJOqlzUhIqImk7cTond6Obv3IfDJLlCIkQ:1674028707923&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj64urz0tD8AhXDCOwKHZh2DicQ_AUoAXoECAEQAw&biw=1536&bih=722&dpr=1.25"
	url = url
	WebDR.get(url)

	pic_links = set()
	invalid = 0

	while len(pic_links) + invalid < max_images:
		SCROLLINGDOWN(WebDR)

		thumbnails_of_pics = WebDR.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails_of_pics[len(pic_links) + invalid:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = WebDR.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in pic_links:
					max_images += 1
					invalid += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					pic_links.add(image.get_attribute('src'))
					print(f"Found {len(pic_links)}")
	return pic_links





if __name__ == '__main__':

	### search the required matrial on google images and then copy paste the url here

	#g_urls = ['https://yandex.com/images/search?text=m1%20abrams%20in%20action']
	g_urls = ['https://www.google.com/search?q=m1+abram+tanks+in+action+1000+images&tbm=isch&ved=2ahUKEwj33Pe0g9P8AhVClScCHcwMDwkQ2-cCegQIABAA&oq=m1+abram+tanks+in+action+1000+images&gs_lcp=CgNpbWcQAzoECCMQJ1DOA1jwKGDaLGgAcAB4AIABmgKIAZkXkgEEMi0xM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=8OXIY_ekMsKqnsEPzJm8SA&bih=712&biw=767&rlz=1C1GCEA_enPK974PK974']
	#g_urls = ['https://www.google.com/search?q=m1+abram+tanks+in+action&rlz=1C1GCEA_enPK974PK974&sxsrf=AJOqlzUiIMTc1F4cV1eph3MBu6NVyH0uDA:1674110446364&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiyjeGzg9P8AhVUYqQEHStJDo4Q_AUoAXoECAEQAw&biw=767&bih=712&dpr=1.25']
	#g_urls = ['https://www.google.com/search?q=m1+abram+tanks+in+war&hl=EN&tbm=isch&sxsrf=AJOqlzUdjbMdI5toXFksw920N625pUceww%3A1674107844154&source=hp&biw=767&bih=712&ei=w9vIY4blOIKwqtsP0YGDyAY&iflsig=AK50M_UAAAAAY8jp1MemKWIzEHaN2CYixK_Cq0a1KTIA&oq=m1+a&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6CAgAEIAEELEDOggIABCxAxCDAVC2BFiuEmDOHmgBcAB4AIAB5gGIAdYGkgEFMC4xLjOYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img']
	label = ['m1_abram_tanks'] #change name of the label according to ur preferences


	if len(g_urls) != len(label):
		raise ValueError('the lenght of the url list does not match the list')


	#pic_path = 'E:\m1a1 tanks yandex/'
	pic_path = 'E:\m1a1 abram tanks/'

	for l in label:
		if not os.path.exists(pic_path + l):
			print(f'making dir: {str(l)}')
			os.makedirs(pic_path + l)

	for url_curr,l in zip(g_urls, label):
		urls = selectingURLs(WebDR, 0.1, 5,url_curr)
		for i, url in enumerate(urls):
			downloadingImageFromURLs(download_path='E:/TANKS_TEST/', url = url, file_name = str(i+1)+ '.jpg') #change ur download path
			##make sure you change the download path
	WebDR.quit()

#urls = selectingURLs(WebDR, 0.1, 3)

for i, url in enumerate(urls):
	downloadingImageFromURLs("E:\m1a1 abram tanks", url, str(i) + ".jpg")

WebDR.quit()





