"""
Search Suggestions System
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3762/
"""
"""
Given an array of strings products and a string searchWord. We want to design a 
system that suggests at most three product names from products after each 
character of searchWord is typed. Suggested products should have common prefix 
with the searchWord. If there are more than three products with a common prefix 
return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of 
searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.

1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.

1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
testcases = {
    '1': ([
              ["mobile", "mouse", "moneypot", "monitor", "mousepad"], 'mouse'
          ],
          [
              ["mobile", "moneypot", "monitor"],
              ["mobile", "moneypot", "monitor"],
              ["mouse", "mousepad"],
              ["mouse", "mousepad"],
              ["mouse", "mousepad"]
          ]),
    '2': ([
              ["havana"], "havana"
          ],
          [
              ["havana"],
              ["havana"],
              ["havana"],
              ["havana"],
              ["havana"],
              ["havana"]
          ]),
    '3': ([
            ["bags", "baggage", "banner", "box", "cloths"], "bags"
          ],
          [
              ["baggage", "bags", "banner"],
              ["baggage", "bags", "banner"],
              ["baggage", "bags"],
              ["bags"]
          ]),
    '4': ([
            ["havana"], "tatiana"
          ],
          [
              [],
              [],
              [],
              [],
              [],
              [],
              []
          ]),
}

from typing import List


"""
41 / 41 test cases passed.
Status: Accepted
Runtime: 604 ms
Memory Usage: 17.5 MB
"""


# Loop avg. cost: 0.05321502685546875 ms
class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cache = dict((searchWord[:i+1], []) for i in range(len(searchWord)))
        for product in products:
            for i, word in enumerate(cache):
                if len(cache[word]) < 3 and word == product[:i+1]:
                    cache[word].append(product)
        return [arr for arr in cache.values()]


"""
41 / 41 test cases passed.
Status: Accepted
Runtime: 480 ms
Memory Usage: 17.2 MB
"""


# Loop avg. cost: 0.03192424774169922 ms
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        prefix = ''
        for sw in searchWord:
            prefix += sw
            arr = [prod for prod in products if prod.startswith(prefix)]
            arr.sort()
            result.append(arr[:3])
        return result
