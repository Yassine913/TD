#ex1et2..................
# function read_file has in argument the filename and return a list of all words in the file.

def read_file(filename):
    f=open(filename,'r')
    frenchwords=list()
    for word in f:
        frenchwords.append(word.strip())
    return frenchwords

#is_mot_possible the word 'word' is constituted of letters in tirage
def is_word_possible(tirage,word):
    list=tirage.copy()
    for alph in word:
        if alph not in list:
            return False
        list.remove(alph)
    return True


#possiblewords return a list of all possible words filename that are constituted of letters in tirage
def possiblewords(tirage,filename):
    return[word for word in read_file(filename) if is_word_possible(tirage,word)]
    
#longestword return the longest word of the possiblewords 
def longestword(filename,tirage):
    wordpossible=possiblewords(tirage,filename)
    solution=wordpossible[0]
    for word in wordpossible:
        if len(word)>len(solution):
            solution=word
    return solution