class Solution:
    def low_stock_products(self, inventory):
        result = []
        
        for product, qty in inventory.items():
            if qty < 10:
                result.append(product)
        
        return result