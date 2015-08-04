__author__ = 'Soheil'
import re
with open("SwapElements.txt", "r") as my_text:
    for line in my_text:
        elements, positions = line.rstrip("\n").split(" : ")
        print elements
        print positions
        poses = re.findall('\d+',positions) # re.findall searches a patern in a string
        print "poses: ", poses

        nums = elements.split()
        print "nums: ", nums
        for i in range(0,len(poses),2):
            nums[int(poses[i])], nums[int(poses[i+1])] = nums[int(poses[i+1])], nums[int(poses[i])]
        print ' '.join(nums)
