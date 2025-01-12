## content
using AABB to accelerate ray tracing
- uniform grids
- spatial partitions
basic radiometry

## Uniform grids
场景复杂，如何进行求交？上节课说到了使用盒子先做判断。
步骤：
- 包围盒
- 预处理（划分为格子）
- 与物体相交的格子判断哪些有物体：
- 进行光线追踪，和格子相交判断。
- 再求【光线】与这个【盒子内的物体】相交。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104215001.png)
平衡：格子不能太稀疏，太密集
- 与光线直接和物体求交换成光线和格子求交。
- 启发式算法求得数量：
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104215228.png)
### when will work well 效果好的时间？
Teapot in a stadium：存在
- 大规模密集
- 大规模稀疏
效果不好。

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104215437.png)

## Spatial Partition
基于上述的不足之处。
key idea：稀疏的时候用大格子，密集的地方用小格子。
### Example：KD-Tree
例子：
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104215650.png)
八叉树：
- 例如停下来的条件：向下切有大部分块都没有东西
- 例如右下角
- 缺点：维数过高的时候计算量很多（8岔+指数级）

KD-tree
- 每次只沿着某个轴砍一刀
- 水平，竖直，交替划分，能够保证均匀的格子
- 类似二叉树的性质，计算更少

其他：BSP-tree：斜着切，不好计算

### KD-tree Pre-processing 预处理

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104220236.png)
数据结构记录：
- 内部节点：
	- 切割的轴
	- 切割的位置
	- 指向孩子的节点指针
- 叶子节点：
	- 实际切割的object

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104220421.png)

### Traversing a KD-Tree：实际进行光线追踪

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104220851.png)
判断：
- 如果有交点，则判断两个child
	- child为leaf：计算物体相交
	- child为internal：计算格子，重复上面过程
- 如果没有交点，则跳过

KD-tree问题：
- 给定AABB的包围盒，得知道哪些三角形【也即物体】和框有交集。（即划分框的办法本身比较难）
- 物体本身也会被划分到多个不同的格子，可能不再这个盒子里但是相交。
## Object Partition：物体划分
### BVH : boudning volume hierarchy
避免了
- 一个几何结构不会出现在多个叶子节点里
- 不需要计算bounding本身和三角形的相交
问题：
- 划分空间并不严格，会产生相交，只能尽可能让它变少
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104221827.png)
### example
步骤
- 找到包围盒
- 递归地进行划分
- 重新计算包围盒
- 直到停下来的条件
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104221926.png)

### Building BVH
如何划分？保持均匀？
solution：沿着更长的轴进行划分
solution：找到中位数？的三角形【有排序的问题】
- 快速选择算法【top问题】

如何停止？
- 设置包含很少的元素的时候进行停止

数据结构
- 中间节点：
	- 盒子
	- 指针
- 叶子节点
	- 盒子
	- 指物体
- 如果要表示一个子集：只需要找到这个子树

### BVH traversal

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104222756.png)
- 如果不相交： return
- 如果相交的是一个叶子：计算所有物体相交
- 两个child都进行计算，返回更近的一个hit。

### comparison 对比

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241104223119.png)

## Basic radiometry 辐射度量学
问题：
- 之前在布林冯模型中提到光线强度I，但是并没有完全介绍
- 按照Whitted的加速模型，光线应该是一块区域散射，而不是一条直线

why 需要学习辐射度量学？
- 更精确的描述光线的方法
- 高级光线追踪建立于此

### Radiometry 辐射度量学
辐射度量学：如何描述光照
表示的新的属性：
- radiant flux:光通量，单位时间内通过的光总量
- intensity:光强，单位立体角光通量，瓦特
- irradiance:辉度，单位面积光通量，瓦特/平方米
- radiance:光亮度

学东西的三把斧：
- why：为什么要学
- what：具体是什么
- how：怎么做

### Radiant Energy and Flux （power）
energy定义：能量是电磁辐射的能量。使用焦耳作为单位。
power：单位时间的性质：单位时间的能量（功率）（单位流明
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213007.png)

### important light measurement


![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213240.png)

#### radio intensity
radio intensity：单位能量除以单位立体角。单位为坎德拉
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213425.png)
#### 立体角
从平面出发：弧长除以半径
- 立体角就是球面上的面积除以半径平方
- 定义了：空间中的角有多大
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213638.png)
#### 单位立体角？微分立体角
从两个角度：
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213852.png)
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106213943.png)
- 对于积分出来是$4\pi$

均匀分布的光源：
- 以单位角来积分的intensity最后得到的是功率
- 所以功率除4pi为indensity
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241106214208.png)

