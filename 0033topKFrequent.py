'''347给定一个非空的整数数组，返回其中出现频率前 k 高的元素。'''
'''1.collections模块
collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型，分别是：

OrderedDict类：排序字典，是字典的子类。引入自2.7。
namedtuple()函数：命名元组，是一个工厂函数。引入自2.6。
Counter类：为hashable对象计数，是字典的子类。引入自2.7。
deque：双向队列。引入自2.4。
defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键。引入自2.5。

Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。

2.5 elements()
返回一个迭代器。元素被重复了多少次，在该迭代器中就包含多少个该元素。元素排列无确定顺序，个数小于1的元素不被包含。

2.6 most_common([n])
返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。其中的元素为元组

2.9 算术和集合操作
+、-、&、|操作也可以用于Counter。其中&和|操作分别返回两个Counter对象各元素的最小值和最大值。需要注意的是，得到的Counter对象将删除小于1的元素。

sum(c.values())  # 所有计数的总数
c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c.most_common()[:-n:-1]  # 取出计数最少的n个元素
c += Counter()  # 移除0和负值'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		'''内置函数Counter，自带计数功能'''
        return [k for k, v in collections.Counter(nums).most_common(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		'''非内置方法:使用字典来解决'''
        d = {}
        for n in nums:
			'''dict.get(a,b) 获取字典中key为a的值，如果a不存在，就设置a的值
				为b'''
            d[n] = d.get(n, 0) + 1
		# sorted方法python3中sorted 可以对所有可迭代的对象进行排序操作，尤其是可以对字典进行排序，其形式为：sorted(iterable, key=None, reverse=False)。sorted函数是有返回值的。	
		# key排序依据的准则，一般为函数名或匿名函数
		# dict.items()获取所有键值对，以键值元组作为列表元素的形式返回
		# dict.keys()获取所有键
		# dict.values()获取所有值
        # dict.get()通过键来获取对应的值
        return sorted(d.keys(), key=d.get, reverse = True)[:k]
