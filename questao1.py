import string 
import json
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mime_types = "application/pdf"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "/home/usuario/estagioIntuitiveCare")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True)
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar")
new_http = driver.find_element_by_class_name("item-page").find_element_by_tag_name('a').get_attribute("href")
driver.get(new_http)
pdf = driver.find_element_by_css_selector('table').find_element_by_tag_name('a').get_attribute("href")
driver.get(pdf)
driver.close()
