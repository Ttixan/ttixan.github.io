## Appearance of Natural Materials
外观是材质和光线共同作用的结果

### What is Material in Computer Graphics
镜面反射，漫反射，渲染方程里：BRDF决定了不同的材质

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117202604.png)

#### Diffuse / Lambertian Material
进入的光是uniform，反射的光是uniform
利用能量守恒，Irradiance不会因为反射而改变。
积分之后（在brdf和入射为常数的时候），得到反射系数：$f_r$

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117203023.png)

#### Glossy material BRDF

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117203131.png)

#### Ideal reflective material
一部分反射，一部分折射。右边的部分：有吸收，才会出现颜色。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117203225.png)

#### Perfect specular reflection
法线方向是初设+入射。
给定初设还可以反过来算入射。
还有不同的方法计算角度（计算$\phi$ 和$\theta$ ）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117203414.png)

### Specular Refraction 折射
不同波长不同的折射率。
Costics：光线在海水表面。海底有几率即受到各个方向的光，在某些地方会形成光的条

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117204011.png)

如何计算折射方向？

#### Snell's Law 折射规律-斯内尔定律
不同的材质有不同的折射率。
折射率x入射角等于

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117204125.png)

如果：计算不出有意义的实数，那么折射就不可能发生。
根号内部小于0（计算cos的意义）

- 只能是$\eta_i$大于 $\eta_t$

- 入射介质大于折射介质的折射率，则为不会发生折射（全反射现象）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117204425.png)

那么人在水底只能看到一个锥的部分。
折射只能看到小的区域。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117204518.png)

所以BRDF+BTDF = BSDF（反射+折射的统称）

#### Fresnel reflection / Term 菲涅尔项
有多少光能被反射可以是由入射光决定的（角度）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117205615.png)

绝缘体的菲涅尔项告诉我们：
方向平行则基本上反射掉，如果基本垂直则为折射。【SP是极化问题，暂时不考虑】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117205702.png)

生活中：汽车前排窗子看起来是反射，靠近的窗子是折射（透明）
导体的菲涅尔项：基本上是反射

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117205849.png)

如何知道计算公式（近似）【Schlick's approxiamation】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117210128.png)

其中：认为曲线从0开始，到90度的时候为1
并且基准反射率和折射率有关

### Microfacet Material 微表面模型
只要离得足够远，看不到表面微小的改变，只能看到一个整体的作用。【现象】
假设：

- Macroscale：平面并且粗糙【看到的是外观】

- Microscale：起伏并且镜面反射【看到的是几何】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117210619.png)

#### Microfacet BRDF
了解法线的分布：基本上集中在宏观的向上
如果表面粗糙：各个方向，分布比较远（方差大）
因此微表面模型可以利用法线分布来描述反射的情况。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117210835.png)

公式：

- 菲涅尔项

- 法线分布（用半程向量表示，反映多少光可以反射）

- 几何项（由于shadowing masking导致的投影，遮挡，看不到的微表面，失去了作用）

	- 几乎和面平行的入射方向，Grazing angle就会发生这种现象（自遮挡）用于修正这部分特殊情况

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117211248.png)

## Isotropic / Anisotropic Materials（BRDFs）
区分材质的方式
观察这个电梯的例子：由于电梯的表面的金属似乎被按照某个方向磨过，所以高光变成了条状（和平常的不一样）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117211655.png)

被叫做：各向异性/各项同性材质。
可以从微表面的看出：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117211824.png)

需要重新定义BRDF：

#### Anisotropic BRDFs 各向异性材质
如果不满足旋转一定的角度之后，看到的BRDF不一样，则说明是各项异性。【绝对角有关，而不是相对角】

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117211931.png)

## BRDF的性质

- 非负性

- 线性性质：可以直接线性相加

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117212335.png)

- 可逆性：交换入射和出射的角色，得到的结果依然是一样的。

- 能量守恒定律：不可能让能量变多（但却是可能有部分被吸收）

- 各向异性vs同性：之和相对角有关，原本的四维可以转化为三维的

	- 还可以不考虑正负，只考虑绝对值。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117212658.png)

## Meansuring BRDF 测量
实际测量和数据推演不一样。是否可以直接用测量结果作为渲染的数据？
枚举所有的初设和入射方向，测的出来所有的radiance
【有很多加速的方法】
测出来之后，进行存储。
MERL BRDF database

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241117213149.png)
