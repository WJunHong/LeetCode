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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode curr = null;
        ListNode res = null;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                ListNode newNode = new ListNode(list1.val);
                if (curr == null) {
                    curr = newNode;
                    res = newNode;
                } else {
                    curr.next = newNode;
                    curr = curr.next;
                }
                list1 = list1.next;
            } else {
                ListNode newNode = new ListNode(list2.val);
                if (curr == null) {
                    curr = newNode;
                    res = newNode;
                } else {
                    curr.next = newNode;
                    curr = curr.next;
                }
                list2 = list2.next;
            }
        }
        while (list1 != null) {
            if (curr != null) {
                curr.next = new ListNode(list1.val);
                curr = curr.next;
            } else {
                curr = new ListNode(list1.val);
                res = curr;
            }
            list1 = list1.next;
        }
        while (list2 != null) {
            if (curr != null) {
                curr.next = new ListNode(list2.val);
                curr = curr.next;
            } else {
                curr = new ListNode(list2.val);
                res = curr;
            }
            list2 = list2.next;

        }
        return res;
    }
}