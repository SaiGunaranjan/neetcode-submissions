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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        int l1_val, l2_val, sum_val;
        ListNode* head = new ListNode(-5);
        ListNode* tail = head;
        int carry = 0;
        while (l1 or l2)
        {
            if (l1 == nullptr)
            {
                l1_val = 0;
                l2_val = l2->val;
                l2 = l2->next;
            }
            else if (l2 == nullptr)
            {
                l1_val = l1->val;
                l2_val = 0;
                l1 = l1->next;
            }
            else
            {
                l1_val = l1->val;
                l2_val = l2->val;
                l1 = l1->next;
                l2 = l2->next;
            }
            sum_val = l1_val + l2_val + carry;
            if (sum_val >= 10)
            {
                carry = 1;
                sum_val -= 10;
            }
            else
            {
                carry = 0;
            }
            tail->next = new ListNode(sum_val);
            tail = tail->next;

        }
        if (carry == 1)
        {
            tail->next = new ListNode(1);
        }
        return head->next;
        
    }
};
