from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(r'data_collection\chromedriver.exe')
driver.get('https://www.tasteatlas.com/100-most-popular-foods-in-philippines')

link_texts = ['', '(50-11) Filipino Foods', '(10-1) Filipino Foods']
ulam_ingredients = []

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
            if ulam_title == 'Pancit' or ulam_title == 'Lumpia': continue
            try:
                ul_elem = article.find_element_by_tag_name('ul')
            except:
                continue
            ingredients = {li.text.split('OR\n')[-1]:1 for li in ul_elem.find_elements_by_tag_name('li')}
            print('{0}: {1}'.format(ulam_title, ingredients))
            ulam_ingredients.append(pd.Series(ingredients, name=ulam_title))

driver.quit()
# convert to DataFrame
ulam_df = pd.DataFrame(ulam_ingredients)
ulam_df.to_csv(r'data_collection\ulam.csv')
print('web scraping done!')

