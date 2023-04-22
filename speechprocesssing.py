
# import speech_recognition as sr
# from gtts import gTTS
# import os
import random
# from re import L
# from tracemalloc import stop
# import nltk
# import ssl
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')

# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# from nltk.text import Text
# import googletrans
# from googletrans import Translator

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# def speech_processing(data):
    
#     random.seed()

#     example_string = "cappuccinos are the worst"
#     words = word_tokenize(data)

#     stop_words = set(stopwords.words("english"))
#     add_words_to_set = {'get', 'please', 'have', 'need'}
#     stop_words = stop_words.union(add_words_to_set)

#     filtered_list = [
#         word for word in data if word.casefold() not in stop_words
#     ]

#     lemmatizer = WordNetLemmatizer()
#     translator = Translator()
#     lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]
#     nltk.pos_tag(lemmatized_words)

#     print(googletrans.LANGUAGES)
#     print(lemmatized_words)
#     print(type(lemmatized_words))

#     result = translator.translate(lemmatized_words ,src = 'auto', dest = 'fr')
#     for translation in result:
#         print(f'{translation.origin} -> {translation.text}')



def replyToCustomer(number, drink):
    if(drink == ''):
        return "I cannot get that for you. We only serve coffees and teas!"
    elif(drink == "processing input"):
        return "hey there, how can I help?"
    else:
        options = ["Sure, " + number + " " + drink + " coming right up",
                    "Yes, I can get that for you",
                    number + " " + drink + "? Of course!",
                    "Good choice! " + number + " " + drink + " coming up",
                    "Sure thing darling"]

        index = random.randint(0, len(options)-1)
        return options[index]

def process(text):

        # number = ''
        # if (text.find('one') != -1 or text.find('1') != -1 or text.find('a ') != -1 or text.find('') != -1):
        #     number = 'one'
        # elif (text.find('two') != -1 or text.find('2') != -1):
        #     number = 'two'

        drink = ''
        if (text.find("hey barista") != -1 or text.find("hi") != -1 or text.find("hello") != -1 or text.find("hey") != -1 or text.find("hey there") != -1 or text.find("barista") != -1):
            drink = "processing input"
        elif(text.find('cappuccino') != -1 or text.find('cappuccinos') != -1 ):
            drink = 'cappuccino'
        elif(text.find('latte') != -1 or text.find('lattes') != -1 ):
            drink = 'latte'
        elif(text.find('mocha') != -1 or text.find('mochas') != -1 ):
            drink = 'mocha'
        elif(text.find('tea') != -1 or text.find('teas') != -1 ):
            drink = 'tea'
        elif(text.find('espresso') != -1 or text.find('esspressos') != -1 ):
            drink = 'espresso'
        elif(text.find('hot chocolate') != -1 or text.find('hot chocolates') != -1 ):
            drink = 'hot chocolate'
        elif(text.find('americano') != -1 or text.find('americanos') != -1 ):
            drink = 'americano'

        s = ''
        if(text.find('idiot') != -1 or text.find('dumb') != -1 or text.find('baka') != -1 or text.find('lamo') != -1):
            s = "That is not very nice! But, "

        return drink, s + replyToCustomer("one", drink)

# def processForCompVis(text):
#     options = ["cappuccino",
#                     "latte",
#                     "mocha",
#                     "hot chocolate"]

#     index = random.randint(0, len(options)-1)
#     return options[index]




