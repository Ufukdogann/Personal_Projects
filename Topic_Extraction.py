from nltk.corpus import stopwords
from preprocess import *
from gensim.summarization import keywords
import nltk
import pdfplumber

# For text files

# with open("data_1.txt", "r", encoding="utf-8") as t:
#     data = t.read()


# For pdf files

pdf_file = "Papers/w19806.pdf"
with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    data = pages[0].extract_text()
    print(data)

nltk.download('stopwords')
nltk_stopwords = stopwords.words('english')
#
preprocessed_data = preprocess(data=data, nltk_stopwords=nltk_stopwords)
#
keyword_list = keywords(preprocessed_data, words=5, lemmatize=True)
print(keyword_list)


