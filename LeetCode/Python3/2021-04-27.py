class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        used_ladder = {}
        used_bricks = 0
        min_ladder = float('inf')
        n_ladder = 0
        for idx in range(len(heights)-1):
            diff = heights[idx+1] - heights[idx]
            if diff <= 0:
                continue
            if n_ladder < ladders:
                used_ladder[diff] = used_ladder.get(diff, 0) + 1
                min_ladder = min(diff, min_ladder)
                n_ladder += 1
                continue
            if diff < min_ladder or ladders == 0:
                used_bricks += diff
            else:
                used_ladder[min_ladder] -= 1
                if used_ladder[min_ladder] == 0:
                    del used_ladder[min_ladder]
                used_bricks += min_ladder
                used_ladder[diff] = used_ladder.get(diff, 0) + 1
                min_ladder = min(used_ladder)
            if used_bricks > bricks:
                return idx
        return idx + 1
