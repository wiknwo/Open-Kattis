'''Alphabet Spam

    William Ikenna-Nwosu (wiknwo)

    About 90 percent of the 300 billion emails sent every 
    day are spam. Thus, a fast spam detection mechanism is 
    crucial for large email providers. Lots of spammers try 
    to circumvent spam detection by rewriting words like 
    “M0n3y”, “Ca$h”, or “Lo||ery”.
    
    A very simple and fast spam detection mechanism is based 
    on the ratios between whitespace characters, lowercase 
    letters, uppercase letters, and symbols. Symbols are 
    defined as characters that do not fall in one of the 
    first three groups.

    Input
    The input consists of:

    one line with a string consisting of at least 1 and at 
    most 100000 characters.

    A preprocessing step has already transformed all 
    whitespace characters to underscores (_), and the line 
    will consist solely of characters with ASCII codes 
    between 33 and 126 (inclusive).

    Output
    Output four lines, containing the ratios of whitespace 
    characters, lowercase letters, uppercase letters, and 
    symbols (in that order). Your answer should have an 
    absolute or relative error of at most 10−6.
'''
def main():
    datastr = input("")
    ratio_whitespace_chars = 0
    ratio_lowercase_letters = 0
    ratio_uppercase_letters = 0
    ratio_symbols = 0

    # Iterate over string and assess each character
    for char in datastr:
        if char == '_':
            ratio_whitespace_chars += 1
        elif char.islower():
            ratio_lowercase_letters += 1
        elif char.isupper():
            ratio_uppercase_letters += 1
        elif not char.isalpha() and not char == '_':
            ratio_symbols += 1

    # Calculate ratios
    ratio_whitespace_chars /= len(datastr)
    ratio_lowercase_letters /= len(datastr)
    ratio_uppercase_letters /= len(datastr)
    ratio_symbols /= len(datastr)

    # Print results
    print(ratio_whitespace_chars)
    print(ratio_lowercase_letters)
    print(ratio_uppercase_letters)
    print(ratio_symbols)

if __name__ == '__main__':
    main()