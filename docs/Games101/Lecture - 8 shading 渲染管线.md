## Lecture 8

### Specularly reflected light 高光
高光的产生：是由于观察的方向和镜面反射方向接近：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010194721.png)

另一种方法：使用平分线方向

- l和v相加得到平分线向量（bisector）

- 如果h和n法线接近，等同于上述的n和v接近（越接近越亮）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010194830.png)

为什么需要指数？（p的用处）
夹角余弦的变化趋势过于平缓，所以需要修正一下：
例如45°都可能还有高光。修正指数使得只有20°左右才有高光。（面积更小）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010195234.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010195420.png)


### Ambient Term 环境光照
假设：

- 不讲究从哪里来（哪里都有）

- 从哪里看，都一样（和观测方向也没关系）

- 所以应该是一个常数（某一种颜色？）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010195940.png)


### 总和
把所有的加起来：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241010200121.png)

### Shading type

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015194848.png)

着色的点不同

- Flat shading：整个面着色

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015194954.png)

每个多边形（如三角形）使用统一的颜色，这个颜色通常是基于多边形的法线和光源的相对位置计算得出的。

- Gouraud shading：顶点着色-法线-插值

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015195003.png)

Gouraud shading 是一种更复杂的光照模型，它在顶点处计算颜色，并通过插值在多边形的表面上进行平滑过渡。

- Phong shading: 每一个像素

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015195040.png)

Phong shading 是一种基于每个像素的光照计算方法。这种方法使用每个像素的法线、视线方向和光源方向进行计算，以实现更精确的高光和细节表现。

#### Shading Frequency: Face, Vertex, or Pixel

几何够复杂的情况着色简单也能有好的效果，取决于具体的物体

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015195302.png)

#### Defining per-vertex normal vector (求点的法线)

1. 考虑表示的是什么图像，从中心延申出去

2. 直接相加各个面的法线

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015195641.png)

### Real-time Rendering pipeline 渲染管线

1. 输入一些点

2. 进行投影到屏幕上

3. 连接成为三角形

4. 离散化为像素，Fragment

5. 对像素进行着色

6. 在屏幕上显示

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015200225.png)

现代的渲染管线，有些过程是可编程的。所以实时渲染就是在写这些处理如何运作。就是写Shader：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015200622.png)

#### Shader Programs
不需要写for循环，只定义每个顶点或者像素的操作。

- vertex shader

- fragment shader

可参考网站：Snail shader Program

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015201415.png)

#### Goal: Highly Complex 3D Scenes in Realtime
虚幻引擎的例子：

- 一次性导入数千万个三角形

- 其他高性能

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015201527.png)

#### GPUs
高度并行的处理器，专门用于处理图形的计算。（并行计算）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015201754.png)

### Texture Mapping 纹理映射
定义：
>**纹理（Texture）**：纹理是一种二维图像或图案，用于在三维模型的表面上提供细节和视觉效果。纹理通常由像素构成，可以包含颜色、亮度、透明度等信息。

有一种方法：可以定义任意一个点的属性（漫反射系数？还有其他属性）
球的红黄蓝颜色

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015202241.png)

理论假设：三维物体的表面其实是二维的（可以被展开）

- 所以物体表面可以和图有一一对应的关系。（纹理的本质）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015202428.png)

- 任意一个点都可以找到模型上的对应位置。
题外话：参数化研究（不需要管怎么产生的映射的关系，假设已经知道了）

#### 映射过程

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015202801.png)

1. 定义了每个点的坐标（u，v都是【0，1】）

2. 可以反复映射（一个纹理用很多遍）

	1. 需要设计的好，才能上下左右无缝衔接。

	2. 图形学中叫Tiled（需要计算）

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241015202856.png)

#### Interpolation Across Triangles：插值
三角形内部的平滑过渡。基于三角形三个顶点。