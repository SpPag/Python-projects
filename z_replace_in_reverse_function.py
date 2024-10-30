def r_replace(string, old, new, number_of_occurences=-1):
    string_list = string.rsplit(old, number_of_occurences)
    string_new = new.join(string_list)
    return string_new
