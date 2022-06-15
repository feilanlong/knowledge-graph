from ltp import LTP
ltp = LTP() # 默认加载 Small 模型
#分词
segment, _ = ltp.seg(["赫哲族主要分布于黑龙江、松花江、乌苏里江交汇构成的三江平原和完达山余脉"])
print(segment)
#词性标注
seg, hidden = ltp.seg(["赫哲族主要分布于黑龙江、松花江、乌苏里江交汇构成的三江平原和完达山余脉"])
pos = ltp.pos(hidden)
print(pos)
#命名实体识别
seg, hidden = ltp.seg(["赫哲族主要分布于黑龙江、松花江、乌苏里江交汇构成的三江平原和完达山余脉"])
ner = ltp.ner(hidden)
print(ner)
tag, start, end = ner[0][0]
print(tag,":", "".join(seg[0][start:end + 1]))
srl = ltp.srl(hidden)
print(srl)
srl = ltp.srl(hidden, keep_empty=False)
print(srl)
