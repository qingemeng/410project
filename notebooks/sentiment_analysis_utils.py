from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

client = language_v1.LanguageServiceClient()
def analyze_sentiment(content):
    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    return sentiment
#     print('Score: {}'.format(sentiment.score))
#     print('Magnitude: {}'.format(sentiment.magnitude))
