// Last updated: 8/15/2026, 12:30:04 AM
1class Solution {
2    public int singleNumber(int[] nums) {
3
4        int ans = 0;
5
6        for (int num : nums) {
7            ans = ans ^ num;
8        }
9
10        return ans;
11    }
12
13    // Time Complexity: O(n)
14    // Space Complexity: O(1)
15}