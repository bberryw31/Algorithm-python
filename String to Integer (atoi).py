class Solution:
    def myAtoi(self, s: str) -> int:
        txt = []
        txt.extend(s)
        a = [str(x) for x in range(10)]
        b = [' ','+','-']

        result = []
        for i in range(len(txt)):
            if txt[i] in a or txt[i] in b:
                result.append(txt[i])
            else:
                break
        if result == []:
            return 0
        else:
            result2 = ''
            for r in result:
                if r == ' ':
                    if result2 == '':
                        continue
                    else:
                        break
                elif r == '-':
                    if result2 == '':
                        result2+='-'
                    else:
                        break
                elif r == '+':
                    if result2 == '':
                        result2+='+'
                    else:
                        break
                else:
                    result2+=r
            if result2 == '':
                return 0
            if result2[0] == '+':
                result2 = result2[1:]
            try:
                answer = int(result2)
                if answer<-2**31:
                    return -2**31
                elif answer>2**31-1:
                    return 2**31-1
                else:
                    return answer
            except:
                return 0