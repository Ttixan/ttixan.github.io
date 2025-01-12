## content
- why ray tracing
- whitted-style ray tracing
- ray-object intersection
	- implicit surface
	- triangles
- axis-aligned bounding boxes （AABB）
	- Understanding
	- Ray-aabb intersection
## why rat tracing
无法很好解决全局的一些特性
- 软阴影
- 镜面反射
- 低效的非直接反射
可以得到近似的，快速的效果，但是质量不好。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241031162113.png)

solution：计算准确，但是很慢。
应用：
- 光栅化：实时，光线追踪：离线。
### 光线
以下几个基本的假设
1. 光线是直线
2. 光线之间不会产生碰撞
3. 光线从光源发射出来，最后进入人眼。
4. 光路可逆性（看得到东西那东西也看得到你？）

## Ray casting 光线投射
光源出发（一种思路），也可以从终点开始（逆向）
1. 视线：对于每个像素，让它和摄像机和连线，延申出去
2. 找到物体：如果和物体相交，取最近的一个点（解决深度的问题）
3. 是否再阴影中：并且和光源作为连线（是否光源可见），那么就形成一条有效的光路。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241031162952.png)

![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241031163352.png)
但是：光线只反射了一次，不符合常识。需要多次反射。
Solution：
### Recursive（Whitted-style） ray tracing
对于镜面的物体
1. 反射
2. 折射
在任意一个点可以继续传播（只需要算出反射和折射方向）

计算量增加：
每一个反射点都会和光源做一个连线，需要计算是否可见。
- 最后做一个累加。
- 还会考虑衰减的问题。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241031164008.png)

命名问题：
- primary ray（第一个实现
- secondary（反射）
- shadow rays（连接光线的部分）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241031164108.png)

## technique question
### Ray-surface intersection 交点
定义：点光源射出的光线
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241101194140.png)

#### with sphere与球的焦点
定义了球上点：$p$
求交点即为吧光线的部分带入其中求方程。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241101194349.png)
再使用球根公式即可得到。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241101194614.png)
求解结果的general的表达：一般性的隐式表面
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241101194737.png)

判定内外还可以根据交点的个数。
求三角形求交的步骤：
- 每个三角形都求一下交点
- 但是相对来说太慢了
- 只需要考虑0，1个交点，做交集
---

Q: Whitted-style 的光线发射，相比于单次光线的特点是什么？
A: 递归，可以多次反射
<!--ID: 1731676468185-->


Q: Whitted-style 中光线的定义有哪两个参数？
A: 原点o和发射方向d
<!--ID: 1731676468189-->


Q: 球的定义有哪两个参数？
A: 原点c和半径R。
<!--ID: 1731676468192-->


Q: 如何求直线和球的相交？
A: 带入，求根公式。
<!--ID: 1731676468194-->


####  Moller-Trumbore 算法：和三角形相交

分为两个步骤：
- 如何求光线和平面求交？
- 求交点是否在这个三角形内？【已经知道的内容】
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102163652.png)

平面的定义：
- 定义一个法线
- 平面必须过某个点，这些点满足某个条件。
- 定义：p（某点）和p‘的向量和平面垂直。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102163850.png)

最后带入之前的直线定义$r(t)=o+td$相交：
- 求得t的表示：
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102164035.png)

是否有可以直接求得点的方法？【作业中提到直接带入】[[作业5相关]]
- 使用重心坐标表示三角形某点
- 使用线性方程组求解【线性方程组的climer法则？】
- 最后得到三个参数都为非负（在三角形内的性质）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102164422.png)

---

Moller-Trumbore 算法求直线与三角形相交，可以分为两步：1. 求和{平面}相交，2. 求交点是否在{三角形}内。
<!--ID: 1731676468221-->


Q: 如何用p定义一个平面？【两个变量】
A: 法线N，p和平面上p'的连线和法线垂直。
<!--ID: 1731676468198-->


Q: 如何直接求三角形是否和某光线相交？
A: 线性方程组的三个参数都大于0
<!--ID: 1731676468201-->


### Accelerate 加速
原始的算法需要求像素x三角形数量个求交计算，太慢了
如何加速？
#### bounding volume 包围盒
用一个相对简单的几何形状包起来复杂表面的物体。
逻辑上：
- 碰不到包围盒那肯定碰不到物体
- 类似于模糊化边界之后进行剪枝计算？

前置：把方体看作三个轴对称平面的交集。（AABB）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102165123.png)

如何判定物体相交？从二维平面上考虑
- 给定一个光线在什么时候会跟无限大的面有交点？
- tmin和tmax进去和出去，x和y的平面
- 求线段的交集（必须同时满足）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102170444.png)

重要思想：
- 只有三个都满足才进入
- 只要离开任意一个就算离开
所以算法：
- 三个平面计算最小时间和最大时间
- 进入的时间为$t_{enter}=max\{t_{min}\}$，最后离开：$t_{exit}=min\{t_{max}\}$
- 最后判断是否交点：进入时间小于离开时间
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102170748.png)
还有一些额外的判断【正负】：
- 如果退出时间小于0：光线后面是box
- 如果退出大于0，但是进入小于0：光线起点在盒子里
总结：当且仅当
- 进入时间<离开时间，并且退出时间大于0，则进行相交。

Why？axis-aligned？
垂直轴的计算更加简单：只需要某轴的分量
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241102171316.png)

---

Q: AABB（Axis-Aligned Bounding Box）是用来解决光线追踪什么问题的？
A: 减少计算量，加速。
<!--ID: 1731676468204-->


Q: 用什么概念来描述和Bounding Box相交的过程？
A: 相交时间
<!--ID: 1731676468207-->


Q: AABB的三个维度上的开始时间应该取什么？【最前，最后】
A: 最后进入才代表全部进入【最大值】
<!--ID: 1731676468210-->


Q: AABB的三个维度上的离开时间应该取什么？【最前，最后】
A: 有光线离开则为离开。【最小值】
<!--ID: 1731676468212-->


Q: AABB进出时间还应该满足和0的什么关系？
A: 退出时间大于0
<!--ID: 1731676468215-->


Q: AABB的进出时间之间应该满足什么大小关系？
A: 进入时间小于出去时间。
<!--ID: 1731676468218-->
