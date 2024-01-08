package LinkedList;

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node iter = head;
        Node next_iter = null;

        while (iter != null) {
            next_iter = iter.next;

            // Create new ListNode
            Node copy = new Node(iter.val, next_iter);
            iter.next = copy;

            iter = next_iter;
        }

        iter = head;

        while (iter != null) {

            if (iter.random != null) {
                iter.next.random = iter.random.next;
            }
            iter = iter.next.next;
        }

        iter = head;
        Node dummy_head = new Node(0);
        Node curr = dummy_head;
        while (iter != null) {
            Node temp = iter.next;
            curr.next = temp;
            curr = temp;

            iter.next = iter.next.next;
            iter = iter.next;
        }

        return dummy_head.next;
    }
}
