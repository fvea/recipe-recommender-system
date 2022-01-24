from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r'C:\Users\fjvin\ulam_recommender_system\data_collection\chromedriver.exe')
driver.get('https://www.tasteatlas.com/100-most-popular-foods-in-philippines')
link_texts = ['', '(50-11) Filipino Foods', '(10-1) Filipino Foods']
ulam_ingredients = {}

for link_text in link_texts:

    if link_text != '': 
        link_elem =  driver.find_element_by_link_text(link_text)
        link_elem.click()

    try:
        _ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "top-list-article__list"))
        )
    finally:
        articles = driver.find_elements_by_class_name("top-list-article__item--shrinked")
        for article in articles:
            ulam_title = article.find_element_by_tag_name('h2').text
            try:
                ul_elem = article.find_element_by_tag_name('ul')
            except:
                print('{0}: {1}'.format(ulam_title, []))
                ulam_ingredients[ulam_title] = []
                continue
            ingredients = [li.text for li in ul_elem.find_elements_by_tag_name('li')]
            print('{0}: {1}'.format(ulam_title, ingredients))
            ulam_ingredients[ulam_title] = ingredients

driver.quit()
print(len(ulam_ingredients))

