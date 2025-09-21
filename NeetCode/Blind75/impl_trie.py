class TrieNode:
    def __init__(self):
        self.children={}
        self.eow = False #endOfword

class PrefixTree:
    def __init__(self):
        self.root=TrieNode() #init trie root
        
    def insert(self, word: str) -> None:
        cur=self.root #set the starting point
        for c in word:
            if c not in cur.children: # if the TrieNode of character hasn't been inserted
                cur.children[c]=TrieNode() # set new character in children list as a new TrieNode
            cur=cur.children[c] #move to next exist Trie Node
        cur.eow=True #set the eow=True


    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c] #move to next trie node
        return cur.eow #check if the word has been inserted
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c] # move on to next char
        return True #for loop finish walking prefix
        
        
