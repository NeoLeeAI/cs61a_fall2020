class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
#2.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)
#2.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        else:
            product *= lnk.first
    return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))

#2.3
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk.rest is Link.empty:
        pass
    else:
        temp = lnk.first
        lnk.first = lnk.rest.first
        lnk.rest.first = temp
        if lnk.rest.rest:
            flip_two(lnk.rest.rest)

#2.4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    pointer = link
    while pointer != Link.empty:
        if f(pointer.first):
            yield pointer.first
        pointer = pointer.rest

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self) -> str:
        if not self.branches:
            return 'Tree({0})'.format(self.label)
        return 'Tree({0}, {1})'.format(self.label, self.branches)
   
#3.1
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    assert isinstance(t, Tree)
    if t.label % 2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

#3.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.label
    1
    >>> t.branches[0].branches[0].label
    9
    >>> t.branches[1].label
    16
    """
    assert isinstance(t, Tree)
    t.label *= t.label
    for b in t.branches:
        square_tree(b)

#3.3
def find_paths(t, entry):
    '''
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    '''
    assert isinstance(t, Tree)
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        if find_paths(b, entry):
            paths += [[t.label] + path for path in find_paths(b, entry)]
    return paths

#3.4
def combine_tree(t1, t2, combiner):
    """
    >>> from operator import mul
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    assert isinstance(t1, Tree) and isinstance(t2, Tree)
    if Tree.is_leaf(t1) and Tree.is_leaf(t2):
        return Tree(combiner(t1.label, t2.label))

    return Tree(
        combiner(t1.label, t2.label),
        [combine_tree(b[0], b[1], combiner) for b in zip(t1.branches, t2.branches)],
    ) 

#3.5
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    assert isinstance(t, Tree)
    t.label = map_fn(t.label)
    for b in t.branches:
        for b_b in b.branches:
            alt_tree_map(b_b, map_fn)
    return t