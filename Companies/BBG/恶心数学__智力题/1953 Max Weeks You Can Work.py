'''
You can work on the projects following these two rules:

1.  Every week, you will finish exactly one milestone of one project. You must work every week.
2.  You cannot work on two milestones from the same project for two consecutive weeks.

Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will stop working. Note that you may not be able to finish every project's milestones due to these constraints.

Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.
'''

# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        _sum, _max = sum(milestones), max(milestones)
		# (_sum - _max) is the sum of milestones from (2) the rest of projects, if True, we can form another project with the same amount of milestones as (1)
		# can refer to the section `Why the greedy strategy works?` for the proof
        
        
        if _sum - _max >= _max:  
            return _sum
        return 2 * (_sum - _max) + 1  # start from the project with most milestones (_sum - _max + 1) and work on the the rest of milestones (_sum - _max)

    
    
# corner case:
# [5,5,3] --> [2,2,3] --> [2,2,2]: 全都可以完成 == 13
# [5,3,2,1] --> tot >= 5 * 2: 全都可以完成 == 
# [5,2,1] --> tot < 5 * 2: == 1 + 2 + 3 + (1) = 7