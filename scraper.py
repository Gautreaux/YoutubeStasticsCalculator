#scrapes your past youtube history 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#TODO - replace most strings with formatted strings

if __name__ == "__main__":

    #initialize everything
    driver = webdriver.Chrome();
    driver.get("https://www.youtube.com/feed/history")
    input("Please log in and press any key once complete.\n")

    #NOTE - normally use document.body.scrollHeight to get doc height
    #   but for youtube, the HTML is configured differently and needs this
    lastScroll = driver.execute_script("return document.body.children[2].scrollHeight")

    stuckInstances = 0

    #do the scraping operation
    while True:
        driver.execute_script("window.scrollTo(0, document.body.children[2].scrollHeight);")

        #TODO - some form of exponential backoff
        time.sleep(1)

        nowheight = driver.execute_script("return document.body.children[2].scrollHeight")
        if(nowheight == lastScroll):
            stuckInstances+=1
            print("Stuck counter: " + str(stuckInstances))
            if(stuckInstances > 10):
                break
        else:
            stuckInstances = 0
            lastScroll = nowheight

    print("Finished scraping, logging to disk.")

    #create a timestamp
    nowTime = time.time()

    #select just the one element that contains all the videos watched
    selectedData = driver.find_element_by_id('contents')

    #dump the scraped data to the disk:
    with open("rawOutput."+str(nowTime)+".html", 'w', encoding='utf8') as f:
        f.write(driver.page_source)

    with open("selectedOutput."+str(nowTime)+".html", 'w',  encoding='utf8') as f:
        f.write(selectedData.get_attribute('outerHTML'))

    input("The scraping is concluded. Press any key to continue.")
    driver.close()