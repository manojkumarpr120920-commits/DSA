// Last updated: 8/13/2026, 2:29:29 PM
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