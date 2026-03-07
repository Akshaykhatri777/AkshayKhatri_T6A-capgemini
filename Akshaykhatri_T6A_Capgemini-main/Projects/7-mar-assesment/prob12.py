class Solution:
    def unique_products(self, products):
        result = []
        
        for i in products:
            if products.count(i) == 1:
                result.append(i)

        return result