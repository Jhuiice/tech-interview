# ##Rearrange a LinkedList (medium)#

# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.


# first attempt (fail)

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  # TODO: Write your code here
  # find the half => reverse it => input the reveresed half into the whole on every other node
  # do this in place
  fast, slow = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next

  # slow is at middle
  # need to reverse slow
  reversed_half = reverse_node(slow)

  # do we need to know how long the length of the node is?
  # no we just need to input the reversed half into everyone so count % 2 == 0

  synced_node = head
  # use 3 nodes? The original half, reversed half, and new one to increment and replace?
  # would that increase the space complexity?

  while synced_node is not None and synced_node.next is not None:

    print(synced_node.value)
    synced_node = synced_node.next
    synced_value = synced_node.value
    synced_node.value = reversed_half.value
    reversed_half = reversed_half.next
    synced_node = synced_node.next

  return

# reverse second half of the node and return it
def reverse_node(slow):
  current = slow
  while current is not None and current.next is not None:
    prev = current.next
    next = current
    current = prev
    current.next = None

  return current



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()


# grokking actual answer
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  if head is None or head.next is None:
    return

  # find middle of the LinkedList
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  # slow is now pointing to the middle node
  head_second_half = reverse(slow)  # reverse the second half
  head_first_half = head

  # rearrange to produce the LinkedList in the required order
  while head_first_half is not None and head_second_half is not None:
    temp = head_first_half.next
    head_first_half.next = head_second_half
    head_first_half = temp

    temp = head_second_half.next
    head_second_half.next = head_first_half
    head_second_half = temp

  # set the next of the last node to 'None'
  if head_first_half is not None:
    head_first_half.next = None


def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
