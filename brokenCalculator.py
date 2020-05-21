'''
Time Complexity: O(log Y) -> as we do /2 atleast once
Space Complexity: O(n)
Did this code successfully run on Leetcode : Yes
Explanation:
For Y>X
Start from the reverse ie Start from Y to X and change * to / and + to -. So whenever even we divide so
we get whole number and whenever odd we subtract. Do this until Y<X and count steps.
For X>Y we can get number of steps by doing X-Y.
At the end we need to do number of steps + X-Y to account for missing a step due to Y<X and to take care of X>Y cases.

For eg.
Eg 5 and 8
        steps = 1 and now Y<X we need to add the difference also to it
        that is 1 so return 1+1=2 steps

'''
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # Idea start from back
        '''
        can't do this
        if X > Y:
            return X-Y add this in the end.
        Eg 5 and 8
        steps = 1 and now Y<X we need to add the difference also to it
        that is 1 so return 1+1=2 steps
        '''

        count = 0
        while Y > X:
            if Y % 2 == 0:
                Y = Y // 2
            else:
                Y += 1
            count += 1

        # Adding X-Y case for X>Y here
        return count + X - Y
