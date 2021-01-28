class Solution:

    def rotate(self, m: list[list[int]]) -> None:
        l = len(m)
        for i in range(l // 2):
            for j in range(i, l - i - 1):
                m[i][j], m[j][l-1-i], m[l-1-i][l-1-j], m[l-1-j][i] = (
                        m[l-1-j][i], m[i][j], m[j][l-1-i], m[l-1-i][l-1-j])


if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    s.rotate(matrix)
    print(matrix)

