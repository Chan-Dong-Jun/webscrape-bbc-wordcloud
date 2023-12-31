from articlescraper import parse_article
from datetime import datetime, timedelta
import pandas
from wordcloud import WordCloud
import matplotlib.pyplot as plt

tod = datetime.now()
word_cloud_map = {}

# period must be after 2015
if (date := input("Pls input date in format (yyyymmdd): ")):
    tod = datetime.strptime(date, "%Y%m%d")

multiplier = 1 # interval between each days 
for no in range(5): 
    parse_article("https://web.archive.org/web/"+ str((tod-timedelta(days=no*multiplier)).strftime('%Y%m%d'))+"/https://www.bbc.com/zhongwen/simp", word_cloud_map)

# create wordcloud
font_path ="SourceHanSerifK-Light.otf"
wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, max_font_size=200, width=1000, height=860,random_state=1)
wc.generate_from_frequencies(word_cloud_map)
plt.imshow(wc)
plt.axis("off")
plt.show()

print(word_cloud_map)