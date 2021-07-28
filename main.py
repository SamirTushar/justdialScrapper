from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def try_finding_text_by_class_name(class_name,local_elem):
    try:
        return local_elem.find_element_by_class_name(class_name).text
    except:
        return ""




def change_to_csv(my_list,separator):
    fa = open("data1.txt", "w")
    # for x in range(len(my_list)):
    #     print(my_list[x]["name"] + separator + my_list[x]["rating"] + separator + my_list[x]["votes"])
    #     #print(x)

    keys = my_list[0].keys()



    for x in my_list:

        line = ""
        for key in keys:
            if line != "":
                line = line + separator + x[key]
            else:
                line = x[key]
        print(line)
        fa.write(line + '\n')
        # print(x["name"] + separator + x["rating"] + separator + x["votes"])
        #print(x)




driver = webdriver.Chrome(executable_path=r"C:\Users\intushars\PycharmProjects\pythonProject\Driver\chromedriver.exe")
driver.get("https://www.justdial.com")
assert "Justdial" in driver.title
elem = driver.find_element_by_id("srchbx")
elem.clear()
elem.send_keys("tyre retailer")
# elem.send_keys(Keys.RETURN)
time.sleep(5)
elem = driver.find_element_by_id("auto")
li_elem = elem.find_elements_by_tag_name("li")
time.sleep(3)
li_elem[0].find_element_by_tag_name("a").click()
time.sleep(5)

try:
    elem2 = elem
    elem = driver.find_element_by_xpath('//section[@class="rslwrp"]/div/ul')
    time.sleep(5)
except:
    elem = driver.find_element_by_id("srchbx")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)
body = driver.find_element_by_tag_name("body")
for x in range(4):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

time.sleep(5)


def resultsPage():
    body = driver.find_element_by_tag_name("body")
    for x in range(4):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

    time.sleep(5)
    elem = driver.find_element_by_xpath('//section[@class="rslwrp"]/div/ul')
    li_elem = elem.find_elements_by_tag_name("li")


    li_dict = []

    for li_item in li_elem:

        '''
        title_span = li_item.find_element_by_class_name("lng_cont_name")
        title_span1 = li_item.find_element_by_class_name("green-box")
        # title_span2 = li_item.find_element_by_class_name("rt_count lng_vote")
        title_span3 = li_item.find_element_by_class_name("adWidth cont_sw_addr")
        title_span4 = li_item.find_element_by_class_name("lng_commn")
        title_span5 = li_item.find_element_by_class_name("distinctxt rsrtopn-1")
        
        print(try_finding_text_by_class_name("lng_cont_name",li_item))
        print(try_finding_text_by_class_name("green-box", li_item))
        print(try_finding_text_by_class_name("rt_count lng_vote", li_item))
        print(try_finding_text_by_class_name("adWidth cont_sw_addr", li_item))
        print(try_finding_text_by_class_name("lng_commn", li_item))
        print(try_finding_text_by_class_name("distinctxt rsrtopn-1", li_item))
        '''

        info_dict = {
                        "name": try_finding_text_by_class_name("lng_cont_name",li_item),
                        "rating": try_finding_text_by_class_name("green-box",li_item),
                        "votes": try_finding_text_by_class_name("lng_vote",li_item),
                        "address": try_finding_text_by_class_name("cont_sw_addr",li_item),
                        "service": try_finding_text_by_class_name("lng_commn",li_item),
                        "time": try_finding_text_by_class_name("rsrtopn-1",li_item)
        }
        li_dict.append(info_dict)

    keyValList = [""]
    expectedResult = list(filter(lambda d: d["name"] not in keyValList,li_dict))

    # create a new file ; create a function to accept a list of dict & seperator as a parameter & write to a csv file
    # with the name as thecurrenttimestamp.csv python get epoc time stamp

    change_to_csv(expectedResult,"|")



resultsPage()

for i in range(0,100):
    next_page = driver.find_element_by_xpath('//a[@rel="next"]')
    next_page.click()
    time.sleep(5)
    resultsPage()
# //span[@class="jcn"]/span
driver.close()


#//section[@class="rslwrp"]/div/ul


'''
create a list called rows which will hold a list of dictionaries.
Each dictionary is one row

define the schema of the dictionary first
Populate it in one shot.
once populated push this dictionary into the list created


'''



