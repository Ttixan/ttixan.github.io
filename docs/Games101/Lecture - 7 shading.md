## Lecture 7 Visibility and occlusion
本课学习遮挡关系和 可见性

### Painter's Algorithm
油画：从远到近画东西（Overwrite）
新画的东西覆盖旧的东西。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009181925.png)

缺陷：

- 需要先按照深度进行排序（$O(n log n)$）

- 但也有无法解决的情况（相互重叠）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009182155.png)

---
画家算法：新画的东西{覆盖}旧的东西。
<!--ID: 1729258257431-->

Q: 按照画家算法，不能解决的问题是什么？
A: 三角形相互重叠。
<!--ID: 1729258257417-->

Q: 针对画家算法不能解决的问题，提出了什么算法？
A: Z-buffer 算法
<!--ID: 1729258257423-->

### Z-buffer
对三角形的（采样到的）一个最小的像素来进行排序，而不是对于品面。

- 需要额外的buffer来存储深度信息

	- Frame buffer

	- depth buffer
例子：越近越深，越浅越远

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009182614.png)

伪代码：

- 任意一个三角形上采样的任意一个点

- 如果比zbuffer里的最小值更小则进行zbuffer的更新

- 并且更新framebuffer的rgb值（存储颜色

- 否则的话什么也不做。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009182903.png)

例子：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009183142.png)

缺陷：

- n个三角形的复杂度为$O(n)$

	- 居然小于$nlog(n)$是因为顺序写三角形上去

- 但是如果三角形的顺序不一样？

	- 由于每个float都不一样，所以不影响
---
Q: Z-buffer算法的伪代码
A:

### Shading 着色
需要着色才能知道面的朝向，以及不同的颜色。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009210806.png)

课程中关于shading的定义：
> 将材质应用于一个物体的过程

### Simple shading model （Blinn-Phong reflection model）
概念解释：

- 高光：Specular highlights

- 漫反射：Diffuse reflection

- 环境光照：Ambient lighting

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009211503.png)

有了这些就可以模拟一个光照的感觉？

---
布林冯shading由三部分组成，分别为：{高光}、{漫反射}、{环境光照}。
<!--ID: 1729258257435-->

关于shading用到的概念【英语】：高光：{Specular highlights}，漫反射：{Diffuse reflection}，环境光照：{Ambient lighting}
<!--ID: 1729258257438-->

有关变量定义：【以下均为单位向量】

- 着色点：shading point

- 法线：n

- 观测方向：v

- 光照方向：l

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009211626.png)

---
Q: 着色模型的输入
A:

#### shading != shadow
着色不考虑其他物体：例如下面这个物体，如果有某个投影，不考虑。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009212113.png)

---
Q: 着色模型不考虑其他物体的阴影，所以没有什么？
A: 没有影子。Shadow。
<!--ID: 1729258257426-->

#### Diffuse Reflection 漫反射
漫反射光线从各个方向分散

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009212321.png)

漫反射会接收到多少光？由单位面积有多少光的能量决定：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009212848.png)

- 由于倾斜，所以单位面积的光能量少了，所以显得更暗

关于离光源远近而导致的强度不同（光的衰减）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009213521.png)

- 总能量相同的情况下，面积越大，某点的能量越小。

- 从而推算出某一点的亮度的公式：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009213633.png)

- 吸收的能量：点乘。【漫反射光的强度近似地服从于Lambert定律，即漫反射光的光强仅与入射光的方向和反射点处表面法向夹角的余弦成正比。】

- 有颜色的原因：吸收一部分能量，反射一部分能量（波长不同）【系数的来源】

- 漫反射项和观察的方向无关。（公式中没有涉及到角度）

例子：为什么有的地方黑9明暗交界线：因为法线垂直于光线。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241009214118.png)

---
漫反射能接收到多少光，由{单位面积}有多少光的能量决定。
<!--ID: 1729258257442-->

倾斜带来的变化是，与光线方向越{垂直}，则越亮。
<!--ID: 1729258257445-->

距离带来的光线变化是，光线强度和{距离的平方}成反比。
<!--ID: 1729258257450-->

某点光线强度和距离的关系，基于的是{面积}内光的能量相同。
<!--ID: 1729258257453-->

漫反射光的强度近似地服从于Lambert定律，即漫反射光的光强仅与{入射光}的方向和反射点处{表面法向}夹角的{余弦}成正比。
<!--ID: 1729258257457-->

漫反射项和观察的方向{无关}。（公式中没有涉及到角度）
<!--ID: 1729258257460-->

漫反射系数$k_d$决定了物体的{颜色}。
<!--ID: 1729258257465-->
