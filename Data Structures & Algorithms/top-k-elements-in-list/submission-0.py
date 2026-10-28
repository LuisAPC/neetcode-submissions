class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucketsort
        # count [idx]
        # num   [list of nums]

        freq_dict = {} #key=num val=freq
        freq_list =[[] for i in range(len(nums) + 1)]
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        for key, val in freq_dict.items():
            freq_list[val].append(key)

        top_k_frequent = []
        for idx in range(len(freq_list) - 1, 0, -1):
            num_list = freq_list[idx]
            for num in num_list:
                top_k_frequent.append(num)
                if len(top_k_frequent) == k:
                    return top_k_frequent

        return False

        #nums=[1,2,3,4,5] len=5 
        #nums=[5,5,5,5,5]
        #freq_list=[0,1,2,3,4,5] len=6