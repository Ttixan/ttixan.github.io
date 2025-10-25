## 目录

- shading 3

	- Barycentric coordinates

	- Texture queries

	- Applications of textures

- Shadow mapping

## Interpolation

为什么需要插值？

- 在三角形顶点上计算（属性）

- 需要得到平滑的过渡(三角形内部获得一个平滑的过渡)

### 重心坐标
每个三角形的重心不同，先定义一个系统

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241016163533.png)

- 只要通过三个数，得到任一点在中心坐标下的表示。

- 并且都为非负数（如果在三角形内）

- 如果满足相加的和为1，则在平面上

举例：

- A点自己的坐标(1,0,0)

#### 面积之比
重心坐标的另一个解释，面积之比

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017121424.png)

定义某个点对应的三角形为对面的。

因此重心的定义：均等分为等面积的三个三角形。1/3

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017121544.png)

### 重心坐标插值
任意一点的值可以是重心坐标下的结果：

- 先算出重心坐标位置

- 再进行插值

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017121740.png)

#### 三维空间属性
注意：重心坐标没有投影下不变的性质
Solution：用三维坐标，而不用投影之后的坐标
如何投影返回去：逆变换

- 3D物体投影到2D屏幕后，点的重心坐标可能是会发生变化的

## 应用纹理 Apply Texture
概念：纹素（Texels）
伪代码：

- 找到纹理

- 查询纹理的值

- 应用纹理

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017122306.png)

但是似乎会出现问题：来自于纹理贴图的大小和像素大小不同的情况。

### 纹理放大 Texture Magnification
如果纹理本身太小，但是需要渲染出来的分辨率又比较大。被拉大的纹理会显得模糊。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017122439.png)

例如：

- 由于分辨率不够，所以很多pixel会映射到同一个texel上

- 因此坐标不是整数：Round为整数。Texel（纹理像素）

- 但是看起来是最左边，看上去是一个一个格子（锯齿化？）

- 希望看起来至少是连续的：右边的
Solution：双线性插值

### 双线性插值 Bilinear
举例:

- 找到邻近的一些像素

- 左下角的水平和竖直距离，分别为s和t

- 线性插值：$lerp(x,v_0,v_1)=v_0+x(v_1-v_0)$

	- 这里的x是一个比例。x 是所需计算的中间位置，取值在 0 到 1 之间

		- 首先计算 v1 - v0，这是端点值之差

		- 然后乘以 x，这是位置系数，表示离 v0 的相对距离

		- 最后加上 v0，就得到了中间位置 x 处的插值值

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017122847.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017123133.png)

#### 三次插值 Bicubic
不是取周围的4个，是取周围的16个。三次插值。【开销更大】
【并没有细讲】

### 纹理缩小
另外一种情况就是纹理相比于要渲染的物体大，这样就会导致纹理缩小，即一个像素会覆盖多个纹素。
Point sampling Texture 点插的问题：走样
看到了近处的锯齿和远处的摩尔纹
造成的原因：

- 纹理分辨率大于要渲染的物体

- 透视造成的近大远小，对于远处的像素而言，一个像素会覆盖多个纹素

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017153131.png)

理解：远近的覆盖像素比例不同

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017153227.png)

Solution：超采样（MSAA），但是计算量增加。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017153420.png)

解决方法，不采样，从点查询变成范围查询。

#### 超采样计算量过大
回到之前的信号的问题：

- 一个像素内有很多材质点，变化的频率太快，所以采样不够，看起来效果不好。

- 因此需要更加高频的的采样方法？

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017153820.png)

solution：

- 不采样，直接得到一个范围的平均值？

### Mipmap（图像金字塔）
允许做范围查询：快，不准确（近似），方形范围的查询
例子：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017153958.png)

类似于马赛克？卷积？分辨率降维？

生成过程：
像素金字塔，层数越高越模糊。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017154138.png)

#### 存储空间
如果想要把每一级都存储起来，额外的开销会增加$\frac{1}{3}$
证明如下【复习等比数列的求和】
>我们知道每一级的面积可以表示为$4^{n-1}$。
>那么对于原本大小为$A_k=4^{k-1}$的纹理，前面$k-1$个项的和为：
>$S_n​=4^0+4^1+4^2+…+4^{k-2}$
>由于等比数列的求和公式：

>![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017155430.png)

>可以看到分母是3，所以额外增加近似于1/3的存储。

因此可以看到很多材质的右下角加入了很多小的材质。

#### 计算过程
计算流程分为：

- 寻找相邻的像素和自己的中心点的连接

- 把pixel映射到texel上，看这两点之间的距离

- 近似为一个方形，取最大长度。作为边长

- 求第几层可以变为一个像素的大小，为边长的log2L层

- 这一层的平均值为可以映射为边长为1的像素。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017160115.png)

可视化结果：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017160440.png)

看到不连续的层上进行查询，需要进行带有分数浮点数的查询：
Solution：进行插值。

#### 三线性插值
进行平均过渡：

- 计算某层的双线性结果

- 两个结果做平均

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017160602.png)

结果：有了过渡

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017160748.png)

#### 不足：Over-blur

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017160853.png)

远处会变得非常模糊
Solution：各向异性过滤（部分解决）

异性过滤会对把原纹理图缩放成不同大小的{矩形}。存储空间是原来的{3}倍。

### Anisotropic filtering
异性过滤会对把原纹理图缩放成不同大小的矩形，各向异性生成的一系列纹理图也叫**Ripmaps**。
可以look-up 矩形的区域

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017161125.png)

对于矩形查询更好，但是没办法查询斜着的、

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017161246.png)

开销：3倍（看矩形的周围的面积）

#### EWA filter
solution：EWA 过滤
任意不规则的形状，可以用圆形来覆盖。
多次查询。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241017161330.png)
