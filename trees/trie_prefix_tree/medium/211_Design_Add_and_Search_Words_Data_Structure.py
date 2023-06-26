# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_word

        return dfs(0, self.root)


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True
