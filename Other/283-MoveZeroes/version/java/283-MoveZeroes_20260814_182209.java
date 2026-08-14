// Last updated: 8/14/2026, 6:22:09 PM
1class Solution {
2    public void moveZeroes(int[] nums) {
3
4        int j = -1;
5
6        // Find the first zero
7        for (int i = 0; i < nums.length; i++) {
8
9            if (nums[i] == 0) {
10                j = i;
11                break;
12            }
13        }
14
15        // No zero in the array
16        if (j == -1) {
17            return;
18        }
19
20        // Move non-zero elements to the front
21        for (int i = j + 1; i < nums.length; i++) {
22
23            if (nums[i] != 0) {
24
25                int temp = nums[i];
26                nums[i] = nums[j];
27                nums[j] = temp;
28
29                j++;
30            }
31        }
32    }
33
34    // Time Complexity: O(n)
35    // Space Complexity: O(1)
36}