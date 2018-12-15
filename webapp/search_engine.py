from pathlib import Path
import pandas as pd
import torch
import numpy as np
import nmslib
from sklearn import preprocessing
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'notebooks'))
import lang_model_utils

class search_engine:
    """Organizes all the necessary elements we need to make a search engine."""

    def __init__(self,
                 nmslib_index,
                 ref_df,
                 query2emb_func):
        """
        Parameters
        ==========
        nmslib_index : nmslib object
            This is pre-computed search index.
        ref_df : pandas.DataFrame
            This dataframe contains meta-data for search results,
            must contain the columns 'code' and 'url'.
        query2emb_func : callable
            This is a function that takes as input a string and returns a vector
            that is in the same vector space as what is loaded into the search index.

        """
        assert 'url' in ref_df.columns
        assert 'content' in ref_df.columns

        self.search_index = nmslib_index
        self.ref_df = ref_df
        self.query2emb_func = query2emb_func

    def search(self, str_search, k=1000):
        """
        Prints the code that are the nearest neighbors (by cosine distance)
        to the search query.

        Parameters
        ==========
        str_search : str
            a search query.  Ex: "read data into pandas dataframe"
        k : int
            the number of nearest neighbors to return.  Defaults to 2.

        """
        query = self.query2emb_func(str_search)
        return self.search_index.knnQuery(query, k=k)


def init_search_engine():
    input_path = Path('../notebooks/data/stackoverflow/processed_data/')
    body_df = pd.read_csv(input_path / 'test.content_token', header=None, names=['content'])
    vote_df = pd.read_csv(input_path / 'test.vote', header=None, names=['vote'])
    assert body_df.shape[0] == vote_df.shape[0]
    comment_df = pd.read_csv(input_path / 'test.comment')
    assert body_df.shape[0] == comment_df.shape[0]
    url_df = pd.read_csv(input_path / 'test.url', header=None, names=['url'])
    assert body_df.shape[0] == url_df.shape[0]
    ref_df = pd.concat([url_df, body_df, comment_df, vote_df], axis=1).reset_index(drop=True)
    ref_df.vote = np.tanh(ref_df.vote)
    ref_df[['sentiment_polarity', 'sentiment_subjectivity']] = preprocessing.MinMaxScaler().fit_transform(ref_df[['sentiment_polarity', 'sentiment_subjectivity']])

    vocab = lang_model_utils.load_lm_vocab('../notebooks/data/stackoverflow/lang_model/vocab.cls')
    lang_model = torch.load('../notebooks/data/stackoverflow/lang_model/lang_model_cpu.torch',
                            map_location=lambda storage, loc: storage)
    q2emb = lang_model_utils.Query2Emb(lang_model = lang_model.cpu(),
                  vocab = vocab)

    search_index = nmslib.init(method='hnsw', space='cosinesimil')
    search_index.loadIndex('../notebooks/data/stackoverflow/lang_model_emb/dim500_avg_searchindex.nmslib')

    se = search_engine(nmslib_index=search_index,
                       ref_df=ref_df,
                       query2emb_func=q2emb.emb_mean)

    print("Search engine initialized!")
    return ref_df, se
