class Solution:
    def canJump(self, nums: List[int]) -> bool:
    	lengthList = len(nums)
    	#Input: nums = [2,3,1,1,4]
    	#Input: nums = [3,2,1,0,4]
    	#Input: nums = [3,0,2,2,1]
    	#when jumping, check if you're still with len(nums) 
    	#iterate through nums, start off with first value, find all minumum jumps of 1 see
    	#where that lands?
    	#jump withe maxCanJump value to the next index?
    	count = 0
    	for x in nums:
    		if x != 0:
    			count += 1
    	if count == lengthList - 1:
    		return True
    	for index in range(lengthList):
    		maxCanJump = nums[index]
    		#maxcanJump + 1 bc range(1, 4) -> 1, 2, 3
    		# for posJumps in range(1, maxCanJump+1):
    			
    			# if index + posJumps == len(nums) - 1:
    			# 	return True
    			# elif index + posJumps < len(nums) - 1 and nums[index + 1] != 0:
    			# 	break
    			# elif posJumps > lengthList:
    			# 	return False
    		if maxcanJump + index >= len(lengthList) - 1:
    			#go back to prev index
    		else if maxcanJump + index <= len(lengthList - 1) and nums[maxcanJump + index] != 0:
    			index = maxcanJump + index
    		

sol = Solution()
sol.canJump(nums = [2, 3, 1, 1, 4])