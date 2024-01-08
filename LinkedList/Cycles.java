package LinkedList;

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        } else if (head.next == null) {
            return false;
        } else {
            ListNode jump_first = head;
            ListNode jump_second = head;
            while (true) {
                jump_first = jump_first.next;
                jump_second = jump_second.next;
                if (jump_second == null) {
                    return false;
                }
                jump_second = jump_second.next;
                if (jump_second == null) {
                    return false;
                }
                if (jump_second.equals(jump_first)) {
                    return true;
                }
            }
        }
    }
}
