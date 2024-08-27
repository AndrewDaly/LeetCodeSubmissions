class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 1. check for edge case
        if len(prices) == 0:
            return 0
        
        # 2. check for simple O(n) solution
        min_value = min(prices)
        max_value = max(prices)
        max_theoretical_profit = max_value - min_value
        min_value_index = prices.index(min_value)
        max_value_index = prices.index(max_value)
        if min_value_index < max_value_index:
            return max_theoretical_profit
        
        # 3. A little more complicated indices don't align with max theoretical solution
        smallest_found_value = prices[0]
        largest_found_value = prices[0]
        max_profit = 0
        for i, j in enumerate(prices):
            if i == 0:
                continue
            # if we find a smallest value, update smallest value
            if j < smallest_found_value:
                smallest_found_value = j
                current_profit = largest_found_value - smallest_found_value
            if j > largest_found_value:
                largest_found_value = j
                current_profit = largest_found_value - smallest_found_value
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit
            

        
           
        

                                                            
    

