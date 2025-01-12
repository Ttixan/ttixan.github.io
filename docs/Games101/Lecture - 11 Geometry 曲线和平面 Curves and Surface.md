TARGET DECK
other::读书笔记::图形学
FILE TAGS
图形学 Lecture-11
## Content 目录
- explicit representation
- 曲线 curve
	- Bezier curves
	- De casteljau's algorithm
	- B-splines, etc.
- 表面 Surface
	- Bezier surface
	- Triangle & quads
		- Subdivision, simplification, regularization

## Explicit representation of Geometry 显式几何表示

### Point Cloud 点云
不考虑面，只考虑点。密集的点表述地更好
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024194423.png)

还有的研究方向：给定点，变成三角形面。

### Polygon Mesh 多边形面
用三角形，四边形来描述复杂的物体
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024194559.png)

保存方式：.obj文件
- 顶点
- 法线
- 纹理坐标
- 连接关系（哪几个点会形成三角形）（指定纹理，顶点，法线）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024194834.png)

---

介绍了两种显式表示几何的方法：{点云}，{多边形面}
<!--ID: 1730361816130-->



## Curve 曲线
### 贝塞尔曲线
用一系列控制点来定义某个曲线，表明了曲线满足的某种性质。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024195605.png)
- 经过起始点和终止点
- 设定了切线的方向

---

贝塞尔曲线的性质：1. 必须经过{起始点}和{终止点}，2. {切线}方向需和设定一致
<!--ID: 1730361816133-->


#### de casteljau 算法
问题：给定三个点，如何求出其曲线？
算法：
- 任意的时间t（0，1）之间，给出其在某个线段上的位置
- 再把新的线段连起来，又找时间t的位置。
- 穷举（任意一个时间t）直到只剩一个点【递归】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024200219.png)

例子2：4个点的例子
- 四个点：找到某点，两个点
- 两个点：找到重点：一个线段
- 一个线段，中间点，找到曲线。【三个点确定的曲线】 
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024200626.png)

---

德卡斯特里奥算法: 1. 取一个{【0，1】}之间的t值，2. 连接两个点，按照t寻找{中间点}，3. {连接}中点，形成新的线段，4. 直到{只剩一个点}。5. 微小增加t，直到1
<!--ID: 1730361816137-->


贝塞尔曲线的代数解释可以用{伯恩斯坦多项式}来表示。
<!--ID: 1730361816141-->


Q: 伯恩斯坦多项式的表达式
A:  $B_n(x) = \sum_{k=0}^{n} \binom{n}{k} x^k (1-x)^{n-k}$
<!--ID: 1730361816118-->


Q: 伯恩斯坦多项式的左边(n,k)是什么？表达式是什么？
A: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
<!--ID: 1730361816122-->


### 代数解释 Evaluation Bezier Curves
把每个阶的分割点依然用t的多项式带入原本的式子，可以得到其实曲线是由控制点和多项式组成的表示：
- n表示控制点的个数，j表示第几个控制点
- t表示时间，$B_j^n(t)$ 表示伯恩斯坦多项式
- 描述的是二项分布。二项式系数位$\binom{n}{k} = \frac{n!}{k!(n-k)!}$
并且这样的性质可以运用到三维空间中。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024202041.png)
三维空间
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024203038.png)

### 贝塞尔曲线性质
- t=0 t=1为起点和终点。
- 切线的朝向（和起点，终点有关），常数和给点个数有关
- 对不同的顶点做变换，做了仿射变化后，得出的曲线是一样的。（
	- 不需要记录每个点，可以不用管变换先后顺序）
	- 但是注意只对仿射变换有用
- 凸包性质：画出来的曲线一定在连接的点之内（类似于素描中的切圆）【不能超过凸包的范围】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024203915.png)

---

贝塞尔曲线的4个性质：1. t=0和t=1的插值为{起点和终点}。2. 和最终片段{相切} 3. {仿射}不变，不需要再计算一次。4. 凸包性质：画出来的曲线一定在连接的点之内。
<!--ID: 1730361816145-->


### 逐段的贝塞尔曲线 Piece-wise
有时候多段的效果并不好，会变成一个平滑的曲线
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024205254.png)
不如逐段定义之后连接起来。
- 每次用4个控制点，之后连接起来
- 把控制点当作控制杆一样（钢笔工具）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024205324.png)

#### 连续性 continuity
- C0连续：终止点和起始点一样，
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024210023.png)

- C1连续：切线距离一样。共线，方向相反，距离一样。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024210036.png)
- 曲率连续（更高的连续性）

---

Q: 逐段的贝塞尔曲线，能够连续的性质是？
A: 1
<!--ID: 1730361816126-->


### 其他曲线 Other types of splines
样条：
用样条固定住，保证一定会过某点。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024210335.png)
B-样条（基函数）
- short for basis spline
性质更好：
- 需求：只改动某个点，不会改变整个曲线的范围【局部性】

## 曲面 Surfaces
贝塞尔曲面，把各种曲面拼接起来。
- 水平、，当作控制点
- 竖直，根据控制点继续生成面
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024210942.png)
### evaluation
水平方向
竖直方向
UV，用某一个U，找到四个点，再给出时间V，则为UV下的位置。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024211125.png)

### 几何处理
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024211237.png)
- Subdivision：更多三角形
- Simplification：更少三角形
- Regularization：统一大小的三角形