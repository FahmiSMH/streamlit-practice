from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def noSpecial(string):
    # Split the input string into words
    words = string.split()

    # Initialize an empty list to store cleaned words
    cleaned_words = []

    # Iterate over each word
    for word in words:
        # Remove special characters from the word and append to cleaned_words
        cleaned_word = ''.join(char for char in word if char.isalnum())
        cleaned_words.append(cleaned_word)

    # Join the cleaned words back into a string
    result = ' '.join(cleaned_words)

    return result
           
#tokenize all the words in the string
def tokenize(sample):
    word = ""
    #split text separated by space
    word = sample.split()
    return word

#remove stop words done
def removeWord(samplearray):
    #print(samplearray)
    newArray = []
    stop_words = set(stopwords.words('english'))
    for i in samplearray:
        if(i.lower() not in stop_words):
            newArray.append(i)
    
    return newArray

#lemming
def lemming(tokens):
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each token
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens