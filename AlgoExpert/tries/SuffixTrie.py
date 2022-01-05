testcases = [
    {
        'input': {
            "classMethodsToCall": [
                {
                    "arguments": ["abc"],
                    "method": "contains"
                }
            ],
            "string": "babc"
        },
        'output': {
            "methodCallResults": [
                {
                    "arguments": ["abc"],
                    "method": "contains",
                    "output": True
                }
            ],
            "trie": {
                "a": {
                    "b": {
                        "c": {
                            "*": True
                        }
                    }
                },
                "b": {
                    "a": {
                        "b": {
                            "c": {
                                "*": True
                            }
                        }
                    },
                    "c": {
                        "*": True
                    }
                },
                "c": {
                    "*": True
                }
            }
        }
    },
    {
        'input': {
            "classMethodsToCall": [
                {
                    "arguments": ["t"],
                    "method": "contains"
                },
                {
                    "arguments": ["st"],
                    "method": "contains"
                },
                {
                    "arguments": ["est"],
                    "method": "contains"
                },
                {
                    "arguments": ["test"],
                    "method": "contains"
                },
                {
                    "arguments": ["tes"],
                    "method": "contains"
                }
            ],
            "string": "test"
        },
        'output': {
            "methodCallResults": [
                {
                    "arguments": ["t"],
                    "method": "contains",
                    "output": True
                },
                {
                    "arguments": ["st"],
                    "method": "contains",
                    "output": True
                },
                {
                    "arguments": ["est"],
                    "method": "contains",
                    "output": True
                },
                {
                    "arguments": ["test"],
                    "method": "contains",
                    "output": True
                },
                {
                    "arguments": ["tes"],
                    "method": "contains",
                    "output": False
                }
            ],
            "trie": {
                "e": {
                    "s": {
                        "t": {
                            "*": True
                        }
                    }
                },
                "s": {
                    "t": {
                        "*": True
                    }
                },
                "t": {
                    "*": True,
                    "e": {
                        "s": {
                            "t": {
                                "*": True
                            }
                        }
                    }
                }
            }
        }
    },
    {
        'input': {
          "classMethodsToCall": [
            {
              "arguments": ["t"],
              "method": "contains"
            },
            {
              "arguments": ["st"],
              "method": "contains"
            },
            {
              "arguments": ["est"],
              "method": "contains"
            },
            {
              "arguments": ["test"],
              "method": "contains"
            },
            {
              "arguments": ["ttest"],
              "method": "contains"
            },
            {
              "arguments": ["sttest"],
              "method": "contains"
            },
            {
              "arguments": ["esttest"],
              "method": "contains"
            },
            {
              "arguments": ["testtest"],
              "method": "contains"
            },
            {
              "arguments": ["tt"],
              "method": "contains"
            }
          ],
          "string": "testtest"
        },
        'output': {
          "methodCallResults": [
            {
              "arguments": ["t"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["st"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["est"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["test"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["ttest"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["sttest"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["esttest"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["testtest"],
              "method": "contains",
              "output": True
            },
            {
              "arguments": ["tt"],
              "method": "contains",
              "output": False
            }
          ],
          "trie": {
            "e": {
              "s": {
                "t": {
                  "*": True,
                  "t": {
                    "e": {
                      "s": {
                        "t": {
                          "*": True
                        }
                      }
                    }
                  }
                }
              }
            },
            "s": {
              "t": {
                "*": True,
                "t": {
                  "e": {
                    "s": {
                      "t": {
                        "*": True
                      }
                    }
                  }
                }
              }
            },
            "t": {
              "*": True,
              "e": {
                "s": {
                  "t": {
                    "*": True,
                    "t": {
                      "e": {
                        "s": {
                          "t": {
                            "*": True
                          }
                        }
                      }
                    }
                  }
                }
              },
              "t": {
                "e": {
                  "s": {
                    "t": {
                      "*": True
                    }
                  }
                }
              }
            }
          }
        }
    }
]

from lib import run_tests


def main():
    tc = testcases[2]
    kls = SuffixTrie(tc['input']['string'])
    assert(tc['output']['trie'] == kls.root)
    calls = tc['input']['classMethodsToCall']
    for c in calls:
        getattr(kls, c['method'])(*c['arguments'])


# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self._add_item(string[i:])

    def _add_item(self, string):
        node = self.root
        for s in string:
            if s not in node:
                node[s] = {}
            node = node[s]
        node[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        tmp = self.root
        for s in string:
            if s not in tmp:
                return False
            tmp = tmp[s]
        return self.endSymbol in tmp
