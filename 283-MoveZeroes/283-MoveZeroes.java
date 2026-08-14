// Last updated: 8/14/2026, 6:22:45 PM
class Solution {
    public void moveZeroes(int[] nums) {

        int j = -1;

        // Find the first zero
        for (int i = 0; i < nums.length; i++) {

            if (nums[i] == 0) {
                j = i;
                break;
            }
        }

        // No zero in the array
        if (j == -1) {
            return;
        }

        // Move non-zero elements to the front
        for (int i = j + 1; i < nums.length; i++) {

            if (nums[i] != 0) {

                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;

                j++;
            }
        }
    }

    // Time Complexity: O(n)
    // Space Complexity: O(1)
}