################
# THIS GIVES TLE
################
class Solution(object):
    def c(self, ls, r, chosen):
        if r > len(ls):
            return None

        if r == 0:
            # return [chosen]
            return [chosen]

        biglist = []
        schosen = set(chosen)
        for i in range(0, len(ls)):
            if ls[i] in schosen: continue
            # if ls[i] in chosen: continue
            biglist.extend(self.c(ls, r - 1, chosen+[ls[i]]))
        return biglist

    def convertToTime(self, ls):
        timeString = ""
        hours = 0
        minutes = 0
        for i in ls:
            if i[-1] == "h":
                hours += int(i[:-1])
            elif i[-1] == "m":
                minutes += int(i[:-1])
        if hours >= 12 or minutes >= 60:
            return None
        timeString = str(hours)
        timeString += ":"
        if minutes < 10:
            timeString += "0"+str(minutes)
        else:
            timeString += str(minutes)
        return timeString

    def readBinaryWatch(self, num):
        if num == 0:
            return ["0:00"]
        possibilities = ["1m", "2m", "4m", "8m", "16m", "32m", "1h", "2h", "4h", "8h"]
        times = set()
        lists = self.c(possibilities, num, [])
        for x in lists:
            temptime = self.convertToTime(x)
            times.add(temptime)
        return list(times)
