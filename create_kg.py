from py2neo import *

# graph = Graph('http://127.0.0.1:7474', username="neo4j", password="123456")
# graph = Graph('http://neo4j:123456@127.0.0.1:7474')
graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))

def create_kg(frame):
    count  = 0
    for i in frame.index:
        '''获取数据'''
        haozhe_nation = frame["郝哲族"].values[i]
        describe = frame["描述"].values[i]
        haozhe_re = frame["关系"].values[i]
        haozhe_nation = str(haozhe_nation)
        describe = str(describe)
        haozhe_re = str(haozhe_re)
        haozhe_nation_node = Node('郝哲族', name=haozhe_nation)
        graph.merge(haozhe_nation_node,'郝哲族','name')  ## merge方法是将重复数据去除掉，只留第一个
        describe_node = Node('描述', name=describe)
        haozhe_re_node = Node('关系', name=haozhe_re)
        # 郝哲族类
        yoga_2 = Relationship(haozhe_nation_node, '描述', describe_node)
        yoga_3 = Relationship(describe_node, '关系', haozhe_re_node)

        try:
            graph.create(yoga_2)
        except:
            continue
        try:
            graph.create(yoga_3)
        except:
            continue
        count += 1
        print(count)
    print("知识图谱创建完毕！")
if __name__=="__main__":
    create_kg()

