def find_duplicate(nums):
    if nums is None or not isinstance(nums, list):
        return False

    unique_nums = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in unique_nums:
            return num
        unique_nums.add(num)
    
    return False

