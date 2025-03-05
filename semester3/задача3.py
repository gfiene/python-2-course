class Solution(object):
    def merge(self, intervals):
        ints = intervals
        ints.sort() 
        print(ints)
        i = 0
        while i+1 <= len(ints)-1:
            print(ints[i], ints[i+1])
            if ints[i][1] >= ints[i+1][0]:
                if ints[i+1][1] > ints[i][1]:
                    ints[i] = [ints[i][0], ints[i+1][1]]
                else: ints[i] = [ints[i][0], ints[i][1]]
                del ints[i+1]
            else: i+= 1
        return intervals
