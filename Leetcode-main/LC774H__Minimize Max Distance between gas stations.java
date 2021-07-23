class Solution {
    public double minmaxGasDist(int[] stations, int k) {
        int n = stations.length;
        double left = 0, right = stations[n-1] - stations[0];
        
        while (left + 1e-6 < right) {
            double mid = (left + right) / 2.0;
            if (isMin (stations, k, mid)) left = mid;
            else right = mid;
        }
        return left;
    }
    
    private boolean isMin (int[] stations, int k, double x) {
        int count = 0;
        for (int i=0; i<stations.length-1; i++) 
            count += (int) ((stations[i+1] - stations[i]) / x);
        return count > k;
    }
}
