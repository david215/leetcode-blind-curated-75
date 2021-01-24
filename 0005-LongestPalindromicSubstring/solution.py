class Solution:

    def longest_palindrome(self, s: str) -> str:
        def expand_around_center(s: str, i: int, j:int) -> str:
            lo, hi = i, i
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break;
                if j - i > hi - lo:
                    lo, hi = i, j
                i -= 1
                j += 1
            return s[lo:hi+1]  # include char at hi

        l = []
        length = len(s)
        for i in range(length - 1):
            l.append(expand_around_center(s, i, i))
            l.append(expand_around_center(s, i, i + 1))
        l.append(expand_around_center(s, length - 1, length - 1))
        return max(l, key=lambda s: len(s))


if __name__ == "__main__":
    s = Solution()
    print(s.longest_palindrome("twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"))

