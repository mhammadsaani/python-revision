morse_code_chars_dic = {'A': '.9', 'B': '9...', 'C': '9.9.', 'D': '9..', 'E': '·', 'F': '..9.', 'G': '99.', 'H': '....', 'I': '..', 'J': '.999', 'K': '9.9', 'L': '.9..', 'M': '99', 'N': '9.', 'O': '999', 'P': '.99.', 'Q': '99.9', 'R': '.9.', 'S': '...', 'T': '9', 'U': '..9', 'V': '...9', 'W': '.99', 'X': '9..9', 'Y': '9.99', 'Z': '99..'}
    
    
def password_generator(website_name):
    if len(website_name) < 5:
        return "Give website with a name lenght more than 5"
    website_name = website_name[0:5]
    password = morse_code_chars_dic.get(website_name[0].upper()) + "5" + website_name[1].lower() + morse_code_chars_dic.get(website_name[2].upper()) + "3" + website_name[3].lower() + morse_code_chars_dic.get(website_name[4].upper()) + "1JythoN"
    return password
    
print(password_generator("gmail"))














