# William Ikenna-Nwosu (wiknwo)
# 
# Trivial: Autori
#
# Great scientific discoveries are often named by the 
# last names of scientists that made them. For example, 
# the most popular asymmetric cryptography system, RSA was 
# discovered by Rivest, Shamir and Adleman. Another 
# notable example is the Knuth-Morris-Pratt algorithm, 
# named by Knuth, Morris and Pratt.
#
# Scientific papers reference earlier works a lot and 
# it’s not uncommon for one document to use two different 
# naming conventions: the short variation (e.g. KMP) using 
# only the first letters of authors last names and the 
# long variation (e.g. Knuth-Morris-Pratt) using complete 
# last names separated by hyphens.
# 
# We find mixing two conventions in one paper to be 
# aesthetically unpleasing and would like you to write a 
# program that will transform long variations into short.
longversion = input("Enter last names separated by hyphens: ")
shortversion = longversion[0]
for i in range(1, len(longversion)):
    if longversion[i] == '-':
        shortversion += longversion[i + 1]

    elif longversion[i].isupper() and longversion[i - 1].islower():
        shortversion += longversion[i]

print(shortversion)
