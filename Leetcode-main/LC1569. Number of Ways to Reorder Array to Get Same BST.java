import java.math.BigInteger;

class Solution {
    long mod = 1_000_000_007;
    public int numOfWays(int[] nums) {

        List<Integer> list = new ArrayList<>();      
        for (int n : nums) list.add(n);
        BigInteger res = helper(list).mod(BigInteger.valueOf(1000000007));
        return res.intValue() -1;
    }
    // combination
    private BigInteger comb(List<Integer> arr){
        if(arr.size() <= 2) return BigInteger.valueOf(1);  //exception case，comb运算在n<3的时候是 == 1
        //long res = 0;
        int root = arr.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for(int i=1; i<arr.size(); i++){
            if(arr.get(i) < root)
                left.add(arr.get(i));
            else
                right.add(arr.get(i)); 
        }
        // n! / (k! * (n – k)!) 
        int a = left.size();
        int b = right.size();
        int min = Math.min(a, b);
        BigInteger c1=BigInteger.ONE;
        BigInteger c2=BigInteger.ONE;
      
        //  这一步是在除去root之后，剩下的n个node分成量组(小于root的组有k个,大于的组有(n-k)个）
        // 然后 comb = n! / (k! * (n-k)!)， 简化后就是以下步骤得到当前BST层的解， res
        for(int i=0; i<min; i++){
            c1=c1.multiply(BigInteger.valueOf(a+b-i));
            c2=c2.multiply(BigInteger.valueOf(min - i));
        }
        BigInteger res = c1.divide(c2);

         // 然后 res = res * comb(left) * comb(right)
        res = res.multiply (comb(left)).multiply (comb(right));
        return res;
    }
}
