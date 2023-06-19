# IRM-FINAL-RESIT

For this research we've extracted tweets from both 2013 and 2023. The aim is compare how three common French loanwords have been used over the course of ten years. The three loanwords we are using for this are: "bureau", "cadeau" and "niveau". These three words are sometimes also spelled in a way that is phonetically easier for Dutch speakers to understand: "buro", "kado" and "nivo". We're gonna loot at whether or not the usage of these different spellings have increased, decreased or stayed stagnant. Based on that we might find interesting things to say about how the Dutch language is changing. 

To calculate the differences between 2013 and 2013 a IRM_FINAL.py Python script was created, which shows you how often each word occurs in each file and compares it to the other spelling for both 2013 and 2023. 

In order to get the data we want we used Karora to extract tweets. The commands we used were consecutively:

zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'kado|cadeau' > file12013.txt

zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'kado|cadeau' > file12023.txt

zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'buro|bureau' > file22013.txt

zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'buro|bureau' > file22023.txt

zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'nivo|niveau' > file32013.txt

zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'nivo|niveau' > file32023.txt

You will see that for every word we picked the 1st of January in both 2013 and 2023 and no specific time to avoid having an unknown variable influencing the results.

After having done that, we ran the python script within the same directory as the .txt files.
