import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import re
import matplotlib.pyplot as plt
% matplotlib inline

df=pd.read_csv('C:/Users/Owner/Downloads/barbie_Cleaned.csv')

# controllare se possiamo dividere la colonna text
# ha una struttura titolo - user - data con mese e anno - recensione


#vediamo se in ogni riga esiste solo un 'July 2023'

conto = 0

for i in df['text']:
    x=i.count('July 2023')
    if x >1:
        conto+=1
        colpevole=[i]



conto ==0

# False. Esiste una riga in cui 'July 2023' e' scritto 2 volte.
# Dobbiamo dividere allora per la prima istanza di 'July 2023' nel testo
# anche se: potrebbe essere nel titolo

date=[]
pattern = r'\d{1,2}\s+[A-Za-z]+\s+\d{4}'


split_parts=[]
for i in df['text']:
    split_parts.append(re.split(pattern, i)[1])

# split_parts adesso contiene tutte le recensioni, ma non i titoli o le date
# nelle recensioni ci sono quelle marcate "Warning: Spoilers"
# vediamo quante sono

conto_spoilers=0

for i in split_parts:
    if 'Warning: Spoilers' in i:
        conto_spoilers +=1
        
# 197 recensioni hanno "Warning: Spoilers" e quello solamente, quindi devono essere cancellate, perche' inutili
# avremo dunque un totale di 600 recensioni

for i in split_parts:
    if 'Warning: Spoilers' in i:
        split_parts.remove(i)
        
# perche' ho dovuto premere 3 volte per eliminarli tutti?


wordcloud=WordCloud().generate(split_parts[3])

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()



# ora qwuello vero

text = " ".join(i for i in split_parts)

barbie_mask = np.array(Image.open("C:/Users/Owner/Downloads/barbie-silhouette-png-9.png"))


stopwords = set(STOPWORDS)
stopwords.update(["review", "helpful", "film", "movie","Sign","found","Permalink","vote","one","much","really","way",
                  "message","even","thing","watch","movies"])

wordcloud = WordCloud(stopwords=stopwords,width=4000,height=2000,colormap="pink",mask=barbie_mask).generate(text)

plt.figure( figsize=(40,20) )
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


