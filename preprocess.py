import re
import string

def preprocess(data, nltk_stopwords):

    # Remove urls
    new_data = re.sub(r"http\S+", "", data)
    new_data = re.sub(r"www\S+", "", new_data)

    # Remove punctuations
    new_data = data.translate(str.maketrans('', '', string.punctuation))

    # remove digits
    new_data = re.sub(r'\w*\d\w*', '', new_data).strip()

    new_data = new_data.lower().split()

    stopwords = stop_word_extension(nltk_stopwords=nltk_stopwords)
    filtered_words = [w for w in new_data if not w in stopwords]
    filtered_words = delete_one_length_strings(filtered_words)

    str1 = " "
    preprocessed_data = str1.join(filtered_words)

    return preprocessed_data


def delete_one_length_strings(data_list):
    for element in data_list:
        if len(element) >1:
            continue
        else:
            data_list.remove(element)
    return data_list

def stop_word_extension(nltk_stopwords):
    extended_list = ["de", "fr", "ag", "nr", "ar", "a", "i", "ch7788", "chf", "herr", "77362ps",
                     "t318539582ps", "gk", "allgemein", "d", "yan", "seen", "his", "zz", "on", "yan", "tan", "fi", "sr",
                     "res", "agehene", "verka", "ser", "li", "umrake", "16v", "n", "bedingungen", "www", "r", "cb",
                     "beding", "mie", "ch", "r", "pr", "ag", "t", "ps", "herr", "z", "n", "www", "de", "ber", "sch", "ge"]

    new_stop_words = nltk_stopwords + extended_list

    return new_stop_words


