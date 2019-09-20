def get_middle(s):
    word_length = len(s)
    mid_index = (word_length-1) / 2
    if word_length % 2 == 0:
        return s[mid_index:mid_index+2]
    else:
        return s[mid_index]
