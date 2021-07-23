class Solution_1 {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int currSave=0;
        int maxSave=0;
        int initialCount=0;
      
        for(int i=0; i<customers.length; i++){
            if(grumpy[i]==0) initialCount += customers[i]; 
            currSave += customers[i] * grumpy[i];
            if(i>X-1){
                currSave -= customers[i-X]* grumpy[i-X];
            }
            maxSave = Math.max(currSave, maxSave);
        }
        return initialCount + maxSave;
    }
}




class Solution_2 {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int satisfied = 0, maxSaved = 0;
        for (int i = 0, save = 0; i < grumpy.length; ++i) {
            if (grumpy[i] == 0) { satisfied += customers[i]; }
            else { save += customers[i]; }
            if (i >= X) {
                save -= grumpy[i - X] * customers[i - X];
            }
            maxSaved = Math.max(save, maxSaved);
        }
        return satisfied + maxSaved;        
    }
}
