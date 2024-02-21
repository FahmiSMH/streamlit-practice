import inspect
import json
import numpy as np
from collections import Counter

#we might be able to delete pandas
placeholder = "This function is yet to be implemented"
#changing all tokens to lowercase will helps pattern matching
#we can borrown this function for lemming in preprocessing.py
def toLowerCase(tokens):
    loweredTokens = []

    for i in tokens:
        loweredTokens.append(i.lower())
    return loweredTokens

#maps tokens to its frequency
def getFrequency(tokens):
    frequency_map = []  # Initialize an empty list to store frequency pairs

    # Count the frequency of tokens using Counter
    token_counter = Counter(tokens)

    # Append item-frequency pairs to the frequency_map
    for token, frequency in token_counter.items():
        frequency_map.append([token, frequency])

    return frequency_map

#sort based on frequency
def freqSort(frequency_map):
    frequency_map.sort(key=lambda x: x[1], reverse=True)
    return frequency_map

#Document Term Matrix
def create_dtm_from_frequency_map(documents):
    sentence = "this function takes array of a different dimension than other functions, come back here to fix this"
    
    print("Function:{",inspect.currentframe().f_code.co_name,"() }", sentence)
    # Create a vocabulary set containing all unique terms
    vocabulary = set()
    for document in documents:
        vocabulary.update(term for term, _ in document)

    # Create a mapping from terms to their indices in the vocabulary
    term_to_index = {term: idx for idx, term in enumerate(vocabulary)}

    # Initialize an empty matrix to store the DTM
    num_docs = len(documents)
    num_terms = len(vocabulary)
    dtm = np.zeros((num_docs, num_terms), dtype=int)

    # Fill the DTM with term frequencies
    for doc_idx, document in enumerate(documents):
        for term, frequency in document:
            term_idx = term_to_index[term]
            dtm[doc_idx, term_idx] = frequency

    return dtm, list(vocabulary)

#should we trim the DTM?
def trimming():
    print("Function:{",inspect.currentframe().f_code.co_name,"() }" ,placeholder)

#sort document term library?
def sortDTM():
    print("Function:{", inspect.currentframe().f_code.co_name,"() }", placeholder)

#convert to bag of words
def bagOfWords(tokens):
    print("Function:{", inspect.currentframe().f_code.co_name,"() } : running")
    # Convert to dictionary
    bag_of_words = {word: count for word, count in tokens}

    # Convert to JSON
    json_bag_of_words = json.dumps(bag_of_words)

    return json_bag_of_words


# Example usage
def Example():
    documents = [
        [['sheet', 96], ['var', 82], ['data', 81], ['const', 77], ['google', 62], ['function', 59], ['using', 55], ['method', 54], ['script', 53], ['variable', 51], ['svekis', 48], ['laurence', 47], ['httpsbasescriptscom', 46], ['apps', 38], ['email', 36], ['set', 35], ['message', 34]],
        # Add more documents if needed
    ]
    tokens =  [['sheet', 96], ['var', 82], ['data', 81], ['const', 77], ['google', 62], ['function', 59], ['using', 55], ['method', 54], ['script', 53], ['variable', 51], ['svekis', 48], ['laurence', 47], ['httpsbasescriptscom', 46], ['apps', 38], ['email', 36], ['set', 35], ['message', 34]]
    dtm, vocabulary = create_dtm_from_frequency_map(documents)
    print("statement 1")
    print("Document-Term Matrix:", dtm)
    print("statement 2")
    print("Vocabulary:", vocabulary)
    print("statement 3")

    trimming()
    sortDTM()
    bagOfWords(tokens)

if __name__ == "__main__":
    Example()