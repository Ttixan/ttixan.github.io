## Content

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241104223522.png)

## important measurement 重要的度量

### Irradiance
定义：每一个面积上对应的能量
对比于radio intensity：单位角上对应的能量
注意：面必须和power垂直才行。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110193108.png)

#### recall：兰伯特定律
不垂直于光的时候接收到的能量要变小。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110193059.png)

#### recall：光的衰减
使用irradiance来理解：除以实际的面积即可

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110193624.png)

### radiance
描述：光线的属性
定义：power在单位里立体角并且单位面积（两次微分）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110193834.png)

确定某个区域面积，会向着某个立体角的方向辐射方向

#### 从之前的单位来理解：
radiance和irradiance/intensity的关系

- 单位立体角的irradiance

- 单位反射区域的intensity

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110194204.png)

因此考虑incident radiance：

- 对于irradiance来说，定义了新的入射方向

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110194410.png)

同理从intensity的角度考虑。因此考虑

- intensity，定义了新的发射方向。

#### Irradiance vs radiance
积分之后就是所有面积上射入的光线。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110194645.png)

## BRDF：bidirectional Reflectance Distribution Function 双向反射分布函数
定义：一个函数，定义了入射方向在某个点的反射情况。包括强度和方向。
过程：一个方向的radiance，入射到某个单位面积，转化为irradiance（能量？），再出射到某个方向化为radiance。
区分：

- 由于不同的反射性质（漫反射，镜面反射）

- 所以**每个反射方向**$w_r$分配的能量都有所不同
BRDF 就是定义如何分配，也定义了不同的材质。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110195313.png)

## Reflection Equation 反射方程
某个方向的入射点对于某个着色点有多少贡献。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110195741.png)

- 后三项是irradiance

- 再BRDF

- 再积分起来就是radiance

## 渲染方程 The rendering equation
难点：需要考虑所有入射的光线，并且不一定来自于光源。（可能是别人二次反射的光线）。入射的光线可能是别人的初涉光线。【递归的问题】

渲染：实质上是入射+反射两部分

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110200131.png)

- $\Omega$ 和$H^2$都是半球

- $cos\theta_i$ 被用法线和入射方向相乘所替代了
TODO：下一节课介绍如何解这个渲染方程

### 概念上的理解 渲染方向

#### 一个点光源

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110200737.png)

#### 很多个点光源：和，加起来

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110200759.png)

#### 面光源：求和变成积分

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110200854.png)

#### 多次反射，简化
其实和以前的方程类似，可以直接当作光源来理解。但是只是不知道另一个面来源的radiance

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110201016.png)

递归解法，简化表示

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110201205.png)

- 后半部分甚至可以看作一个操作符？算子

- 进一步简化的方程为

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110201309.png)

为什么要这么写？是为了解方程

- L可以左移

- 求逆做求解

- 算子形式有类似于泰勒展开的性质。（K作为反射操作符可以分解）

- 最后得到一次、两次、三次反射后的结果的和，是对于弹射次数的分解

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110203911.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110204053.png)

因此，和光栅化的区别在于：

- 只能实现前两项

- 光线追踪是可以计算后面的部分。（二次、三次光照）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110204503.png)

### 直观例子
多次弹射之后会更亮。但是会收敛到一个差不多的亮度

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110204728.png)

## 如何解渲染方程？

### 概率论复习

#### 随机变量

- 随机变量

- 随机概率分布

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110205031.png)

#### 概率

- 随机变量以不同的概率取不同的值

- 概率为非负值

- 概率之和为1

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110205126.png)

#### 期望

- 期望：如果重复取样能得到的平均数

- 期望的计算方法：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110205217.png)

#### 连续情况
概率分布方程：Probability Distribution Function

- 函数的纵坐标并不直接表示概率

- 而是连线（区域)
回顾之前的离散概率分布：

- 概率密度函数积分=1

- 期望也是积分

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110205535.png)

随机变量函数的期望也可以得到期望

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241110205730.png)
