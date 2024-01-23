from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # sentence 중복 알파벳 set으로 제거
        set_sent = set(sentence)
        
        # sentence와 ascii_lowercase 비교
        if set_sent == set(ascii_lowercase):
            return True
        else:
            return False