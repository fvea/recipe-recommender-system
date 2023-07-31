# Filipino-based Dish (Ulam) Recommendation System

This project aims to develop a recommender system for recommending relevant Filipino-based dishes to users based on the given set of ingredients and/or food allergens to consider when providing recommendations.

## Dataset
A web scraper script using Python-Selenium is used to collect a list of common Filipino dishes and their ingredients from [tasteatlas.com](https://www.tasteatlas.com/100-most-popular-foods-in-philippines) as shown in the table below. Overall, the script collected over 90 unique Filipino dishes.

|      Index      |     Ulam Title      |      Ingredients      |
|---------------------|---------------------|---------------------|
|   0     |   Adobong manok    |   ['CHICKEN', 'ONION', 'GARLIC', 'SOY SAUCE', 'WHITE WINE VINEGAR', 'BAY LEAF', 'BROWN SUGAR', 'PEPPERCORNS', 'OIL']    |
|   1     |   Talunan    |   ['CHICKEN', 'VINEGAR', 'GINGER', 'GARLIC', 'FISH SAUCE', 'BLACK PEPPER', 'SALT', 'BAY LEAF']    |
|   2    |   ...     |   ...     |


## Natural Language Processing (NLP)

The project uses basic natural language processing (NLP) to convert the user's given set of ingredients into a bag-of-words/TF-IDF representation, which a machine learning model (nearest-neighbor) uses to recommend relevant dishes based on similarity (cosine-similarity) with other dishes.

![CPE 020 FINAL PRESENTATION](https://github.com/fvea/dishiseat_recipe_recommendation_algo/assets/75005859/02f820c9-3db3-4f7b-86c2-f529a635c1de)

## Algorithm Demo

https://github.com/fvea/dishiseat_recipe_recommendation_algo/assets/75005859/79c5fbff-494b-4998-b35c-0bd9a21f60f1

## Resources:
- https://www.tasteatlas.com/100-most-popular-foods-in-philippines

## Developers
- Fj Vincent Atabay
- Joel Francis Aseo
- Dea Marielle Cahambing
- Faith Mary Galon
- Angel Mary Isip
- John Michael Tejada
