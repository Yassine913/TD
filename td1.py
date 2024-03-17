#filename dans tout ce TD fait reference au nom du fichier frenchssaccent
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

#ex3......................
#return score of the word in argument
def score(mot):
    point1=['a','e','i','l','n','o','r','s','t','u']
    point2=['d','g','m']
    point3=['b','c','p']
    point4=['f','h','v']
    point8=['j','q']
    point10=['k','w','x','y','z']
    points=0
    if mot=='':
        return 0
    for alph in mot:
        if alph in point1 :
            points+=1
        elif alph in point2:
            points+=2
        elif alph in point3:
            points+=3
        elif alph in point4:
            points+=4
        elif alph in point8:
            points=8
        else:
            points+=10
    return points


# max_score return the word that has the maximum points and the value of the maximum points
def max_score(words):
    solution=words[0]
    for word in words:
        if score(solution)<score(word):
            solution=word
    return [solution,score(solution)]
    
#the flowing function return the word that has the maximum points from tirage.
def research_maxpoints(tirage,filename):#tirage is a list of strings
    words=possiblewords(tirage,filename)
    return max_score(words)

#ex4........................

#return the word with the highest score and its score.
def highest_scoreword(letters,filename):#letters is a string of letters that can contain '?'
    joker='?'
    if joker not in letters:
        return research_maxpoints(list(letters),filename)
    else:
        positionjoker=letters.find(joker)
        alphabet='abcdefghijklmnopqrstuvwxyz'
        words=[]
        for letter in alphabet:
            listletters=list(letters)
            listletters[positionjoker]=letter
            words.append(possiblewords(listletters,filename))
        return research_maxpoints(words,filename)
            



