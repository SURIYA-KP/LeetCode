class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        int count = 0, i = 1, current_sum = 0;
        HashSet<Integer> b_set = new HashSet<Integer>();
        for (int j: banned){
            b_set.add(j);
        }
        while(current_sum <= maxSum - i && i <= n){
            if (!b_set.contains(i)){
                current_sum += i;
                count += 1;
            }
            i += 1;
        }
        return count;
    }
}
