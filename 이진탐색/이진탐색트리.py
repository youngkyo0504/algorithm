##BST
#이진탐색트리는 노드의 오른쪽은 자신보다 크게 왼쪽은 작게하는 트리구조이다. 
# 장점 : 입력 시 값에 따라 곧바로 위치가 지정되기 때문에 데이터 검색 속도가 빠르다. 따라서 숫자 값 검색이 잦을 경우에 유리하다.
# 단점 : 최악의 경우에 한 쪽으로만 이어질 수 있다.
# (단점을 보완한 트리들로는 AVL tree, red black tree .. 등이 있다)

class Node:#각 노드는 2가지의 포인터를 가진다. 1가지의 값을 가진다.
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right = None

class bst:
    def __init__(self):
         self.root = None
    def insert(self, data):  #크면 오른쪽으로 탐색을 진행 작으면 왼쪽으로 진행 비어있는 값을 찾으면 데이터 넣기 
        self.root = self._insert_value(self.root, data)
        #위식은 루트를 항상 맨위 꼭지가 되게한다. insert value함수 리턴값을 보면 알 수 있음 
        #배열처럼 인덱스를 아는 것이 아니고 링크트리스트 처럼 루트부터 이동하기 때문에 루트는 굉장히 중요하다. 
    def _insert_value(self, currentNode, data):
        if currentNode == None:
            currentNode = Node(data)
            print(currentNode.data)
        else:
            if data <= currentNode.data:#왼쪽 부분에서 재귀
                currentNode.left = self._insert_value(currentNode.left,data)
            else:#오른쪽 부분에서 재귀 
                currentNode.right = self._insert_value(currentNode.right,data)    
        return currentNode    
    def find(self, key):
        return self.find_value(self.root, key)
    def find_value(self,currentNode, key):
        if  currentNode==None or currentNode.data == key:
            return currentNode is not None #currentNode가 있으면 True 이고 없으면 False이다. 
        else:
            if key<= currentNode.data:
                return self.find_value(currentNode.left, key)
            else:
                return self.find_value(currentNode.right, key)
    def delete(self, key):
        self.root = self.delete_value(self.root, key)
    def delete_value(self, currentNode, key):
        if currentNode == None:
            print("there is not same key in tree")
        elif currentNode.data == key:
            currentNode = self.delete_remake(currentNode)
            return currentNode  
        else:
            if key <= currentNode.data:#왼쪽 부분에서 재귀
                self.delete_value(currentNode.left,key)
            else:  #오른쪽 부분에서 재귀 
                self.delete_value(currentNode.right, key)
        return currentNode
    def delete_remake(self,del_node):
        if del_node.right:
            node = del_node.right
            #삭제하는 노드의 모든 right부분은 항상 삭제하는 노드의 모든 left보다 크다  
            #따라서 삭제하는 노드의 left를 right부분 중 가장 작은 곳에 붙인다. 
            print(node.data)
            if node !=None:    
                while node.left != None:
                    node = node.left #끝까지 내려간다. 
                node.left = del_node.left
            del_node = del_node.right
        else:
            del_node = del_node.left
        return del_node

work =bst()
a = [13, 11, 14, 5, 12, 3, 7, 2, 4, 6, 8]
for i in a:
    work.insert(i)
print(work.root.left.data)
print(work.find(10))
work.delete(10)
currentNode=work.root
while currentNode != None:
    print(currentNode.data)
    currentNode=currentNode.left
#다음엔 순회하는 코드를 보자
        

            

                 

    
        