class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        sug = []
        keyword = []
        products.sort()
        
        for i in range(len(searchWord)):
            keyword.append(searchWord[i])
            for j in range(len(products)):
                product_list = list(products[j])
                
                if keyword == product_list[:i+1]:
                    if len(sug) < 3:
                        sug.append(''.join(product_list))
            ans.append(sug)
            sug = []
        return ans