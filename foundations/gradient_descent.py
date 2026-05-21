class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        i=0
        while i<(iterations):

            newx= init-(learning_rate*init*2)
            init=newx
            i=i+1

        return round(init,5)

