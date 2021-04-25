class SameOrNot:
    def sameOrNot(word1: str, word2: str):
        if len(word1) != len(word2): return False
        else:
            for i in range(len(word1)):
                if word1[i] != word2[i]: return False
        return True

    if __name__ == "__main__":
        testSamples = [
            ["a", "ab"],
            ["a", "a"],
            ["casserole", "casserole"],
            ["love", "live"],
            ["asdf", "jkl;"],
            ["longword", "long"]
            ]

        for sample in testSamples:
            print(sameOrNot(sample[0], sample[1]))
