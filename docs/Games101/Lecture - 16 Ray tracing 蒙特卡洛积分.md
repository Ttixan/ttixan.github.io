## content

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241104223747.png)

## Monte Carlo 蒙特卡洛积分
想要解决的问题：给定任何的函数，想要计算某段范围之间的定积分。【给出最后的值】
以前的做法：不定积分相减
但是：

- 有的函数无法很好写出解析解。

- 我们：只关心最后的结果，不关心中间的解析式。
蒙特卡洛积分：【直观解释】

- 取某一块的y作为小长方形

- 采样多次，把所有的长方形加起来，就是积分

### 定义
蒙特卡洛近似：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113164313.png)

### 例子：蒙特卡洛估计
一个平均的采样函数：$b-a$。可以看作一个长方形

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113164508.png)

结果：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113164531.png)

好处：

- 只需要对积分区域之间进行采样，知道PDF即可。【采样越多，结果更准】

- 需要在x上采样，x上积分

## Path Tracing
回顾whitted-style ray tracing的假设

- 总是产生镜面反射

- 在漫反射表面上停止传播
这样简单的假设是否合理呢？

#### Problem 1：Glossy reflection
现实情况中有类似于磨砂的材质，并不是完全镜面反射

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113165208.png)

#### Problem 2：Reflections between Diffuse materials
漫反射表面其实也会发光，而不是停住。Color bleeding现象。【图中红色的面】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113165432.png)

### Whitted-Style ray tracing is Wrong
按照渲染方程才是更正确的方法。需要解渲染方程。

- 需要解出半球的积分，得到一个值

- 还需要递归解决

#### A simple Monte Carlo Solution 简单的例子
着色点p，camera的radiance的积分。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113190421.png)

- FX是什么？

- PDF是什么？因为半球面的面积是$2\pi$ 按照均匀的就是倒数

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113190551.png)

算法的流程：

- 随机选择基于pdf中的某个方向

- 对于每个方向

- 一条光线共线的radiance，逐步增加基于蒙特卡洛积分的，某点的radiance

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113191014.png)

### Introducing Global Illumination
光源反射出来的radiance和面反射出来的radiance都一样，也可以看作光源。
Q点到P点反射的radiance，【就像】在P点看向Q点的radiance，就可以看作Q点的直接光照。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113191314.png)

简单算法上加上分支：

- 如果打到的是object而不是光源

- 【递归】q点的直接光照的结果作为p点的光照，方向为反向

#### Problem 1：Explosion of # rays
可能会有很多光线都达到这点上，再经过bounce之后，指数级增长

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113191546.png)

那么N=？的时候不会爆炸？N=1的时候。
所以需要修改任意一点的着色，不能用N个光线，而是随机采集一根光线。
对于N=1就是路径追踪。N！=1就是分布式追踪。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113191801.png)

#### Solution：Ray generation
一个像素有可能有多个光线，很有可能有多个路径。
那么只要有足够多的path就可以了，再求平均。
对于一个像素内，均匀取多个位置，从摄像机位置连接光线，如果达到了某个scene的p点，则像素进行shading。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113192155.png)

#### Problem 2：Retrieval
还有一个问题是算法不会停止（弹射次数）
方法：

- 限制光线弹射的次数，不对，没有考虑多次弹射的能量问题
引入方法：俄罗斯轮盘赌（Russian  Roulette）

#### Russian Roulette（RR）俄罗斯轮盘赌
决定一定的概率往下追踪。一定的概率停下来。
一定的概率：

- P的概率进行继续发射，并且除以p

- 1-P的概率返回为0
最后的期望依然为Lo

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113194511.png)

代码上的改变：除以P_RR

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113194542.png)

#### 最后的问题：效率 low-SPP
SPP（sample per pixel）一个像素发出多少个光线。
但是low SPP下效果不好。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113194755.png)

Why？和光源的大小有关，很多光线浪费掉了，没办法打到光源上。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113194914.png)

Solution：是否有不是均匀的采样方法（不是蒙特卡洛那样均匀的采样），提高效率？
如何可以直接在光源上进行采样，则不会浪费了。

#### Solution: 在光源上采样
但是以前的假设是基于方向角的。
是否可以把渲染方程改写为对A的积分而不是对omega的积分？只需要得到两者的关系

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113201505.png)

只需要求出投影即可。再除以距离的平方。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113201702.png)

最后带入即可。（在微积分上面的变量替换）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113202042.png)

还解决了一个问题：光源的贡献

- 【直接光照】改写后的渲染方程：进行均匀的采样（光照采样的结果）

- 【间接光照】其他的反射：俄罗斯轮盘赌

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113202306.png)

最后最后需要考虑的：是否有中间物体挡道直接光照，需要判断一下。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241113202554.png)
