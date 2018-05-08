# article-recommender
Flask App to browse news articles and recommend similar articles.

This application runs a Flask app that allows you to run [BBC](http://mlg.ucd.ie/datasets/bbc.html "BBC")
articles across various genres (business, entertainment, politics, sport, tech). However, this can be extended to any corpus of text documents.

The output when running the Flask app should look like this:
![alt text](https://github.com/nicharuc/article-recommender/blob/master/img/article1.png)

User will need to also download [GloVe](https://nlp.stanford.edu/projects/glove/ "GloVe"), which are word embeddings that represent word semantics.

To run in terminal:
```
python glove_filepath articles_folder_filepath
```
