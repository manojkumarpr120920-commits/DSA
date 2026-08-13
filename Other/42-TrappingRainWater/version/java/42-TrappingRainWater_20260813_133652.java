// Last updated: 8/13/2026, 1:36:52 PM
1class Solution {
2
3    public int trap(int height[]) {
4
5        int n = height.length;
6
7        // Left maximum
8        int leftMax[] = new int[n];
9
10        leftMax[0] = height[0];
11
12        for (int i = 1; i < n; i++) {
13            leftMax[i] = Math.max(height[i], leftMax[i - 1]);
14        }
15
16        // Right maximum
17        int rightMax[] = new int[n];
18
19        rightMax[n - 1] = height[n - 1];
20
21        for (int i = n - 2; i >= 0; i--) {
22            rightMax[i] = Math.max(height[i], rightMax[i + 1]);
23        }
24
25        // Calculate trapped water
26        int trappedWater = 0;
27
28        for (int i = 0; i < n; i++) {
29
30            int waterLevel = Math.min(leftMax[i], rightMax[i]);
31
32            trappedWater += waterLevel - height[i];
33        }
34
35        return trappedWater;
36    }
37}