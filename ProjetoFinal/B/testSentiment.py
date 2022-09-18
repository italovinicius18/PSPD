from LeIA.leia import SentimentIntensityAnalyzer 

s = SentimentIntensityAnalyzer()

ex1 = 'eu odeio o bolsonaro'

ex2 = 'bolsonaro é bom'

ex3 = 'eu odeio o lula'

ex4 = 'lula é bom'

print(s.polarity_scores(ex1))

print(s.polarity_scores(ex2))

print(s.polarity_scores(ex3))

print(s.polarity_scores(ex4))