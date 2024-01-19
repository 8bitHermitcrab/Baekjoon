class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = ''
        codes = []
        
        for word in words:
            for i in word:
                code += morse_code[ord(i)-97]
            codes.append(code)
            code = ''
        return len(set(codes))