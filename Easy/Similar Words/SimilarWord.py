def countSimilar(wordList: list, targetWord: str):
    wordCount = 0
    for word in wordList:
        if isSimilar(word, targetWord):
            wordCount += 1
    return wordCount

def isSimilar(word1: str, word2: str):
    set1 = set(word1)
    set2 = set(word2)
    return set1.difference(set2) == set()


if __name__ == "__main__":
    wordList = [ "velo", "low", "vole",
                 "lovee", "volvelle", "lowly",
                 "lover", "levo", "loved", "lovelovee",
                 "lowe", "lowes", "lovely", "lowan",
                 "lowa", "evolve", "loves", "volvelle", "lowed" ]
    targetWord = "love"

    print(countSimilar(wordList, targetWord))
