// Last updated: 8/14/2026, 6:22:44 PM
class Solution {
    public int removeDuplicates(int[] nums) {

        int i = 0;

        for (int j = 1; j < nums.length; j++) {

            if (nums[j] != nums[i]) {
                nums[i + 1] = nums[j];
                i++;
            }
        }

        return i + 1;
    }
}