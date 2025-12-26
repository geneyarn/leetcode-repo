class Test:

    def test(self):

        a = [1, 3, 4]
        pre = 0
        ans = 0
        for _ in a:
            pre += 1
            ans += pre
            print(pre)
            # print(ans)

        return ans

Test().test()