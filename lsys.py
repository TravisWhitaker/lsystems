######################################
# lsys.py
# General lindenmeyer system functions
# author: stphndemos
######################################

class lsystem():

    alphabet = {}
    axiom = ''
    rules = {}

    """
    params:
        alphabet:
            dictionary of possible characters as keys,
            with function to perform as value
        axiom:
            the base string (depth 0)
        rules:
            dictionary of production rules to apply
            recursively, depth times
    """
    def __init__(self, alphabet, axiom, rules):
        self.alphabet = alphabet
        self.axiom = axiom
        self.rules = rules

    """
    params:
        depth:
            how many times to recursively apply produciton rules
        tree:
            the base tree, defaults to the provided axiom
    returns:
        tree with rules applied depth times
    """
    def apply_rules(self, depth, tree = 'workaround!'):
        if tree == 'workaround!':
            tree = self.axiom
        if depth == 0:
            return tree
        out_tree = ''
        for c in tree:
            if c in self.rules:
                out_tree += self.rules[c]
            else:
                out_tree += c
        return self.apply_rules(depth-1, out_tree)

    def perform_actions(self, tree = axiom):
        for c in tree:
            self.alphabet[c]()
    
def gen_lsys(alphabet, axiom, rules, depth):
    system = lsystem(alphabet, axiom, rules)
    output = system.apply_rules(depth)
    print output
    system.perform_actions(output)

