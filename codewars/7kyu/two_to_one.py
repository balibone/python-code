def longest(s1, s2):
    combined_unique_string = set(s1+s2)
    sorted_char_list = sorted(combined_unique_string)
    sorted_unique_string = "".join(sorted_char_list)

    return sorted_unique_string


print(longest("aretheyhere", "yestheyarehere"))
