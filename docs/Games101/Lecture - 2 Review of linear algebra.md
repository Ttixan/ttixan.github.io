## 所需前置知识
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916113732.png)

- 数学
	- 线性代数，微积分，统计
- 基础物理
	- 光学，力学
- 很少的
	- 信号处理
	- 数值分析
- 和一点的美学
## 基础知识

### 向量
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912113909.png)

### 向量正则化
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912113933.png)

- 长度
- 单位向量。magnitude（大小，长度？），用于表示方向


### 向量加法
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912114054.png)
### 正交单位
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912210937.png)
### 向量乘法
#### 点乘
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912211021.png)

性质：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912211048.png)

多维

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912211128.png)

- 用处
	- 找到夹角
	- 寻找投影

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912211248.png)

向量分解

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240912211341.png)

点乘在graphics的应用

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916112152.png)

- 方向上的接近
- 分解向量

#### 叉乘 cross product
计算出的叉积和两个向量都要垂直。垂直于a和b所在的平面。

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916112359.png)

- 右手定则，决定方向。
- 向量叉积不满足交换律
- 可以得出三维空间。

叉乘的性质3：叉乘满足分配律：A×(B+C)=A×B+A×C


![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916112743.png)

- 右手坐标系：X x Y = Z
- 计算方法，笛卡尔坐标系

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916112947.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240925211012.png)

作用
- 判定左右（和z的方向进行比对，顺时针逆时针）
- 判定内外（在某个顺序连接的三角形的外侧，右侧）三角形光栅化的基础

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916113042.png)

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916113331.png)

### 矩阵
#### 矩阵变换
mxn m行，n列
矩阵乘法
矩阵乘积
MxN NxP = MxP
#### 性质
- 无交换律
- 结合律
- 分配律
#### 矩阵向量乘法
- 左矩阵，右向量，mx1
#### 转置
- 行编程列，列编程行
- 转置的性质

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916114506.png)

- 对角矩阵，单位矩阵
- 逆矩阵，相乘为单位矩阵

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916114627.png)

