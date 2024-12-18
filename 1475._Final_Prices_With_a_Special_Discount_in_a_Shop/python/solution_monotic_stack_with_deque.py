class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        m_stack = deque()
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            while(m_stack and m_stack[-1] > price):
                m_stack.pop()
            if m_stack:
                prices[i] -= m_stack[-1]
            m_stack.append(price)
        return prices
