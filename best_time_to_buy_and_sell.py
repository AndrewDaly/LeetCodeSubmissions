class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        lowest_element_so_far = prices[0]
        biggest_remaining_element = prices[0]
        for i, j in enumerate(prices):
            if i == 0:
                biggest_remaining_element = max(prices[i:len(prices)])
                current_profit = biggest_remaining_element - lowest_element_so_far
                if current_profit > max_profit:
                    max_profit = current_profit    
                continue
            lowest_element_so_far = min(prices[0:i])
            biggest_remaining_element = max(prices[i:len(prices)])
            current_profit = biggest_remaining_element - lowest_element_so_far
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit