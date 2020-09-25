# Web-Scraping-and-Clustering
This repository contains code that was used to scrape the names of peer-reviewed articles from the journal PLOS ONE. A K-Means clustering algorithm was then applied to the data to sort the article names into clusters based on their content. 

## Introduction 
PLOS ONE is an open-access journal published by the Public Library of Science. The journal publishes primary research articles from any area that falls under science or medicine. Some of the categories outlined on their website include Biology and Life Sciences, Computer and Information Sciences, Earth Sciences, People and Places, and Physical Sciences. This project aims to use a clustering algorithm to sort articles into categories based on the names of the articles. 

## Methods 
#### Dataset Creation and Pre-processing 
The dataset contains 1,300 article names scraped from the PLOS ONE website using the Beautiful Soup library (code can be found in file webscraper.py). The data was pre-processed by removing stop words and punctuation, changing all words to lowercase, and stemming the words to their root word.

#### Feature Generation 
TF-IDF values were calculated and used as features. TF-IDF values determine how important a word is to a document. The TF-IDF value for a term in a document is directly proportional to the number of times the word appears in that document and inversely proportional to the number of document in which it appears. Thus the value is adjusted to ensure common words don't have a higher value. TF-IDF vectors are commonly used as features in the clustering of text data. 

#### Clustering Model 
The clustering model that was used is the K-Means model which is an unsupervised Machine Learning model. This model clusters by identifying 'K' centroids which are the centers of the clusters. The average Silhouette score was used to measure the performance of the algorithm. The Silhouette score is a value between -1 and 1 and determines how close data points in one cluster are to those in another. If the value is close to 1, that means that data points are far from other clusters, if it close to 0 that means that clusters are overlapping, and if it is close to -1 that means the clusters are not well-defined. The average Silhouette score was calculated for K values from 2 to 20 and the number with the highest Silhouette score was used. 


## Analysis 
The average Silhouette scores were all above 0 but were very low. This was an early indication that the clustering might be inconclusive. A K value of 18 was used for the final model. On calculating the 10 most common words in each cluster, many of the clusters contained common research terms. The most terms in cluster 0 for example were model, base, human, respons, diseas, character, chang, detect, applic, correct. These are all common words used in research articles. This was also the cluster with the largest number of articles. The model's performance might improve on including these common research terms in the stop word list. A few clusters seemed to have common words that were relevant to a particular topic. For instance, cluster 2 had the following common words:  covid19, factor, patient, survey, global, studi, among, pandem, risk, social. These are all words that can be associated with the Covid19 pandemic. These were all stemmed words. Changing the way the data was pre-processed might also improve the performance of the model as would adding features. It also possible that another clustering algorithm might perform better on this dataset. 


## References
The following are articles that I refered to:

PLOS ONE:
https://journals.plos.org/plosone/

K-Means: 
https://medium.com/neuronio/unsupervised-learning-with-k-means-3eaa0666eebf, 
https://medium.com/@lucasdesa/text-clustering-with-k-means-a039d84a941b, 
https://medium.com/@MSalnikov/text-clustering-with-k-means-and-tf-idf-f099bcf95183

Web-Scraping
https://towardsdatascience.com/web-scraping-news-articles-in-python-9dd605799558


