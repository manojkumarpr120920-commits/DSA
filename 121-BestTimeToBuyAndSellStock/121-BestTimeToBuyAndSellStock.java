// Last updated: 8/14/2026, 6:22:47 PM
class Solution {
    public int maxProfit(int[] prices) {

        int buyPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {

            if (buyPrice < prices[i]) {

                int profit = prices[i] - buyPrice;

                maxProfit = Math.max(maxProfit, profit);

            } else {

                buyPrice = prices[i];
            }
        }

        return maxProfit;
    }
}