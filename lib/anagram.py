# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,word_list):
        return [matching_word for matching_word in word_list if sorted(self.word.lower()) == sorted(matching_word.lower())] 
        

