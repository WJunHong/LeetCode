package LinkedList;

public class ReverseLL {
    
    public ListNode curr = null;

    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return curr;
        }
        if (head.next == null) {
            head.next = curr;
            return head;
        } else {
            ListNode temp = head.next;
            head.next = curr;
            curr = head;
            return reverseList(temp);
        }

    }
}

