'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Able to go circular means total available gas must be >= total cost of travel
        if sum(cost) > sum(gas):
            return -1
        
        res, balance = 0, 0
        for i in range(len(gas)):
            balance += (gas[i] - cost[i])
            if balance < 0:
                res = i + 1 # found the not ok gas station, thus, his next will be
                balance = 0
        
        return res  # no more check if pass the first check