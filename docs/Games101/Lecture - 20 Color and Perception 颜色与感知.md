## Content
- What is Color
- Color perception
- Color reproduction / matching
- Color space

## Physical Basis of Color
光学基础：牛顿棱镜，光实际上是多种颜色混合而成。

光谱：光线能量再不同波长上的分布。
图形学：关心可见光的光谱

谱功率密度（SPD）：光在不同的波长，强度分布是多少。
对于蓝天来说：小波长，更多看到蓝天
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205142248.png)

不同的光源SPD不一样。不同光线在不同的波长？
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205142319.png)

分布的线性：波长的叠加。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205142349.png)

因此，什么是颜色？
### 什么是颜色？
颜色是人的感知，跟人有关。（跟实际的光不太一样？）
人如何感知颜色？ 

## Perception
眼球的解剖。光线投射到视网膜上，有感光细胞。
- 棒状细胞：感知光的强度，不感知颜色，得到灰度图，数量更多。
- 锥形细胞：感知颜色，数量更少。SML三种类型
	- S：感知短波长
	- M：中段
	- L：长波
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205143737.png)

实际上，每个人的眼睛里的细胞分布并不相同。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205143816.png)

感知的结果就是两个函数相乘积分。
- 给定某个波长，知道光线强度多少
- 考虑不同的SML曲线。
- 将响应曲线和SPD积分。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205145916.png)
因此看到的颜色其实是SML三个数组成的。
看到的是光线光谱积分的结果。
### Metamers：同色异谱现象
调和不同的光谱，使得和我看到的另一个颜色一样。
光谱不同，但是颜色结果一样。（调和）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205150218.png)

## Color reproduction / Match
加色系统
- RGB：加起来最后是白色
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205150333.png)

减色系统：调和所有的颜料最后是黑色。
更改不同颜色混合的比例，得到最后的颜色。

需要减色？的情况就就没办法混合得到一些颜色。
【系数为负数的情况】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205150547.png)

#### CIE RGB 颜色系统
给定某种单一波长的颜色，用三种不同的单色光，混合得到最后的颜色。

下面这张图【匹配函数】：给任何一个固定的波长，需要用多少比例的颜色混合？
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205150801.png)
颜色匹配函数的应用：
- 给定实际的光的光谱，SPD分布，如何计算需要多少RGB
- 每一个波长，考虑需要多少RGB，则为积分（每一条线都是每一个单色光）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205151020.png)

## Color space 颜色空间
sRGB：standardized RGB：标准颜色系统
- 广泛使用
标准颜色空间能形成的颜色是有限的？

### CIE XYZ
CIE XYZ系统：
- 人造定义颜色曲线
- 由于绿色（Y）的分布比较广，覆盖整个波长？所以大概可以表示一些亮度。
- 严格正值

如何可视化XYZ？但是二维显示。
- 归一化，xyz
- 固定Y，显示小写xy
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205151710.png)
色域由上图可知、实际上RGB不能显示整个CIE XYZ的区域

### HSV 
色相、纯度、亮度
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205152340.png)

### CIELAB
红绿、黄蓝、灰白
极限两端为互补色。
互补色是由实验得到的。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205152621.png)

### CMYK：减色系统
打印上的混合墨水。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241205152905.png)
为什么需要K？既然可以混合？三种的价格比一种的价格更贵。