/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* fp = head;
        ListNode* sp = head;
        int count = 0;
        while (fp)
        {
            if (count >= n+1)
            {
                sp = sp->next;
            }
            fp = fp->next;
            count += 1;
        }

        if (count == n)
        {
            head = head->next;
            return head;
        }

        ListNode* temp = sp->next;
        sp->next = temp->next;

        return head;
        
    }
};
