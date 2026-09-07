class Solution(object):
    def largestAltitude(self, gain):
        alt=[0,gain[0]]
        for i in range(len(gain)-1):
            gain[i+1]=gain[i]+gain[i+1]
            alt.append(gain[i+1])
        return max(alt)