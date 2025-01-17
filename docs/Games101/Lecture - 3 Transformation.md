## Application
- camera 变化
- ik
## Why
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916144521.png)
 从三维世界到二维的逻辑


## 2D Transformations

### Rotation, scale, shear
思路，找前后对应关系。

#### Shear Matrix
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916145907.png)
向右移动，x=ay（k=1/a)。所以应该是原本的x（1）+y（a） 
#### Rotate
默认从原点开始，从逆时针开始旋转。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916150643.png)

推导过程：列出两个方程，分别为（1，0）和（0，1）的坐标前后变换的等式。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916150627.png)
### Representing transformations using matrices
#### 线性变换概念
可以用矩阵相乘表示，线性变换
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916150801.png)

## Homogeneous coordinates 齐次坐标
### Motivation
Motivation：不希望把平移变换独立出来，希望也用一种简单整合的方式表示。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916151259.png)


### Solution
Solution，把维度拓展为3个，加法可以加入。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916151518.png)
向量具有平移不变性：所以vector后面是0。


### Properties
性质：加减性质是否保留
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916152021.png)
- 点+点=中点（齐次坐标系下）


### Affine Transformation 仿射变换
结构：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916152245.png)

 - 左上角是原本的变换矩阵
 - 右边两个是移动
 - 最下面是001 （只有在仿射变换的时候是001）
其他例子
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916152330.png)


### Inverse Transform 逆变换
结果是乘逆矩阵
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916152544.png)


### Composite Transformation 变换的组合
Solution：多个简单变换的组合
Insight：矩阵乘法的顺序会影响结果 （因为不满足交换律）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916152828.png)
概念的推广：多个矩阵相乘
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916153104.png)


### Decomposing Complex Transform 变换的分解
沿着某个点旋转的方法：移动回原点-旋转-移动回去
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916153641.png)

## 3D Transform
结果是扩展了一个维度，保留之前2维的性质
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916154036.png)
顺序：先线性变换再平移。
以下为Lecture 4 
  ### 缩放 平移
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916194407.png)
### 旋转

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916194432.png)
为什么ｙ的角度不对？因为按照右手螺旋定则，应该是ＺｘＸ而不是ＸｘＺ得到Ｙ，所以是反向旋转。



#### 分解复杂角度
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916195357.png)

#### 绕某轴旋转的向量
罗德里格斯
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916195635.png)
在原点的旋转（默认）
不再原点的轴的旋转：和上节课一样，先移到原点再旋转，之后再复位。

## Viewing transformation（观测）
### 流程
类比于正在拍照片

- 寻找一个地方和人（model transformation）
- 找到合适的摄像机角度（view transformation）
- 照相（projection transformation）

#### 定义相机
- 位置
- 视角方向
- 向上方向（类似于画幅旋转），相机绕着视角方向的轴旋转。
一般来说我们希望相机始终位于原点，而且相机是正摆放的(Y轴正方向)，拍摄方向是朝着正前方拍的(Z轴负方向)
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240916201245.png)


#### 关键观察
目的：完成初始化

- 没有相对运动，拍出来的东西不变。
- 先把相机移动到0，0，0。向着-z方向看。
- 和相机一起移动物体

#### 变换过程 how to
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918213144.png)

- 平移矩阵【移到原点】
- 过渡矩阵
	- 过渡矩阵本身不好求，所以求逆
	- 逆矩阵求出来之后，由于这个过渡矩阵是正交的，所以直接求转置则为逆。
		- **正交矩阵**：一个矩阵 $Q$ 被称为正交矩阵，如果满足 $Q^TQ=I$，其中 $Q^T$ 是 $Q$ 的转置，$I$ 是单位矩阵。
		- 旋转矩阵是正交的，而且多个旋转矩阵相乘也保持一样的性质。齐次坐标系下也一样。
		- 根据定义，逆矩阵意思是$AA^{-1}=I$，所以正交矩阵的逆矩阵 就是其转置。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918213737.png)

## Projection transformation（投影）
- 将3d转化到2d上
- 两种，正交和透视
- 以是否有近大远小的区分。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918215342.png)


#### Orthographic projection（正交）
- 将相机放在某位
- 将z轴直接丢掉
- 得到x，y，做一个【-1，1】之间的缩放
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918215550.png)
- 更正规的做法：先平移，再缩放。
- 【l,r】【b，t】【f，n】左右，前后，上下。far near（z）注意值，远近是由于-z，远的地方其实值更小。（右手系）
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918215750.png)
- 数学公式。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918220035.png)


#### Perspective projection（透视）
透视投影矩阵=正交投影矩阵x透视变正交矩阵
所以需要先求出透视变正交矩阵，再做一次正交投影的变化。

- 等比放大
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918220928.png)
- 流程：把平面挤一挤，再变成正交投影。
	- 远近平面上各自的z不会变化？
	- 中心点不变
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918221216.png)
- 挤压的具体操作：基于相似三角形
	- 由距离推算出。通过【相似三角形】得到xy坐标的关系
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240918221552.png)
- 由于之前提到的乘k之后点的性质依然不变，所以暂且把得到的点乘z。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919214200.png)

- 之后已经可以得到【除了第三行的】转换矩阵内容。
- 前两行的内容。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919213658.png)
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919213536.png)

- 需要根据【之前规定的】两个点得到两个不等式。从而推算出第三行的内容。
	- 近平面上：所有点不会发生变化。近平面上z为n，所以坐标是（x，y，n，1）
		- 但是表示方法在齐次坐标系下可以根据矩阵乘变成n乘。这样会更方便之前的unknown形式直接求解。
		- 由于$n^2$与xy无关，所以第三行前两列为0，0。后面的数暂且列为等式。
	- 远平面上：z不会发生变化。
		- 取中心点的特殊性质：中心点挤压之后不发生位置偏移。
		- 00f1转换之后依然是00f1，根据上面的f乘得到$f^2$和$f$ 。（方便替换z直接做等）
		- 得到不等式。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919213332.png)
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919214908.png)
- 最后求解出A，B的值。
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20240919213040.png)


[深入理解透视矩阵 - zhyingkun](https://www.zhyingkun.com/perspective/perspective/#:~:text=%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%E9%80%8F%E8%A7%86%E7%9F%A9%E9%98%B5%C2%B6.)

得到了透视变正交矩阵和正交矩阵，最后相乘得到：
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007213126.png)


粘贴自lecture5（上节课没讲完的）
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


## 附录：代码作业

最后的答案为：
```C++
#include <Eigen/Dense>
#include <cmath>

Eigen::Matrix4f get_projection_matrix(float eye_fov, float aspect_ratio, float zNear, float zFar) {
    // 将视场角从度转换为弧度
    float fov_rad = eye_fov * M_PI / 180.0f;

    // 计算投影矩阵的参数
    float tan_half_fov = std::tan(fov_rad / 2.0f);
    float range_inv = 1.0f / (zNear - zFar);

    // 创建投影矩阵
    Eigen::Matrix4f projection = Eigen::Matrix4f::Zero();
    projection(0, 0) = 1.0f / (aspect_ratio * tan_half_fov); // x轴缩放
    projection(1, 1) = 1.0f / tan_half_fov;                  // y轴缩放
    projection(2, 2) = (zNear + zFar) * range_inv;           // z轴缩放
    projection(2, 3) = 2.0f * zNear * zFar * range_inv;     // z轴偏移
    projection(3, 2) = -1.0f;                                 // 透视效果
    projection(3, 3) = 0.0f;                                  // 齐次坐标

    return projection;
}
```
![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007213656.png)

>大部分资料跟书上推导出来的透视投影矩阵一般是由fov,aspect,far,near四个参数数定义的，我们现在来看下我们前面求的透视投影矩阵转化成由上面四个参数定义的形式。

推导过程：

![image.png](https://picbed-1305808788.cos.ap-chengdu.myqcloud.com/img/20241007213722.png)
