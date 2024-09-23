class Solution {
    public int majorityElement(int[] nums) {
        int cnt1 = 0;
        Integer ele = null;
        int n = nums.length ;
        for(int i=0;i<n;i++){
            if(cnt1==0){
                ele = nums[i];
                cnt1 = 1;
            }
            else if (nums[i] == ele){
                cnt1++;
            }
            else{
                cnt1--;
                
            }
        }

        int cnt2 = 0;
        for(int i = 0;i<n;i++){
            if (nums[i] == ele){
                cnt2++;
            }
        }       

        if (cnt2> (int) n/2){
            return ele;
        }
        
        return -1;
    }
}
