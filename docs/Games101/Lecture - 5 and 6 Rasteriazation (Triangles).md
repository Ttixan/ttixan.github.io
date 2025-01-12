TARGET DECK
other::读书笔记::图形学
FILE TAGS
图形学 Lecture-5

光栅化成像

## Lecture 5 - 目录
- finishing up viewing

光栅化：
- different raster displays
- rasterizing a triangle

Occlusions and Visibility
【遮挡与可见性】

## Perspective projection
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007211839.png)

定义视锥的两个概念：
1.  垂直可视角度（类似于广角？之类的镜头概念）
2.  视角比例？
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006193923.png)
如何和之前的投影之间转化？
- 利用tan
- 利用aspect
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006194324.png)

## Canonical Cube to Screen
将方块投影到屏幕上
Raster 其实是德语中的Screen 
Rasterize 其实就是屏幕化？投影到屏幕上
【暂时】理解屏幕：
- 是一个混合是方块
- 方块混合了 红 绿 蓝（光学三原色）
### 定义屏幕空间(screen space)

像素坐标：
- 整数
- range from 【0,width-1】【0，height-1】
- 但是实际上的中心点:【x+0.5，y+0.5】
屏幕空间
- 和z无关
- 将【-1，1】转换到长宽之间
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006195338.png)
转换矩阵：
- 先把长宽缩放（放大为width和height）
- 再把中心平移到左下角
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006195627.png)

## 不同的显示屏
光栅显示和CRT（cathode ray tube）阴极扫描
- 隔行扫描

Frame buffer-- 内存区域（显存）映射到屏幕上
- 显示的图像就是内存中的一块区域

平板显示设备
- 低分辨显示设备
- 高分辨率（甚至超过人的视网膜分辨率）

液晶显示器（LCD）
- 理论依据：光栅留下某个方向的光的能量
- 理论依据：同通过液晶的扭曲，调整光的方向？

发光二极管（LED）

电子墨水屏幕

## 多边形变换 （Mesh）
这一部分的作用是把不同的形状”打散“到屏幕上，告诉屏幕上每个点的像素值
使用三角形的原因：
- 最基础的多边形（更退化就是线段了）
- 多边形可以拆分为三角形
- 独特性质
	- 内部一定是平面（四边形可以折
	- 内外定义清晰（内外判断简单
	- 插值简单（中心坐标）

重点：判断像素点三角形的位置关系

---
选择三角形作为网格化的三个优点：1. {最基础}的多边形， 2. 多边形可以{拆分}为三角形，3. 三角形的{独特性质}
<!--ID: 1728445533712-->



三角形的三个独特性质是什么？1. 内部一定是{平面}【四边形可以折】 2. {内外}定义清晰【内外判断简单】3. {插值}简单【中心坐标】
<!--ID: 1728445533715-->




## 简单方法-采样
采样是一种离散化函数的方法
给定三角形，判断像素中心是否再三角形内部。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006202126.png)
显像伪代码
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006202442.png)

如何判断某点是否在三角形内？【叉积】

如果在某个边界上怎么办？
- 不做处理【本课】
- 特殊处理

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006202611.png)
算法优化-其实很小的一块区域才在三角形的覆盖范围
- 没有在【min，max】的xy之内的都不计算【Bounding box：包围盒】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006202843.png)
- 狭长的对角线三角形还可以从左右采样来减少计算量
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006203033.png)

---
Q: 包围盒（Bounding boxing）的优化的做法是取三角形的哪两个值？
A: 三个点的最大值和最小值。
<!--ID: 1728445533674-->



Q: 除了Bounding box 还可以怎么优化三角形的内外判断？
A: 从左往右扫描。
<!--ID: 1728445533678-->



## 真实的屏幕光栅化
绿色感光元件更多（更敏感）
bayer pattern
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006203336.png)

### 锯齿！Jaggies
采样率过低--信号走样问题
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241006203630.png)

## Lecture 6 - 目录
antiliasing and Z-buffering
- Antialiasing
	- sampling theory
	- antialiasing in practice
- Visibility / occlusion
	- Z-Buffering

## Artifact
采样会产生artifact（瑕疵）
- 锯齿
- 摩尔纹
来源于奇数行和列的跳过
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007105435.png)
- 车轮效应：人眼的采样跟不上时间（看起来像车轮往后退
本质：信号的变化太快，采样的速度跟不上。

---
采样会产生哪两种瑕疵？1. {锯齿}，2. {摩尔纹}
<!--ID: 1728445533719-->



Q: 产生瑕疵（Artifact）的根本原因是什么？【两个速度】
A: 采样速度慢于信号变化速度
<!--ID: 1728445533681-->



## Blurring（Pre-Filtering） before Sampling
采样之前先做模糊。采样的是模糊的三角形
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007105804.png)
结果：
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007105913.png)

注意：不能先采样再模糊。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007110032.png)

但是为什么？会产生这种走样？

---
Q: 课程提到的一种抗锯齿的方法叫什么？
A: 预滤波（模糊）
<!--ID: 1728445533685-->



Q: 预滤波的先后顺序是什么？
A: 先模糊后采样
<!--ID: 1728445533688-->



### 傅里叶展开
使用sin和cos来表示一个函数
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007110624.png)
傅里叶级数展开--傅里叶变换

---
Q: 傅里叶级数是用什么来表示一个函数？
A: sin 和 cos
<!--ID: 1728445533691-->



傅里叶展开是从{时域}到{频域}
<!--ID: 1728445533722-->



傅里叶展开把函数分解为多个从低到高不同{频率}的函数
<!--ID: 1728445533726-->



### 傅里叶变换
时域--频域
把函数分解为多个从低到高不同频率的函数（不同频率的段）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007110902.png)
从图像来看：采样频率低跟不上函数的变化
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007111139.png)

因此，走样的定义：
>两种频率的函数，给定一种采样方法，无法区分他们

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007111348.png)

---
走样在信号上的表现：两种频率的函数，给定一种{采样方法}，无法区分他们
<!--ID: 1728445533729-->



## 滤波（Filtering）
去掉某些频率
例子：中心为低频，外层为高频。可以用亮度来表示多少。【因此为低频多，高频少】
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007111724.png)
### 高通滤波
【高通滤波】：过滤了低频的信号：
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007112115.png)
为什么高频率的是边界？（变化很剧烈？）
### 低通滤波
只留下低频信息，去掉高频率
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007112342.png)
### 去掉了高频和低频信息
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007112453.png)

---
Q: 高通滤波留下的是图像的什么？
A: 边缘
<!--ID: 1728445533694-->



Q: 低通滤波留下的是图像的什么？
A: 内容（除开边缘）
<!--ID: 1728445533697-->



### 滤波和卷积（平均）
【结论】：时域的卷积等于频域上的乘积。
两种操作：
1. 时域上卷积
2. 频域上乘积再傅里叶逆变换回来
	1. 卷积核也可以傅里叶变换
	2. 留下了低频（模糊）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007113016.png)
#### box 滤波器
box filtering：1/9是为了归一化，防止越来越亮。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007113357.png)
box和频率的关系：越大的box越小的频率范围（越模糊--越小的频率留了下来）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007113555.png)

---
时域的卷积等于频域上的{乘积}
<!--ID: 1728445533733-->


采样的本质是：重复原始信号上的{频谱}。
<!--ID: 1728445533736-->


卷积：频域上的{冲激函数}相乘。
<!--ID: 1728445533739-->



## 采样 Sampling
采样的本质是：重复原始信号上的频谱。
卷积：频域上的冲激函数相乘。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007114010.png)
### 走样 Aliasing
采样慢-频谱密集-重叠的部分就造成了走样
（采样慢-周期长-频率短）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007114637.png)

---
走样的原因：采样慢-频谱密集-{重叠}的部分就造成了走样
<!--ID: 1728445533743-->



反走样在频谱上的反映：过滤掉高频，在进行重复之前使得内容更加{窄}
<!--ID: 1728445533746-->



### 反走样 Antialiasing
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007115257.png)

两种方案：
- 增加采样率（根本上解决，但是比较贵）
- 反走样：
	- 在进行重复之前使得傅里叶内容更加窄（更少的重叠）
	- 比如说过滤掉高频的内容。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007115333.png)

### 实际中（In Practice）
- 先进行卷积操作（模糊）
- 在做采样
例子-前后对比：按照覆盖的面积做一个平均
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007115804.png)

### Antialiasing by Supersampling MSAA（Multisample Anti-Aliasing）
更多采样点 把像素内部多加一些
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007120238.png)
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007120245.png)
判断：小像素n/大像素N = 百分比（之前要求的模糊比例）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007120359.png)
例如下面的2/4=0.5
结果：深浅不同
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007120501.png)
变成box-采样
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007120610.png)

---
Q: MSAA的关键在于M，M的意思是什么？
A: 多重采样
<!--ID: 1728445533701-->



Q: 多重采样的意思是在每个像素里进行什么？
A: 每个像素内进行多个采样来工作
<!--ID: 1728445533705-->



Q: MSAA的目的是计算得到什么？
A: 单个像素的颜色值（三角形覆盖）
<!--ID: 1728445533708-->



### 代价（Cost）
计算量增加。
还有其他的方案（复用等）
- FXAA
- TAA
超分辨率
- DLSS