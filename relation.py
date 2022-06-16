from ltp import LTP
ltp = LTP() # 默认加载 Small 模型

#通过语义角色标注任务可以将句子中各实体以及其关系表示出来，以主谓宾关系为例，构建一个（主，谓，宾）的三元组
def srl_AtoA(sent):
    seg, hidden = ltp.seg([sent])
    seg = seg[0]
    # print(seg)
    srl = ltp.srl(hidden, keep_empty=False)[0]
    # print(srl)
    results = []
    
    for s in srl:
        key = s[0]
        values = s[1]
        result_A0 = ''
        result_A1 = ''
        for value in values:
            print(value)
            if value[0] == 'A0':
                result_A0 = ''.join(seg[value[1]:value[2]+1])
            if value[0] == 'A1':
                result_A1 = ''.join(seg[value[1]:value[2]+1])
        if result_A0 != '' and result_A1 != '':
            results.append((result_A0,seg[key],result_A1))
    print(results)
    return results
if __name__ == "__main__":
    srl_AtoA("赫哲族主要分布于黑龙江、松花江、乌苏里江交汇构成的三江平原和完达山余脉")


