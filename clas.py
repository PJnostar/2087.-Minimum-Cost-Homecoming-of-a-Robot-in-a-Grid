# Solution to 2078 Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution(object):

    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        print("start position: ", startPos)
        print("home position: ", homePos)
        total_cost = 0
   
        #go down    sum(list[n:m]) gives a sum of elements of list starting from index n to m-1
        #           When we go down, we dont add the cost of first index (aka startpos[0]). First added cost is startpos[0]+1
        #           Last element in the sum is homepos[0]+1, because sum stops counting at m-1 index. We need to count m as well, hence the "+1"
        #           This is dumb but it works.
        #           This same logic applies to going right
        if (startPos[0]<homePos[0]):
            total_cost += sum(rowCosts[startPos[0]+1:homePos[0]+1])
        #go up      In this case the stupidity of sum() is advantegous, because if we count sum(rowCosts[homePos[0]:startPos[0]]) 
        #           it automatically doesnt count the "last" step (aka startPos[0]) 
        #           This same logic applied to going left
        if (startPos[0]>homePos[0]):
            total_cost += sum(rowCosts[homePos[0]:startPos[0]])
        #go left
        if (startPos[1]>homePos[1]):
            total_cost += sum(colCosts[homePos[1]:startPos[1]])
        #go right
        if (startPos[1]<homePos[1]):
            total_cost += sum(colCosts[startPos[1]+1:homePos[1]+1])

        print(total_cost)
        return total_cost