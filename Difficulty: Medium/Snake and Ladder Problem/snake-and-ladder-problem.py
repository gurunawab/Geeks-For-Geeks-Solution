from collections import deque


class Solution:

    def minThrows(self, n, lad, sn):
        target = n * n
        board = {
            **dict(zip(lad[::2], lad[1::2])),
            **dict(zip(sn[::2], sn[1::2])),
        }
        q, vis = deque([(1, 0)]), {1}

        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps

            for dice in range(1, 7):
                nxt = curr + dice
                if nxt <= target:
                    nxt = board.get(nxt, nxt)
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt, steps + 1))

        return -1 