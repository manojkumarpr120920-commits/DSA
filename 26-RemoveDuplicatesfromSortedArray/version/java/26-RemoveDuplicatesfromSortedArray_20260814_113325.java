// Last updated: 8/14/2026, 11:33:25 AM
1class Solution {
2    public int removeDuplicates(int[] nums) {
3
4        int i = 0;
5
6        for (int j = 1; j < nums.length; j++) {
7
8            if (nums[j] != nums[i]) {
9                nums[i + 1] = nums[j];
10                i++;
11            }
12        }
13
14        return i + 1;
15    }
16}