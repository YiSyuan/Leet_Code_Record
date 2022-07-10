# 13
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            "I": "1",
            "V": "5",
            "X": "10", 
            "L": "50",
            "C": "100", 
            "D": "500",
            "M": "1000",
        }
        s = list(s)
        b, used = [], []
        for k in range(len(s)):
            if k in used:
                continue
            value = s[k]
            next = s[k+1] if k != len(s)-1 else False
            tran = False
            if (value == "I" and next and next in ("V", "X")) or \
                  (value == "X" and next and next in ("L", "C")) or \
                    (value == "C" and next and next in ("D", "M")):
                tran = True

            if tran:
                c = eval(f"{symbol[next]} - {symbol[value]}")
                b.append(f"+{c}")
                used.extend([k, k+1])
            else:
                b.append(f"+{symbol[value]}")
                used.append(k)
        m = "".join(i for i in b)
        m = eval(m)
        return m
