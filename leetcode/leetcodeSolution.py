Problem 1:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l=[i,j]
                    return l

        return

Problem 242:
class Solution(object):
    def isAnagram(self, s, t):
        s=list(s)
        t=list(t)
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

Problem 206
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=[]
        if head==None:
            return a
        while(head.next):
            a.append(head.val)
            head=head.next
        a.append(head.val)
        a=a[::-1]
        return a

Problem 121
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp=0
        for i in range(len(prices)):
            if prices[i]<max(prices[i:len(prices)]):
                if max(prices[i:len(prices)])-prices[i]>maxp:
                    maxp=max(prices[i:len(prices)])-prices[i]
        return maxp

Problem 412
class Solution(object):
    def fizzBuzz(self, n):
        result=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%5==0:
                result.append("Buzz")
            elif i%3==0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result

        """
        :type n: int
        :rtype: List[str]
        """

Problem 62
class Solution(object):
    def uniquePaths(self, m, n):
        a = [[0 for x in range(m)] for y in range(n)]
        for i in range(len(a[0])):
            #print(i)
            a[0][i]=1
        #print(a)
        for j in range(len(a)):
            a[j][0]=1
        #print(a)
        for i in range(1,len(a)):
            for j in range(1,len(a[i])):
                a[i][j]=a[i-1][j]+a[i][j-1]
        result=a[len(a)-1][len(a[0])-1]
        return result

Problem 77
from itertools import combinations
class Solution(object):

    def combine(self, n, k):
        x=[]
        for i in range(1,n+1):
            x.append(i)
        z=(list(combinations(x,k)))
        for j in range(len(z)):
            z[j]=list(z[j])
        return z

Problem 128
class Solution(object):
    def longestConsecutive(self, nums):

        nums=set(nums)
        nums=list(nums)
        nums=sorted(nums)
        #print(nums)
        counter=1
        ans=1
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if abs(nums[i+1]-nums[i])==1:

                counter=counter+1
            else:
                if counter>ans:
                    ans=counter
                counter=1
        if counter>ans:
            ans=counter
        return ans
