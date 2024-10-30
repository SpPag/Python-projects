"""
Να κατασκευάσετε ένα πρόγραμμα που χρησιμοποιεί μια συνάρτηση count_capital_small(s) για να μετρήσει τα κεφαλαία και τα
μικρά γράμματα σε ένα κείμενο που ζητείται από τον χρήστη. Εγώ θα ονομάσω τη συνάρτηση count_upper_lower_case(text)
γιατί το capital και small μου φαίνεται άσχημη επιλογή ονομασίας κεφαλαία και πεζά γράμματα και η ονομασία της
παραμέτρου s για συμβολοσειρά, επειδή αφορά ελληνικά με ενοχλεί και γι' αυτό την ονομάζω text.
"""


def count_upper_lower_case(text):
    upper_count = 0
    lower_count = 0
    for element in text:
        if element.isalpha():
            if element.isupper():
                upper_count += 1
            if element.islower():
                lower_count += 1
    return (f"The number of uppercase letters in your text is {upper_count} and that of lowercase letters, is "
            f"{lower_count}")


while True:
    text = input("What text I analyze? (input break or exit to exit) \n")
    if text.lower().strip() in "break, exit":
        break
    count_upper_lower_case(text)
    print(count_upper_lower_case(text))

