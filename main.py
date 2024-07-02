import clas

startPos = [1,3]
homePos = [2,0]
rowCosts = [5,4,3]
colCosts = [8,2,6,7]

sol = clas.Solution()
sol.minCost(startPos, homePos, rowCosts, colCosts)