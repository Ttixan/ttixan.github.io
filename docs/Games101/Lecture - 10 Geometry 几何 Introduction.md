## 纹理应用
纹理可以用来表示环境光。
现代GPU中，纹理(texture)=内存(memory)+范围查询(range query)
可以把环境光当作贴图【用纹理描述环境光】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020112421.png)

- Uta大学的茶壶（经典模型）

环境光的假设：

- 来自某个无限远处

- 只记录方向信息
那么这个纹理应该如何得到呢？

### Spherical environment map
环境光的记录方法：使用球体（Spherical enviroment map）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020112714.png)

记录在球上，再展开。我们可以把球的表面完全展开，得到的二维图像就是环境纹理。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020112741.png)

但是在靠近极点的地方会存在扭曲的问题。
【地球仪】"纬度"越高，纹理越向"两级"聚拢，而"纬度"低的地方则不易出现这种情况。解决这一问题的方式是立方体映射。

解决方法：立方体映射

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020112931.png)

我们用一个立方体盒子包裹这个球体，这样由球心出发，朝球面任意一点方向射出的射线都会投影在立方体六个面的其中一个面上，最终效果如下：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020113112.png)

### 凹凸贴图 Bump mapping
在不改变几何特征的情况下，通过几何表面高度变化改变渲染点的法线方向，从而改变最终的渲染效果，造成物体表面凹凸有致的**假象**(因为我们并没有增加三角形个数，改变几何特征)。

- 不仅可以表示颜色

- 还可以表示法线，凹凸、法线贴图（bump normal mapping）

- 应用复杂的纹理来表现相对高度（并不是真的增加了很多面）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020113304.png)

黑白：

- 黑色为0，白色为1，定义了相对高度，改变法线

- 黑色区域代表高度值低的地方，白色区域代表高度值高的地方)
那么接下来如何计算出法线方向？

#### 原理

- 扰动表面的每个像素的法线

- 材质上面显示的是材质点的高度转移（height shift）

- 那么应该如何去改变法向量？

- 本质是改变了相对高度

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020114228.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020114626.png)

#### Flatland推导

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020115556.png)

- flatland就是从一维来看的法线变化情况

- 使用差分来检查如何变化：每平移一个单位，高度变化是多少。c是一个常数（由贴图决定？）

- 将得到的切线进行逆时针旋转90°之后就是法线方向（x，y进行交换）

- 最后进行正则化。（单位为1）
在3D的情况也是一样。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020140317.png)

当然，我们一开始假设了初始法线方向永远是垂直向上的(0,0,1)，但是这无疑不符合真实情况。因此我们对每个渲染点，都定义了一个局部坐标系，在这个局部坐标系里法线方向是(0,0,1)，最终将计算出的法线方向通过坐标变换从局部坐标系变换到世界坐标中。

### displacement mapping 位移贴图
真实改变了三角形的形状
相比于法线贴图：

- 边缘也发生了改变

- 阴影也发生了改变
但是代价是：

- 三角形的面数足够细小

- 至少比纹理要小（同理采样）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020140624.png)

### 3D procedural Noise
上面介绍的纹理应用都是应用在二维平面的，那么很自然就有三维的纹理应用。三维纹理的意思就是除了物体表面有纹理，物体内部也是有纹理的，而内部的纹理通常是通过生成某种三维噪声然后再做处理得到的。比如下图示展示的**Perlin noise（柏林噪声）**，就可以得到一种大理石纹理的效果。
三维空间中的噪声函数，得到一些裂缝？之类的

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020140904.png)

### Provide Precomputed shading
直接把算好的结果放在纹理上（环境光遮蔽），

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020141023.png)

## Introduction Geometry 几何介绍
现实生活中的几何形体应该如何表示？
曲面如何表示？

布料是怎么表示呢？

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020141328.png)

流体是怎么表示的？

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020141403.png)

### Taxonomy

- 隐式几何

	- 满足一定特殊关系的点

	- 例如球：$X^2+Y^2+Z^2=1$

	- 更通用的情况：$f(x,y,z)=0$

	- 缺陷：哪些点在这个方程式？不太直白

	- 优点：判断某点是否在面上

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020142136.png)

- 显式几何

	- 要么直接给出，要么定义映射函数

	- uv映射到xyz

	- 缺陷：无法判断是否在表面

	- 优点：可以更清晰地得到形状的预期？

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020142324.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020142459.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241020141852.png)

### More implicit expression

#### Constructive Solid Geometry
通过基本几何的基本运算来定义一个新的几何。
【Blender里面的布尔做法】

- 交 intersection

- 并 union

- 差异 difference

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241023214501.png)

#### Distance Function （Implicit）距离函数
使用距离函数逐渐进行表面的交融。

- 距离函数：空间中任何一点定义到表面的最小距离
距离函数的例子：距离函数的意思是**会返回当前点与任意物体表面的最短距离**，如果返回的距离是负数，说明这个点在物体内部；如果为正，则在物体外部。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024113516.png)

那么我们只要将两个距离函数做一个融合（blending），随着融合程度的调整，我们可以得到右边一系列的几何图形，给人一种两个水滴合在一起的感觉。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241023214751.png)

例子：
A: 交接的地方为0，远离的左右分别为正负
B同理
A，B可以叠加。【blend】实际上blend的是两者的边界。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024103032.png)

#### Level set Methods (implicit) 水平集
上面的距离函数需要定义出一个解析表达式，但是有时候我们不一定能够求出这个解析式。那么针对这种情况我们可以用level set（水平集）来表示几何形状。

我们看下面的例子来解释什么是level set。其实就是我们给每个格子设定一个值，然后找出值为的地方连起来就得到了level set，连接起来也就形成物体表面。

通过网格的形式来表示之前的距离函数。
地理上的等高线。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024111113.png)

可可以是三维的。三维类似于纹理的映射。

#### Fractals 分形
类似于勾股定理的那个树？
往里面看更加小的部分又是更小的部分？

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241024111310.png)

### Implicit representation 优缺点
优点：

- 表述很紧凑（一个公式）

- 简单的query，在外在内，距离

- 光线追踪简单？
-
