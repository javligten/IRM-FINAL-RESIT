correct1 = "cadeau"
incorrect1 = "kado"
file12013 = "file12013.txt"
file12023 = "file12023.txt"

correct2 = "bureau"
incorrect2 = "buro"
file22013 = "file22013.txt"
file22023 = "file22023.txt"

correct3 = "niveau"
incorrect3 = "nivo"
file32013 = "file32013.txt"
file32023 = "file32023.txt"

def calculate_frequency(incorrect, correct, filename):
    with open(filename, 'r') as f:
        text = f.read()
    
    words = text.split()
    
    count_incorrect = words.count(incorrect)
    count_correct = words.count(correct)
    total = count_incorrect + count_correct
    
    if count_incorrect > count_correct:
        result = count_incorrect / total, count_correct / total
        difference = count_incorrect - count_correct
        print(f"'{incorrect}' appears '{count_incorrect}' times compared to '{correct}' '{count_correct}'", result, "with a difference of:", difference, "in", filename)
    elif count_correct > count_incorrect:
        result = count_incorrect / total, count_correct / total
        difference = count_correct - count_incorrect
        print(f"'{incorrect}' appears '{count_incorrect}' times compared to '{correct}' '{count_correct}'", result, "with a difference of:", difference, "in", filename)
    else:
        result = count_incorrect / total, count_correct / total
        print(f"'{incorrect}' and '{correct}' have the exact same usage frequency", result, difference, "in", filename)

calculate_frequency(incorrect1, correct1, file12013)
calculate_frequency(incorrect1, correct1, file12023)
calculate_frequency(incorrect2, correct2, file22013)
calculate_frequency(incorrect2, correct2, file22023)
calculate_frequency(incorrect3, correct3, file32013)
calculate_frequency(incorrect3, correct3, file32023)

"""COMMANDS TO GET THE DATA"""
"""zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'kado|cadeau' > file12013.txt"""
"""zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'kado|cadeau' > file12023.txt"""

"""zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'buro|bureau' > file22013.txt"""
"""zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'buro|bureau' > file22023.txt"""

"""zless /net/corpora/twitter2/Tweets/2013/01/20130101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'nivo|niveau' > file32013.txt"""
"""zless /net/corpora/twitter2/Tweets/2023/01/20230101\:*.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | grep -E -i -w 'nivo|niveau' > file32023.txt"""