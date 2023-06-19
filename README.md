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
The results should then look like this:

'kado' appears '180' times compared to 'cadeau' '359' (0.3339517625231911, 0.6660482374768089) with a difference of: 179 in file12013.txt
'kado' appears '16' times compared to 'cadeau' '106' (0.13114754098360656, 0.8688524590163934) with a difference of: 90 in file12023.txt
'buro' appears '14' times compared to 'bureau' '178' (0.07291666666666667, 0.9270833333333334) with a difference of: 164 in file22013.txt
'buro' appears '5' times compared to 'bureau' '68' (0.0684931506849315, 0.9315068493150684) with a difference of: 63 in file22023.txt
'nivo' appears '22' times compared to 'niveau' '507' (0.04158790170132325, 0.9584120982986768) with a difference of: 485 in file32013.txt
'nivo' appears '24' times compared to 'niveau' '747' (0.0311284046692607, 0.9688715953307393) with a difference of: 723 in file32023.txt
