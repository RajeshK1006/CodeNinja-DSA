class Solution {
    public int maxSubArray(int[] nums) {

        int n = nums.length;

        int summ = 0;
        Integer maxi = Integer.MIN_VALUE;

    
        for(int i = 0;i<n;i++){
            summ += nums[i];

            

            maxi = Math.max(maxi,summ);

            if(summ<0){
                summ= 0;
            }

            


        }
        return maxi;

    }}
