from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\fjvin\ulam_recommender_system\data_collection\chromedriver.exe')

driver.get('https://www.tasteatlas.com/100-most-popular-foods-in-philippines')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "top-list-article__list"))
    )
finally:
    ulam_ingredients = {}

    for i in range(1, 51):

        xpath = '//*[@id="19402"]/section/div[{}]'.format(i)

        div_elem = driver.find_element_by_xpath(xpath=xpath)

        ulam_title = div_elem.find_element_by_tag_name('h2').text

        try:
            ul_elem = div_elem.find_element_by_tag_name('ul')
        except:
            print('iteration#{0} -> {1}: {2}'.format(i, ulam_title, []))
            ulam_ingredients[ulam_title] = []
            continue

        ingredients = []
        for li in ul_elem.find_elements_by_tag_name('li'):
            ingredients.append(li.text)
        
        print('iteration#{0} -> {1}: {2}'.format(i, ulam_title, ingredients))
        ulam_ingredients[ulam_title] = ingredients

    driver.quit()
        

