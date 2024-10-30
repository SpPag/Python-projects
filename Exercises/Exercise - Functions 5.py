"""
Να κατασκευάσετε συνάρτηση formatted_print(text, width, align) που να δέχεται ως είσοδο ένα κείμενο text, έναν ακέραιο
αριθμό ως width και μια λογική μεταβλητή (boolean) align. Η συνάρτηση να μορφοποιεί το κείμενο, σε στήλη πλάτους width,
και αν align = True, το στοιχίζει.
Επιλέγω να θέσω τις παραμέτρους width και align ως προαιρετικές.
"""


def receive_multiple_line_text():
    global text
    text = ""
    print("type text here: ")
    while True:
        new_text = input()
        if new_text == "":
            break
        text += new_text.strip() + " "
    return text.strip()


def align_text(line, width):
    sp = " "
    line = line.strip()
    needed_spaces = int(width) - len(line)
    if sp not in line:
        return line
    while len(line) < int(width):
        line = line.replace(sp, sp + " ", needed_spaces)
        sp += " "
    return line


def formatted_print(text, width=70, align=False):
    line = ""
    split_text = text.split()
    alignment = ""
    while alignment not in y_n_answers:
        alignment = input("Do you want to align your text? Y/N\n").upper()
    if alignment in "Y, Υ":
        align = True
    if alignment in "N, Ν":
        align = False
    min_width = max(len(x) for x in split_text)
    width = input(f"enter width (minimum allowed value is {min_width}): ")
    while not width.isdigit() or int(width) < min_width:
        width = input(f"enter width (minimum allowed value is {min_width}): ")
    if len(text) <= int(width):
        if align:
            text = align_text(text, width)
        line_sum = text.strip()
    else:
        line_sum = ""
        for word in split_text:
            if len(line + word + " ") <= int(width):
                line += word + " "
            elif len(line + word + " ") > int(width):
                line = line.strip()
                if align:
                    line = align_text(line, width)
                line_sum += line + "\n"
                line = ""
        line_sum += line.strip()
    return line_sum


y_n_answers = ["Y", "N", "Υ", "Ν"]
wants_to_print = True

while wants_to_print:
    receive_multiple_line_text()
    print(formatted_print(text))
    while exit not in y_n_answers:
        exit = input("Exit? Y/N\n").upper()
        if exit in "Y, Υ":
            wants_to_print = False
        if exit in "N, Ν":
            exit = ""
            break
