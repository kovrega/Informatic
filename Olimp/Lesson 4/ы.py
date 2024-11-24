
#
#
#
# class BST():
#     left = None
#     right = None
#
#     def __init__(val, self):
#         self.value = val
#
#     def search(self, val):
#         if val < self.val:
#             if self.left:
#                 self.left.search(val)
#             else:
#                 return False
#         elif val > self.val:
#             if self.right:
#                 self.right.search(val)
#             else:
#                 return False
#         else:
#             return self
#
#     def paste(self, val):
#         if val < self.val:
#             if self.left:
#                 self.left.past(val)
#             else:
#                 self.left = BST(val)
#
#         elif val > self.val:
#             if self.right:
#                 self.right.past(val)
#             else:
#                 self.right = BST(val)
#
#
#
#     def get_value(self, val):
#         curr = self.right
#         while curr and curr.left:
#             curr = curr.left
#
#         return curr
#
#     def delete(self, val):
#         node = self.search(val)
#         if node == None:
#             return  # Либо raise ValueError('Нельзя удалить, то чего нет')
#
#         if node.right and node.left:
#             min_el = node.get_value(val)
#             node.val, min_el.val = min_el.val, node.val
#             min_el.delete(min_el.val)
#         elif node.right:
#             node.val, node.right.val = node.right.val, node.val
#             node.right.delete(val)
#
#         elif node.left:
#             node.val, node.left.val = node.left.val, node.val
#             node.left.delete(val)
#
#         else:
#             del node
#
#
#
#
#
#
# Tree1 = BST(2)