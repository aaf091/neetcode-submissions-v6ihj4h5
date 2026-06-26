class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def t_bananas(speed, num):
            if num%speed==0:
                return num//speed
            return num//speed + 1
        l=1
        r=max(piles)
        L=len(piles)
        while l<=r:
            current_speed = (l+r)//2
            current_time = sum(t_bananas(current_speed, pile) for pile in piles)
            if current_time>h:
                l=current_speed+1
            else:
                r=current_speed-1
        return l
