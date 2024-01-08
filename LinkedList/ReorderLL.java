package LinkedList;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode fast = head;
        ListNode faster = head;
        while (faster.next != null && faster.next.next != null) {
            fast = fast.next;
            faster = faster.next.next;
        }

        ListNode lastOfFirstHalf = fast;
        ListNode firstOfSecondHalf = fast.next;
        while (firstOfSecondHalf.next != null) {
            ListNode current = firstOfSecondHalf.next;
            firstOfSecondHalf.next = current.next;
            current.next = lastOfFirstHalf.next;
            lastOfFirstHalf.next = current;
        }

        fast = head;
        faster = lastOfFirstHalf.next;
        while (fast != lastOfFirstHalf) {
            lastOfFirstHalf.next = faster.next;
            faster.next = fast.next;
            fast.next = faster;
            fast = faster.next;
            faster = lastOfFirstHalf.next;
        }
    }
}