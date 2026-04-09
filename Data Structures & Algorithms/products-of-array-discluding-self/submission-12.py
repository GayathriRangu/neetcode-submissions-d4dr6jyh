class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        output = []
        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                output.append(0 if num != 0 else total_product)
            else:
                output.append(total_product // num)
        
        return output