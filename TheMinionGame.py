# Total Substrings of any string of length = n+(n-1)+(n-2)+(n-3)+...+2+1
# Total Substrings starting with vowel at position, i = Total Substrings - i
# Total Substrings starting with consonant at position, i = Total Substrings - i



def minion_game(string):
    # your code goes here
    Vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
      # Vowels
        if string[i] in Vowels:
            kevin_score += (len(string)-i)
        else:
          # Consonants
            stuart_score += (len(string)-i)
    if kevin_score > stuart_score:
        print("Kevin",kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart",stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
