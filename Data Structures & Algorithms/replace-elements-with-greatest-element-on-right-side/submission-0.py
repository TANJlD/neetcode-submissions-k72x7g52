class Solution:
    def replaceElements(self, arr : List[int]) -> List[int]:
        great = 0

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                great = arr[i]
                arr[i] = -1
            else:
                c = great 
                great = max(great, arr[i])
                arr[i] = c 

        return arr
        
                
