class Node {
  constructor(data=null) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor(data=null) {
    this.head = new Node(data)
    this.prev = null
    this.size = data ? 1 : 0
  }

  push(val) {
    let head = this.head
    this.head = new Node(val)
    this.head.next = head
    this.size++
  }

  pop() {
    // popping tail becauset this is a linked list and not a stack
    let head = this.head
    while (this.head.next.next) {
      console.log(this.head)
      if (this.head.next.next == null) {
        this.head.next = null
      }
      this.head = this.head.next
    }
    console.log(this.head)
    this.size--
  }

  printList() {
    let head = this.head
    while (head) {
      console.log(head.data)
      head = head.next
    }
  }
}

node = new LinkedList(1)
node.push(2)
node.push(3)
node.printList()
node.pop()
node.printList()
node.push(43)
node.printList()
// console.log(node.size)