class Solution {
    public int singleNumber(int[] nums) {

        int ans = 0;

        for (int num : nums) {
            ans = ans ^ num;
        }

        return ans;
    }

    // Time Complexity: O(n)
    // Space Complexity: O(1)
}