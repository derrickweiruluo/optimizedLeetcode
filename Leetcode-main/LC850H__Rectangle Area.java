class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        if (rectangles.length == 0 || rectangles[0].length == 0) return false;
        
        int area = 0;
        int x0 = Integer.MAX_VALUE;
        int x1 = Integer.MIN_VALUE;
        int y0 = Integer.MAX_VALUE;
        int y1 = Integer.MIN_VALUE;
        
        HashSet<String> set = new HashSet<String>();
        
        for(int[] rec : rectangles){
            area += (rec[3]-rec[1]) * (rec[2] - rec[0]);
            
            String LL = rec[0] + " " + rec[1];
            String LR = rec[2] + " " + rec[1];
            String UL = rec[0] + " " + rec[3];
            String UR = rec[2] + " " + rec[3];
            
            if(!set.add(LL)) set.remove(LL);
            if(!set.add(LR)) set.remove(LR);
            if(!set.add(UL)) set.remove(UL);
            if(!set.add(UR)) set.remove(UR);
            
            x0 = Math.min(x0, rec[0]);
            x1 = Math.max(x1, rec[2]);
            y0 = Math.min(y0, rec[1]);
            y1 = Math.max(y1, rec[3]);
            
        }
        // System.out.println(set.size());
        if(!set.contains(x0 + " " + y0) || !set.contains(x0 + " " + y1) || !set.contains(x1 + " " + y0) || !set.contains(x1 + " " + y1) || set.size() != 4) return false;
       
        return area == (x1 - x0) * (y1 - y0);
    }
}
