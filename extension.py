"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so. For the server extension, write your code in
extension_server.py
"""


STOPWORDS = ['a','about','above','after','again','against','all','am','an',
'and','any','are','as','at','be','because','been','before','being','below',
'between','both','but','by','cannot','could','did','do','does','doing','down','during',
'each','few','for','from','further','had','has','have','having','he','her','here','hers','herself',
'him','himself','his','how','i','if','in','into','is','it','its','itself','me','more','most','my',
'myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours',
'ourselves','out','over','own','same','she','should','so','some','such','than','that','the',
'their','theirs','them','themselves','then','there','these','they','this','those','through',
'to','too','under','until','up','very','was','we','were','what','when','where','which',
'while','who', 'why', 'with', 'would', 'you', 'your', 'yours', 'yourself', 'yourselves']


def filter_stopwords(words):
    """
    This function is passed:
        words:      a list of words to filter

    The function will filter all stopwords out of input word list

    >>> filter_stopwords(['a', 'this', 'love'])
    ['love']
    """

    return list(filter(lambda word: word not in STOPWORDS, words))


def stem_words(words):
    """
    This function is passed:
        words:      a list of words to stem

    The function will stem all words from input

    >>> stem_words(['cooking', 'runs'])
    ['cook', 'run']
    """

    from nltk.stem import PorterStemmer
    pStemmer = PorterStemmer()
    stemmed_words = list(map(lambda word: pStemmer.stem(word), words))

    return stemmed_words