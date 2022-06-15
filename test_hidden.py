from ltp import LTP

ltp = LTP()

seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
print(seg)
print(hidden)