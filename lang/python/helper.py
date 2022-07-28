class TestCase:
    def __init__(self, case_input, target):
        self.input = case_input
        self.target = target


TAG_NUMBER = 1


def tag_number():
    global TAG_NUMBER
    tag = TAG_NUMBER
    TAG_NUMBER = TAG_NUMBER + 1
    return tag


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.__tag = None

    def get_tag(self):
        if self.__tag is None:
            self.__tag = tag_number()
        return self.__tag

    # def __str__(self):
    #     tag = self.get_tag()
    #     l = '' if self.left is None else f"{tag}->{self.left.get_tag()} \n {self.left.__str__()} \n"
    #     r = '' if self.right is None else f"{tag}->{self.right.get_tag()} \n {self.right.__str__()} \n"
    #     return f"{tag}[label=\"{self.val}\"]\n {l} {r}"


class Token:
    def __init__(self, val, token_type):
        self.val = val
        # 1: (; 2: ), 3:string
        self.type = token_type

    def __str__(self):
        return f'val: {self.val} type: {self.type}'


def parse_binary_tree(s):
    def token(s):
        tk = []
        val = ''
        for i in s:
            if i == '(':
                tk.append(Token(i, 1))
                continue
            elif i == ')':
                if val != '':
                    tk.append(Token(val, 3))
                    val = ''
                tk.append(Token(i, 2))
                continue
            elif i == ' ':
                if val != '':
                    tk.append(Token(val, 3))
                    val = ''
                continue
            else:
                val += i
        return tk

    # 1: out (); 2 in ()
    state = 1
    # for recursion
    stack = []
    current = []
    tk = token(s)
    for k in tk:
        if k.type == 1 or k.type == 3:
            stack.append(k)
        else:
            while len(stack) > 0 and (type(stack[-1]) != Token or stack[-1].type != 1):
                current.append(stack.pop())
            if len(stack) == 0:
                raise Exception('parse error')
            else:
                # pop (
                stack.pop()
            current.reverse()
            v = l = r = None
            if len(current) == 0:
                stack.append(None)
                continue
            elif len(current) == 1:
                v = current[0].val
            elif len(current) == 2:
                v = current[0].val
                l = current[1]
            elif len(current) == 3:
                v = current[0].val
                l = current[1]
                r = current[2]
            stack.append(TreeNode(v, l, r))
            current = []

    if len(stack) == 1:
        return stack[0]

    return None


def parse_pre_order_tree(s):
    root = None

    stack = []
    idx = 0
    ch_idx = 1
    # while idx < sz:
    for n in s:
        if n is not None:
            c = TreeNode(n)
            stack.append(c)
            if root is None:
                root = c
        else:
            c = None

        if len(stack) > 0 and stack[0] != c:
            # left
            if ch_idx == 1:
                stack[0].left = c
                ch_idx = 2
            else:
                stack[0].right = c
                ch_idx = 1
                stack.pop(0)

    return root


def print_tree(tree):
    from graphviz import Source

    s = f"digraph G {{{tree}}}"
    Source(s, filename="test.gv", format="png").view()


def inorder_traver_recursive(root):
    if root is None:
        return
    inorder_traver_recursive(root.left)
    print(root.val, ' ', end='')
    inorder_traver_recursive(root.right)


def in_order_iterate(root):
    stack = []
    s = root
    while stack or (s is not None):
        while s is not None:
            stack.append(s)
            s = s.left
        s = stack.pop()
        print(s.val, ' ', end='')
        s = s.right


def morris_in_order(root):
    def pre_node(root):
        s = root.left
        while s.right and s.right != root:
            s = s.right
        return s

    s = root
    while s:
        if s.left is None:
            print(s.val, ' ', end='')
            s = s.right
        else:
            p = pre_node(s)
            if p.right:
                print(s.val, ' ', end='')
                s = s.right
                p.right = None
            else:
                p.right = s
                s = s.left





def pre_order_recursive(root):
    if root is None:
        return
    print(root.val, ' ', end='')
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)


def pre_order_iterate(root):
    stack = []
    s = root
    while stack or (s is not None):
        while s is not None:
            print(s.val, ' ', end='')
            stack.append(s)
            s = s.left
        s = stack.pop()
        s = s.right


def post_order_recursive(root):
    if root is None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.val, ' ', end='')


def post_order_iterate(root):
    """
    best explain: https://www.jianshu.com/p/456af5480cee
    """
    stack = []
    s = root
    last_visit = root
    while stack or (s is not None):
        while s is not None:
            stack.append(s)
            s = s.left
        s = stack[-1]
        if s.right is None or s.right == last_visit:
            print(s.val, ' ', end='')
            last_visit = s
            stack.pop()
            # test stack and pop stack again
            s = None
        else:
            s = s.right
