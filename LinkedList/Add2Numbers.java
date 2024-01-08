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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy_head = new ListNode(0);
        ListNode curr = dummy_head;
        int carry_over = 0;

        while (l1 != null && l2 != null) {
            int remainder = (l1.val + l2.val + carry_over) % 10;
            carry_over = (l1.val + l2.val + carry_over) / 10;

            ListNode temp = new ListNode(remainder);
            curr.next = temp;
            curr = temp;

            l1 = l1.next;
            l2 = l2.next;
        }

        while (l1 != null) {
            int remainder = (l1.val + carry_over) % 10;
            carry_over = (l1.val + carry_over) / 10;

            ListNode temp = new ListNode(remainder);
            curr.next = temp;
            curr = temp;

            l1 = l1.next;            
        }

        while (l2 != null) {
            int remainder = (l2.val + carry_over) % 10;
            carry_over = (l2.val + carry_over) / 10;

            ListNode temp = new ListNode(remainder);
            curr.next = temp;
            curr = temp;

            l2 = l2.next;   
        }

        if (carry_over == 1) {
            ListNode temp = new ListNode(1);
            curr.next = temp;
            curr = temp;
        }

        return dummy_head.next;
    }
}
