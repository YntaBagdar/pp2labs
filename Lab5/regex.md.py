#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.


import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))





#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


import re
def match(text):
        model = 'ab{2,3}'
        if re.search(model,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("ab"))
print(match("aabbbbbc"))




#Write a Python program to find sequences of lowercase letters joined with a underscore.


import re
def text1(text):
        result = '^[a-z]+_[a-z]+$'
        if re.search(result,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text1("aab_cbbbc"))
print(text1("aab_Abbbc"))
print(text1("Aaab_abbbc"))







#Write a Python program to find the sequences of one upper case letter followed by lower case letters.



import re
def text_match1(text):
        patterns1 = '[A-Z]+[a-z]+$'
        if re.search(patterns1, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match1("AaBbGg"))
print(text_match1("Python"))
print(text_match1("python"))
print(text_match1("PYTHON"))
print(text_match1("aA"))
print(text_match1("Aa"))






#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


import re
def text_match2(text):
        patterns2 = 'a.*?b$'
        if re.search(patterns2,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match2("aabbbbd"))
print(text_match2("aabAbbbc"))
print(text_match2("accddbbjjjb"))








#Write a Python program to replace all occurrences of space, comma, or dot with a colon.





import re
my_text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", my_text))




#Write a python program to convert snake case string to camel case string.


def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))






#Write a Python program to split a string at uppercase letters.


import re
Text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', Text))






#Write a Python program to insert spaces between words starting with capital letters.


import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))





#Write a Python program to convert a given camel case string to snake case.




def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))