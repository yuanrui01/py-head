class Solution:
    # 2799. 统计完全子数组的数目
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        n = len(nums)
        cnt = deffaultdict(int)
        ans = 0
        left = right = 0
        while right < n:
            cnt[nums[right]] += 1
            while left <= right and len(cnt) == k:
                ans += n - right
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            right += 1
        return ans