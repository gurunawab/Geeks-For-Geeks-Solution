class Solution:
    def maxStackHeight(self, r, h):
        bit = [0] * 1002

        # Sort by radius ascending; break ties with height descending
        for rad, ht in sorted(zip(r, h), key=lambda x: (x[0], -x[1])):
            # Query max height achievable with height < ht
            val, i = 0, ht - 1
            while i > 0:
                val = max(val, bit[i])
                i -= i & -i

            # Update BIT at current height
            val += ht
            i = ht
            while i <= 1001:
                bit[i] = max(bit[i], val)
                i += i & -i

        return max(bit)