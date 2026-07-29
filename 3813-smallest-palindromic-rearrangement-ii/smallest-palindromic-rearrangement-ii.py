class Solution(object):
    def nCr(self, n, r, k):
        r = min(r, n - r)
        result = 1

        for i in range(1, r + 1):
            result = result * (n - r + i) // i
            if result >= k:
                return k

        return result

    def smallestPalindrome(self, s, k):
        n = len(s)

        mid = ""
        if n % 2 == 1:
            mid = s[n // 2]

        count = [0] * 26

        for i in range(n):
            if n % 2 == 1 and i == n // 2:
                continue
            count[ord(s[i]) - ord('a')] += 1

        # Half frequencies
        for i in range(26):
            count[i] //= 2

        half_result = []
        half = n // 2

        for _ in range(half):
            placed = False

            for j in range(26):
                if count[j] > 0:
                    count[j] -= 1

                    ways = 1
                    letters = sum(count)

                    for c in range(26):
                        if count[c] > 0:
                            ways *= self.nCr(letters, count[c], k)
                            letters -= count[c]

                        if ways >= k:
                            break

                    if ways >= k:
                        half_result.append(chr(j + ord('a')))
                        placed = True
                        break

                    k -= ways
                    count[j] += 1

            if not placed:
                return ""

        rev = half_result[::-1]

        if mid:
            half_result.append(mid)

        return "".join(half_result + rev)
        