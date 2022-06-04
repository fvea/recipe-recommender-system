from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(r'data_collection\chromedriver.exe')
driver.get('https://www.tasteatlas.com/100-most-popular-foods-in-philippines')

link_texts = ['', '(50-11) Filipino Foods', '(10-1) Filipino Foods']
ulam_titles = []
ulam_ingredients = []
ulam_descriptions = []
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
            ulam_desc = article.find_element_by_class_name("description").text
            # ulam_pic_link = article.find_element_by_class_name("swiper-slide")
            try:
                ul_elem = article.find_element_by_tag_name('ul')
            except:
                continue
            ingredients = [li.text for li in ul_elem.find_elements_by_tag_name('li')]
            ulam_titles.append(ulam_title)
            ulam_descriptions.append(ulam_desc)
            ulam_ingredients.append(ingredients)
            print('{0}: {1}'.format(ulam_title, ingredients))
            

driver.quit()
print('ulam_titles.len: {0}\n ulam_ingredients.len: {1}'.format(
    len(ulam_titles), len(ulam_ingredients)))
# convert to DataFrame
ulam_df = pd.DataFrame({'ulam_titles': ulam_titles, 
                        'ingredients': ulam_ingredients, 
                        'ulam_descriptions': ulam_descriptions})
ulam_df.to_csv(r'data_collection\ulam.csv')
print(ulam_df.head())
print('web scraping done!')

