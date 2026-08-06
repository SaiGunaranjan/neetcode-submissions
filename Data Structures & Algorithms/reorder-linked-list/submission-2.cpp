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
    void reorderList(ListNode* head) {

        std::vector<int> arr;
        ListNode* tail = head;

        while (tail)
        {
            arr.push_back(tail->val);
            tail = tail->next;
        }

        int num_ele = arr.size();
        bool flag = true;
        vector<int> ind_arr;
        int lp = -1;
        int rp = num_ele;
        for (int i = 0; i < num_ele; i++)
        {
            if (flag == true)
            {
                lp += 1;
                ind_arr.push_back(lp);
                flag = false;
            }
            else
            {
                rp -= 1;
                ind_arr.push_back(rp);
                flag = true;
            }
        }
        tail = head;
        for (int i = 1; i < num_ele; i++)
        {
            tail->next = new ListNode(arr[ind_arr[i]]);
            tail = tail->next;
        }
        
    }
};
