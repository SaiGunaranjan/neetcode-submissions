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
    ListNode* reverseBetween(ListNode* head, int left, int right) {

        if (left == right)
        {
            return head;
        }
        int fp = 0;
        int sp = 0;
        ListNode* fp_head = head;
        ListNode* sp_head = head;
        ListNode* sp_prev = new ListNode(-1000,head);
        while (fp < right - 1)
        {
            if (fp >= right - left)
            {
                sp_prev = sp_head;
                sp_head = sp_head->next;
                sp += 1;
            }
            fp_head = fp_head->next;
            fp += 1;
        }
        ListNode* prev = fp_head->next;
        while (sp <= fp)
        {
            ListNode* temp = sp_head->next;
            sp_head->next = prev;
            prev = sp_head;
            sp_head = temp;
            sp += 1;
        }
        sp_prev->next = prev;

        if (left == 1)
        {
            return sp_prev->next;
        }
        else
        {
            return head;
        }
        
    }
};