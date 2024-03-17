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
    points=0
    mot=''
    for word in words:
        if score(word)>points:
            mot=word
            points=score(word)
    res=(mot,points)
    return res