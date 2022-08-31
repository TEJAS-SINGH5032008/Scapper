from selenium import webdriver
from bs4 import BeautifulSoap
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelus/Downloads/chromedriver")
browser.get(START_URL)
def scrape():
    headers = ["name", "distance", "radius", "mass"]
    planet_data= []
    for i in range(0. 428):
        soup = BeautifulSoap(browser.page_sourcxe, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "Brightest stars in univere"}):
            li_tags = ui_tags.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0
                temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                        except:
                            temp_list.append("")
                            planet_data.append(temp_list)
                            browser.fimd_element_by_xpah('//*[@id="prmary_column]/footer/div/div/div/nav/span[2]/a')
                            with open("scapper_1.csv","w")as f:
                                csvwriter = csv.writer(f)
                                csvwriter.writerow(headers)
                                csvwriter.writerows(planet_data)
                                scrape()
