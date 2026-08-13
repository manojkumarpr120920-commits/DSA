// Last updated: 8/13/2026, 2:15:01 PM
1class Solution {
2    public int maxProfit(int[] prices) {
3
4        int buyPrice = Integer.MAX_VALUE;
5        int maxProfit = 0;
6
7        for (int i = 0; i < prices.length; i++) {
8
9            if (buyPrice < prices[i]) {
10
11                int profit = prices[i] - buyPrice;
12
13                maxProfit = Math.max(maxProfit, profit);
14
15            } else {
16
17                buyPrice = prices[i];
18            }
19        }
20
21        return maxProfit;
22    }
23}