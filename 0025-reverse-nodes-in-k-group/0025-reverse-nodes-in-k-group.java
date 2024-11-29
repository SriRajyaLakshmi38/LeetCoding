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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || head.next == null || k == 1) return head;
        int count = 1;
        ListNode node = head, tempHead = head, tempPrev = null;
        while (node != null) {
            if (count == k) {
                ListNode tempLast = node.next;
                node.next = null;
                if (tempHead == head) head = reverseList(tempHead);
                else tempPrev.next = reverseList(tempHead);
                tempHead.next = tempLast;
                tempPrev = node = tempHead;
                tempHead = tempHead.next;
                count = 0;
            }
            count++;
            node = node.next;
        }
        return head;
    }
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = curr == null ? null : head.next;
        while (curr != null) {
            curr.next = prev;
            prev = curr;
            curr = next;
            next = next == null ? next  : next.next;
        }
        return prev;
    }
}