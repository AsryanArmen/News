# News
Machine Learning

------------
|Overview  |
------------
In this problem you have no training data. There is only test data - it is in the test_news.csv file .

For each news item from the file, you need to predict its topic.
The topics are as follows (the topic and its numerical code are given below):

    'Society/Russia' : 0
    "Economy" : 1
    'Security structures' : 2
    'Former USSR': 3
    "Sports" : 4
    'Self-Care': 5
    'Construction' : 6
    'Tourism/Travel' : 7
    'Science and Technology': 8
  
You need to parse training data from open news sources (for example, RIA Novosti, Lenta.ru and any other sites) and train a model on it to predict the news topic (you only need news with the topics listed above). The markup is usually on the news site, that is, you will also parse the topics.

Then you need to apply the trained model to the test news and predict the topic (its numeric code). An example file with a forecast - base_submission_news.csv

---------
|main.py|
---------

In this python file we collect data with Selenium

