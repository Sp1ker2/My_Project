class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f'TreeNode({self.value})'


# Создаем корневой узел дерева
root_node = TreeNode("A")

# Создаем потомков для корневого узла
child_b = TreeNode("B")
child_c = TreeNode("C")


# Добавляем потомков к корневому узлу
root_node.add_child(child_b)
root_node.add_child(child_c)


# Создаем потомков для узла "B"
child_e = TreeNode("D")
child_f = TreeNode("E")

# Добавляем потомков к узлу "B"
child_b.add_child(child_e)
child_b.add_child(child_f)

# Создаем потомков для узла "C"
child_g = TreeNode("F")
child_h = TreeNode("G")

# Добавляем потомков к узлу "C"
child_c.add_child(child_g)
child_c.add_child(child_h)

# Выводим дерево
print(root_node)
for child in root_node.children:
    print(f"--{child}")
    for grandchild in child.children:
        print(f"----{grandchild}")
