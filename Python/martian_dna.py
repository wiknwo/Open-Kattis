'''Martian DNA

    William Ikenna-Nwosu (wiknwo)

    As you are probably aware, human DNA can be 
    represented as a long string over an alphabet of size 
    four (A, C, G, T), where each symbol represents a 
    distinct nucleobase (respectively; adenine, cytosine, 
    guanine, and thymine).

    For martians, however, things are a bit different; 
    research conducted on the latest martian captured by 
    NASA revealed that martian DNA consists of a whopping 
    K distinct nucleobases! Martian DNA may thus be 
    represented as a string over an alphabet of size K.

    Now, a certain research group interested in exploiting 
    martian DNA in artificial intelligence applications 
    has requested to get a single consecutive piece of a 
    martian DNA string. For R of the nucleobases, 
    they have specified a minimum quantity of how many 
    they need of that particular nucleobase to be present 
    in their sample.

    You are interested in finding the shortest substring 
    of the DNA which satisfies their requirements.

    Input
    The first line contains three integers N, K, and R, 
    denoting the total length of the martian DNA, the 
    alphabet size, and the number of nucleobases for 
    which the researchers have a minimum quantity 
    requirement, respectively. They obey 1≤R≤K≤N.

    The second line contains N space-separated integers: 
    the complete martian DNA string. The i-th of these 
    integers, Di, indicates what nucleobase is in the 
    i-th position of the DNA string. Nucleobases are 
    0-indexed, i.e. 0≤Di<K. Each nucleobase will occur 
    at least once in the DNA string.

    Each of the following R lines contains two integers 
    B and Q representing a nucleobase and its mimimum 
    required quantity, respectively (0≤B<K,1≤Q≤N). No 
    nucleobase will be listed more than once in these 
    R lines.

    Output
    Output a single integer, the length of the shortest 
    consecutive substring of the DNA that satisfies the 
    researchers’ requirements. If no such substring exists, 
    output “impossible”.
'''
def main():
    # Parsing first line of input
    data = input('').split(' ')
    n = int(data[0]) # Total length of martian DNA
    k = int(data[1]) # Alphabet size
    r = int(data[2]) # Number of nucleobases for which the researchers have a minimum quantity requirement

    # Parsing second line of input
    data = input('')
    martian_dna_string = data.split(' ') # i-th integer, D_i indicates what nucleobase is in the i-th position of the DNA string. Each nucleobase will occur at least once in the DNA string

    # Parsing next r lines
    nucleobases_minreqquantity_dict = {}
    for i in range(r):
        data = input('').split(' ')
        b = data[0] # nucleobase
        q = int(data[1]) # minimum required quantity. No nucleobase listed more than once in these r lines
        nucleobases_minreqquantity_dict[b] = q

    # Calculating length of shortest consecutive substring 
    # of DNA that satisfies the researchers' requirements.
    # IF no such substring exists, output "impossible".
    shortest_consecutive_substring_DNA = ''
    flag = True
    for key, value in nucleobases_minreqquantity_dict.items():
        # Not enough nucleobases of type 'key'
        if martian_dna_string.count(key) < value:
            print("impossible")
            flag = False
            break
        else:
            shortest_consecutive_substring_DNA += key * value

    if flag:
        for char in martian_dna_string:
            if char not in nucleobases_minreqquantity_dict:
                shortest_consecutive_substring_DNA += char
        print(len(shortest_consecutive_substring_DNA))
    
if __name__ == '__main__':
    main()