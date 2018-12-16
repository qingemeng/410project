# Semantic search tool for stack overflow 

The tool we are is a semantic search engine for python related stack overflow solutions. It will retrieve top 100 stack overflow answers based on semantic similarity, voting, and corresponding comments sentiments.

## Application
The web app is hosted on a GCP VM instance. The URL is http://35.197.153.176:5001/search
We use Flask framework for building this app.

## Preparing data/model/indices etc for the Application

#### Data: Public data set on big query https://cloud.google.com/bigquery/public-data/stackoverflow is used
#### Preprocessing
Stack overflow answer body, votes, comments as well as the url are retrieved and processed. We are using BigQuery to get the table, storing it on Google Cloud Storage, and export csv from there.

#### Data cleaning and transformation
- Scoping the problem down to python by filtering out the solutions which have an question of a *python* tag
- Code block in each post is removed since it is not always correct and complete, and most of the time, it doesn’t have semantic meaning.
- Urls are constructed for each post to guild user to the stack overflow site
- Comment sentiments are retrieved using TextBlob library.

#### Training model
With particular domain, we decided to train our own model to generate embeddings. With stackoverflow data processed. An unsupervised learning approach is adopted. 500 feature dimensions are given to LSTM model.

#### Ranking results
- We use a tanh function to process votes to scale it to -1 to 1, and penalize on the extreme values
- Sentiments are normalized before use.
- `nmslib` is used to build index and retrieve index with cosine similarity. 
- `distance + 0.01/tanh(vote) + 0.001/normalize(polarity)` is used to get the ranking score for the top 100 results.

Jupyter notebook is used for this project, and the server is hosted on a GCP instance with URL http://35.197.153.176:8888

The details of each step are in-lined with each notebook

## Infrastructure: 
- We deployed a VM instance (16 vCPUs, 104 GB memory, 100GB disk space)with a pre-built docker imaging to train our language model since our laptops are not powerful enough to achieve this.
- Language model training: 
We’ve trained a language model with a dataset(644466 rows)

## Code structure

```
.
├── notebooks (containing notebooks for process data, train language model, get embedding and build index, etc)
│   ├── Get\ results.ipynb
│   ├── Process\ stackoverflow\ data.ipynb
│   ├── README.md
│   ├── Train\ LM\ with\ stackoverflow.ipynb
│   ├── general_utils.py
│   ├── lang_model_utils.py
│   ├── sentiment_analysis_utils.py
│   └── seq2seq_utils.py
├── requirements
│   └── requirements.txt
├── setup.sh
├── vm-setup.md
└── webapp (Flask application for the search engine)
    ├── README.md
    ├── main.py
    ├── search_engine.py
    └── static
```


