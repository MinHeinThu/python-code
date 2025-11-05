# Solution One 
# Remove the duplicate element using set
# Convert set to list
# If convert list len is the same as original list : no duplicate
# Else: duplicate
def containsDuplicate(nums):
    sett = list(set(nums))
    if len(sett) == len(nums):
        return False
    else:
        return True
    # return len(nums) != len(set(nums))


# Solution Two




    
