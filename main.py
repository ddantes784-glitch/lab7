import string
from collections import Counter
text = """
Гарри Поттер ни разу в жизни не слышал о Хогвартсе, когда письма начали 
прилетать на Тисовую улицу. Дядя Вернон, тётя Петунья и их сын Дадли 
были совершенно обычными людьми. Они терпеть не могли всё странное и загадочное. 
Но однажды ночью, когда на улице гремел гром, а дождь стучал в окна, 
в их жизни появился великан по имени Хагрид. Он принёс письмо для Гарри. 
Мальчик, который выжил, наконец узнал правду о своей семье, о волшебстве 
и о том, что его ждёт в школе магии Хогвартс.
"""
text_lower = text.lower()
clean_text = text_lower.translate(str.maketrans('', '', string.punctuation))
words = clean_text.split()
word_counts = Counter(words)
print("Топ-10 самых частых слов:")
for word, count in word_counts.most_common(10):
    print(f"{word:<15} : {count}")
