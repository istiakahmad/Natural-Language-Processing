import re       # regular expression package

'''
                                            Metacharacters
Character	Description	                                                                            Example
[]	        A set of characters	                                                                    "[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	            "\d"	
.	        Any character (except newline character)	                                            "he..o"	
^	        Starts with	                                                                            "^hello"	
$	        Ends with	                                                                            "world$"	
*	        Zero or more occurrences	                                                            "aix*"	
+	        One or more occurrences	                                                                "aix+"	
{}	        Exactly the specified number of occurrences	                                            "al{2}"	
|	        Either or	                                                                            "falls|stays"	
()	        Capture and group	 

                                                Special Sequences
Character	Description	                                                                                    Example
\A	        Returns a match if the specified characters are at the beginning of the string	                "\AThe"	

\b	        Returns a match where the specified characters are at the beginning or at the end of a word	    r"\bain"
                                                                                                            r"ain\b"	

\B	        Returns a match where the specified characters are present, but NOT at the beginning 
            (or at the end) of a word	                                                                    r"\Bain"
                                                                                                            r"ain\B"	

\d	        Returns a match where the string contains digits (numbers from 0-9)	                            "\d"	

\D	        Returns a match where the string DOES NOT contain digits	                                    "\D"	

\s	        Returns a match where the string contains a white space character	                            "\s"	

\S	        Returns a match where the string DOES NOT contain a white space character	                    "\S"	

\w	        Returns a match where the string contains any word characters 
            (characters from a to Z, digits from 0-9, and the underscore _ character)	                    "\w"	

\W	        Returns a match where the string DOES NOT contain any word characters	                        "\W"	

\Z	        Returns a match if the specified characters are at the end of the string	                    "Spain\Z"

                                               Sets
Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) are present	

[a-n]	    Returns a match for any lower case character, alphabetically between a and n	

[^arn]	    Returns a match for any character EXCEPT a, r, and n	

[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	

[0-9]	    Returns a match for any digit between 0 and 9	

[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	

[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
            [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: 
            return a match for any + character in the string
ruby?
Match "rub" or "ruby": the y is optional
	
ruby*
Match "rub" plus 0 or more ys
	
ruby+
Match "rub" plus 1 or more ys
	
\d{3}
Match exactly 3 digits
	
\d{3,}
Match 3 or more digits
	
\d{3,5}
Match 3, 4, or 5 digits

'''
#
# txt = "The  rain in Spain"
#
# x = re.search("^The.*Spain$", txt)          # Match
#
# x = re.findall("ai", txt)
# print(x)                                    # ['ai', 'ai']
#
# x = re.findall("Portugal", txt)             # Make a search that returns no match:
# print(x)                                    # []
#
# x = re.search("\s", txt)
# print("first white-space character locate in:", x.start())  # The first white-space character is located in position: 3
#
# x = re.search("Portugal", txt)
# print(x)                                    # None
#
# x = re.split("\s", txt)                     # Split at each white-space character:
# print(x)                                    # ['The', 'rain', 'in', 'Spain']
#
# x = re.split("\s", txt, 1)                  # Split the string only at the first occurrence:
# print(x)                                    # ['The', 'rain in Spain']
#
# x = re.sub("\s", "9", txt)                  # Replace all white-space characters with the digit "9":
# print(x)                                    # The9rain9in9Spain
#
# x = re.sub("\s+", " ", txt)                  # Replace all white-space characters with the digit "9":
# print(x)                                    # The9rain9in9Spain
#
#
# x = re.sub("\s", "9", txt, 2)           #Replace the first two occurrences of a white-space character with the digit 9:
# print(x)                                # The9rain9in Spain
#
# x = re.search("ai", txt)                #The search() function returns a Match object:
# print(x)                                # <_sre.SRE_Match object; span=(5, 7), match='ai'>
#
# '''
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
# '''
#
# x = re.search(r"\bS\w+", txt)#Search for an upper case "S" character in the beginning of a word, and print its position:
# print(x.span())              # (12, 17)
#
# x = re.search(r"\bS\w+", txt)#Search for an upper case "S" character in the beginning of a word, and print the word:
# print(x.group())             # Spain
#
# x = re.search(r"\bS\w+", txt) #The string property returns the search string:
# print(x.string)                 # The rain in Spain
#

my_string = "Let's write @RegEx! Here more than 10 rules are discussed. I would thanks to you."
# pattern = r"\s+"    # [' ', ' ']
# pattern = r"\W+"    # ["'", ' ', ' ', '!']
# pattern = r"\w"         # ['L', 'e', 't', 's', 'w', 'r', 'i', 't', 'e', 'R', 'e', 'g', 'E', 'x']
# pattern = r"\w+"    # ['Let', 's', 'write', 'RegEx']
# pattern = r"[A-Z][a-z]"  # ['Le', 'Re', 'Ex']
# pattern = r"[a-z][A-Z]"  # ['gE']
# pattern = r"[@]\w+"     # ['@RegEx']
# pattern = r"\S+"        # ["Let's", 'write', '@RegEx!']
# pattern = r"\S"        # ['L', 'e', 't', "'", 's', 'w', 'r', 'i', 't', 'e', '@', 'R', 'e', 'g', 'E', 'x', '!']
# print(re.findall(pattern, my_string))
#
# # Split my_string on sentence endings and print the result
# sentence_endings = r"[.?!]"
# print(re.split(sentence_endings, my_string))
#
# # Find all capitalized words in my_string and print the result
# capitalized_words = r"[A-Z]\w+"
# print(re.findall(capitalized_words, my_string))
#
# # Find all digits in my_string and print the result
# digits = r"\d+"
digits = r"[0-9]+"
# print(re.findall(digits, my_string))
                                            # Build Regular Expression
from nltk.tokenize import regexp_tokenize
print(regexp_tokenize(my_string, digits))

# print(re.sub(r'[aeiou]+', '-', my_string))

text = """101   COM     Computers
205   MAT   Mathematics
189   ENG    English"""

# 1. extract all course numbers
# print(re.findall('[0-9]+', text))       # ['101', '205', '189']
# 2. extract all course codes: match exactly 3 consequtive occurrences
# print(re.findall('[A-Z]{3}', text))     # ['COM', 'MAT', 'ENG']
# 3. extract all course names:  have at least 4 or more characters
# print(re.findall('[A-Za-z]{4,}', text, re.IGNORECASE)) # ['Computers', 'Mathematics', 'English']
# define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
# print(re.findall(course_pattern, text))

phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
# print("Phone Num : ", num)

# the finite-state automaton for the regular expression is compiled once and reused.
regularexpression = re.compile(r'\w+ou\w+')     # compiling regularexpression as a regex
# print(regularexpression.findall(my_string))

# (?=) syntax is defines a look ahead. It match an entity that's followed by the pattern.
pattern = re.compile(r"\w+(?=,)")
print(pattern.findall("Me, myself, and I")) # ['Me', 'myself']
pattern = re.compile(r'\w+(?=\sfox)')
print(pattern.search("The quick brown fox").group())    # brown


