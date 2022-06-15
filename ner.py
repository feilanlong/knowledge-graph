from ltp import LTP
ltp = LTP()  # 默认加载 Small 模型
# user_dict.txt 是词典文件， max_window是最大前向分词窗口
ltp.init_dict(path="user_dict.txt", max_window=4)

def get_ner(sent):
    
    # 分词
    seg, hidden = ltp.seg([sent])
    # #词性标注
    # pos = ltp.pos(hidden)
    # 命名实体识别
    ner = ltp.ner(hidden)
    print(ner)
    ners=[]
    for i in range(len(ner[0])):
        tag, start, end = ner[0][i]
        print(tag, ":", "".join(seg[0][start:end + 1]), end=" ")
        ners.append("".join(seg[0][start:end + 1]))
    # print(ners)
    return ners

if __name__ == "__main__":
    ners = get_ner("赫哲族主要分布于黑龙江、松花江、乌苏里江交汇构成的三江平原和完达山余脉")
    print('\n\n===============================')
    print(ners)


