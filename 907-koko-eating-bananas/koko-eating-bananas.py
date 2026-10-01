class Solution(object):
 def minEatingSpeed(self, piles, h):
     import math

     def isValid(k):
         hours = sum(math.ceil(pile / float(k)) for pile in piles)
         return hours <= h

     left = 1
     right = max(piles)

     while left < right:
         mid = (left + right) // 2
         if isValid(mid):
             right = mid
         else:
             left = mid + 1

     return left