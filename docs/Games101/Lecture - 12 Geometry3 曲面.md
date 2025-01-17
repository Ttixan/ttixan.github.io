## Surface
### 几何处理
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024211237.png)
- Subdivision：更多三角形
- Simplification：更少三角形
- Regularization：统一大小的三角形【正三角形】
	- 改进三角形质量的同时不改变质量

---

介绍了三种几何处理：1. {Subdivision}：更多三角形，2. {Simplification}：更少三角形，3. {Regularization}：统一大小的三角形【正三角形】
<!--ID: 1731328416358-->



### Subdivision 细分
制作的步骤？
- 引入更多三角形（各种算法）
- 改变他们的位置。（引入三角形使得模型的外形变化）
#### Loop Subdivision
注意这里的loop不是循环的意思。
- 将一个三角形切分为4个
- 改变不同的三角形的位置（根据不同的顶点类型，新的和老的）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025113416.png)
具体做法：
对于新的顶点
- 找到ABCD四个点
- 对白点进行加权（分数是这样设计的）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025113626.png)

对于旧的顶点
- 找到周围的顶点（6个顶点）
- 一部分相信老的顶点的值，一部分保留自己的位置
	- n为度：连接的边的数量
	- u为一个和度有关的参数，例如n=3，3/(8n)
- 最后的公式：
	- $1-n*u$ 表示平均和加权
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025113930.png)

---

Q: 介绍的Loop细分三角形算法，可以把顶点分为哪两类？
A: 新的和旧的
<!--ID: 1731328416325-->


介绍的Loop细分三角形算法，可以分为两个步骤：1. {划分}三角形，2. 指定{新位置}
<!--ID: 1731328416361-->


Q: 对于Loop算法中的新顶点，新位置由什么决定？
A: 周围邻居节点。
<!--ID: 1731328416330-->


Q: 对于Loop算法中的旧节点，位置由什么决定？【两个】
A: 自己顶点的度和邻居节点的位置
<!--ID: 1731328416333-->



#### Catmull-Clark subdivision 对于general mesh的细分
三角形网格才能用loop，对于一般的情况可以用这个方式（三角形和四边形）
定义：
- 非四边形面（Non-quad face）
- 奇异点：degree  ！= 4 （Extraordinary vertex）
具体做法：
- 取边的中点
- 取面的中点
- 连接起来。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025150940.png)

- 问题: 有多少新的奇异点？
新增加的三角形内部的奇异点。
- 问题：他们的度呢？
度为边的数量（三角形内部的为了要跟每一个边相连，所以为3）
- 问题：还有多少非四边形面？
没有了。每个非四边形面在引入细分之后都添加了奇异点。
**奇异点数不会再增加。**【性质】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025151333.png)
#### 更新方法
- 边上的点：周围面中心+周围边的和
- 面上的点：周围顶点的和
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025151709.png)

更新结果的例子：
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025151824.png)

---

Q: Catmull-Clark 细分方法针对的是什么形状？【不止】
A: 不止三角形，更广的多边形。
<!--ID: 1731328416335-->


Q: Catmull-Clark 算法细分面，提到了需要切分什么面？
A: 非四边形面
<!--ID: 1731328416338-->


Q: Catmull-Clark 算法细分面后，什么性质的点不会增加？
A: 奇异点【degree  ！= 4 （Extraordinary vertex）
<!--ID: 1731328416341-->


Q: Catmull-Clark 算法细分，更新的点分为哪两种？
A: 边上的点和面上的点。
<!--ID: 1731328416344-->


### Mesh simplification 简化
#### Definition and concept
目标是减少mesh elements的数量，并且保存整体的形状。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025152217.png)
- 存储上的问题（移动设备上显示）
- 远近需求（不同情况不同复杂程度）
相关：
- mipmap（图像的层次结构）-层次结构的3D（几何）
#### how to do？边坍缩
边坍缩方法：把边捏在一起。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025152554.png)
困难的问题在于：如何找到一个合适的坍缩点？在不影响外观的情况下
Solution：二次误差度量
#### Quadric Error Metrics 二次误差度量
找到某个点，使得到每个其他点的L2距离之和最小。【类似于机器学习中的损失函数优化】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025152959.png)

选择哪个边进行坍缩？
Solution：每一条边都有一个二次度量误差，从低到高开始坍缩。

问题1，但是：以前的边坍缩之后还会影响其他边的变化。
某种数据结构：堆。
- 允许求最小
- 允许动态更新
问题2：局部最优是否是全局最优？
贪心算法效果已经不错了，所以就采用这种方法。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025153506.png)

实际效果：
简化的部分跟平面或者曲面有关系（大小）

---

Q: 为什么需要减少面数？
A: 存储上的问题（移动设备上显示）和 远近需求（不同情况不同复杂程度）
<!--ID: 1731328416347-->


Q: 课程中介绍了一种减少面数的方法是什么？
A: 边坍缩方法
<!--ID: 1731328416349-->


Q: 边坍缩方法如何决定消去哪条边？
A: 可以按照L2距离来缩小
<!--ID: 1731328416352-->


Q: 如何解决边坍缩更新过程中的动态问题？【数据结构】
A: 堆结构
<!--ID: 1731328416355-->


## Shadows - shading遗漏的问题
之前没有讲到shadow的问题，可以塑造更强的位置感
### Shadow mapping 阴影图
实际上是一种 Image-space的问题
- 在计算shadow的过程中对于几何情况并不需要了解
- 并且还需要处理一些走样问题
关键在于：
- 一个不在阴影中的点，必须同时被光和摄像机所看到
**Note：经典的shadow mapping 只能处理点光源（hard shadow）**
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241111202945.png)

#### Pass 1：render from light
从点光源开始讲shadow的问题
- 先从光源看到什么（光栅化1）
	- 记录看到的深度图
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025160259.png)
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025160328.png)

#### Pass 2：Projection
- 从摄像机看向场景（光栅化2）
- 渲染的点重新投影回去光源【注意是转换】，转换后只比较z的大小
- 看是否深度一致，
	- 一致则为可见点
	- 不一致则为看不到的点
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025160700.png)
绿的部分是距离约等于的部分
有些看起来不干净的点：
- 由于精度问题，不能完全相等（浮点数）
- shadow map（记录深度的图）本身的分辨率和渲染场景的分辨率不一致（走样）

结果：
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025161022.png)
缺点：
- 计算开销
- 浮点数数值精度
- 阴影图的分辨率（基于image的技术的通病）
- 只能做硬阴影

---

shadow mapping的关键假设：不在阴影里的点，必须同时被{光源}和{相机}看到
<!--ID: 1731328416364-->


shadow mapping所使用的光栅化技术：{深度图}
<!--ID: 1731328416367-->


### 其他方式
软阴影和硬阴影
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025161518.png)

实际中的物理依据：
- 本影
- 半影
实际上取决于光源的大小
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241025161502.png)
