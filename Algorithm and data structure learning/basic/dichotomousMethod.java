class Solution {
    public int search(int[] nums, int target) {
        int left=0; //函数下标
        int right=nums.length-1;  //上标，-1防止溢出
        while(left<=right){ //当上下标相同或下标小于上标时，退出程序
            int middle=left+((right-left)/2); //移动中值选择器
            if(nums[middle]>target){
                right=middle-1; //大于要找的数字，缩小右区间
            }else if(nums[middle]<target){  //小于要找的数字，缩小左区间
                left=middle+1;
            }else{  //找到了，返回所在的数组下标
                return middle;
            }
        }

        return -1;
    }
}