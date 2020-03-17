#scrapes your past youtube history

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#TODO - replace most strings with formatted strings
#TODO - add a timer to track how long this takes

if __name__ == "__main__":

    #initialize everything
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/feed/history")
    input("Please log in and press any key once complete.\n")

    start_time = time.time()

    with open("selectedOutput."+str(start_time)+".html", 'w',  encoding='utf8') as f:

        #NOTE - normally use document.body.scrollHeight to get doc height
        #   but for youtube, the HTML is configured differently and needs this
        lastScroll = driver.execute_script(
            "return document.body.children[2].scrollHeight")

        stuckInstances = 0

        #do the scraping operation
        while True:
            driver.execute_script("window.scrollTo(0, document.body.children[2].scrollHeight);")

            #TODO - some form of exponential backoff
            time.sleep(5)

            nowheight = driver.execute_script("return document.body.children[2].scrollHeight")

            if(nowheight == lastScroll):
                stuckInstances += 1
                print("Stuck counter: " + str(stuckInstances))
                if(stuckInstances > 5):
                    break
            else:
                #new data was loaded

                #find the relevant parts
                selectedData = driver.find_element_by_id('contents')
                f.write(selectedData.get_attribute('innerHTML'))
                #remove the part we just logged
                driver.execute_script("document.getElementById('contents').innerHTML = \"\"")


                stuckInstances = 0
                lastScroll = nowheight

    print("Scraping concluded successfully in " +
          str(time.time()-start_time-25)+" seconds.")
    driver.close()
