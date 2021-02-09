""" Word cloud """
# Still contains bugs

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = "!()-[]{};:'\,<>.?@\#$%^&*_~''"
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with",
                           "from", "here", "when",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor",
                           "too", "very",
                           "can", "will", "just"]

    words_dict = {}
    list_of_words = file_contents.split(" ")
    for word in list_of_words:
        # word = word.lower()
        new_word = ""
        for x in word:
            if x not in punctuations:
                new_word = new_word + x
        word.lstrip().rstrip()
        if word.isalpha() and word not in uninteresting_words:
            words_dict[word] = words_dict.get(word, 0) + 1

    return words_dict


file_contents = " Dear Team, Dear Team, Dear Team, if .,AASDanisad.,. google, Google Coursera ."

print(calculate_frequencies(file_contents))
