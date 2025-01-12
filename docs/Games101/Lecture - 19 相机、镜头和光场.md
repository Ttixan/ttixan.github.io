## Content

## Imaging 成像
成像 = 模拟 + 捕捉
### What‘s the Camera
相机的内部结构如何？
相机的最古老现象：小孔成像
棱镜：
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121203022.png)
快门：控制光多少进入相机
传感器：计算Irradiance，在整个暴露的过程中

### Pinhole Camera：针孔相机
特点：
- 没有任何的景深
- 看不到任何的虚化的地方，
- 光线追踪的时候用的针孔摄像机

### Field of View：视场
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121203539.png)
什么因素可以决定视场？
- 传感器的高度
- 传感器和棱镜之间的距离（可以暂且称为焦距）

不同的视场有不同的拍照结果：
- 35mm的胶片作为基准
- 对应如果是35mm的胶片，焦距应该是多少【等效焦距】
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121203916.png)
例子：越窄越远
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121204048.png)
平时使用：固定传感器的大小，改变焦距来改变成像的大小。
胶片和传感器大小不一样，好的相机，大的相机，更高的分辨率
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121204306.png)
对于手机来说，更小的传感器，更小的焦距，达到一样的图像

## Exposure：曝光
H=T x E
曝光 = 曝光时间 x irradiance
- Time：【延长快门时间】如果用更长的曝光时间就可以换来更亮的图片
- Irradiance：光圈（aperture）的大小会影响irradiance
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121204504.png)
### Exposure Control：曝光控制
光圈大小：
- F-stop来控制光圈的大小，F越小，光圈越大
- 光圈类似于瞳孔
	- 更亮，缩小
	- 更暗，放大
快门速度：
- 改变快门开放的时间，速度越快开放越短
ISO gain(感光度)
- 后期处理，接收到的光x某个数值？
- 可以是硬件上的：调节sensor
- 也可以是软件的：数字信号上调节
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121204907.png)

为什么会模糊？
- 光圈大，一定区域会变得很虚？
- 快门时长，为什么人会变得模糊

#### ISO的解释
信号有噪声，如果相乘一个噪声，不仅放大信号，也会放大噪声。
为什么会有噪声呢？
光如果理解为光子的话，快门时间不够，光子进入不够，看到的就是噪声。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121205348.png)
#### F-Stop：光圈的解释
两种写法：
- FN或者F/N 只关心后面这个N
- 简单理解：F-Stop的数字是光圈的直径的逆（反比例函数？）
快门的过程：
- 完全关闭再打开的过程是【我们关心的过程】
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121205654.png)
除了调节曝光度，还有什么作用？
- 运动模糊（Motion Blur）：在快门打开的时间内，物体已经进行一些运动了
	- 那么所有的运动过程也会被记录下来
	- 结果就是平均下来的图像

但是运动模糊一定会坏事吗？
- 不一定：可以用来表示速度感（赛车游戏）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121210006.png)
如果快门采样时间的比不上高速运动的时间
Rolling shutter：扭曲的螺旋桨
- 是由于不同位置在不同时间采样的原因
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121210215.png)

可以用ISO和F-stop来进行互换
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121210329.png)
但是这样的代价是牺牲了景深。和运动模糊

#### Thin Lens Approximation 棱镜
假设：一种理想化的薄棱镜
光线穿过焦点后，变成平行光。
可以使用棱镜组的组合来模拟这种可以改变焦距的理想薄棱镜。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121211101.png)
定义：
- 物距，像距，焦距
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121211207.png)

#### Defocus Blur
 CoC （Circle of Confusion）：
 - 光经过聚焦的某个点之后进行发散
 - 发散后的一段距离都是一个图像
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121211805.png)
结论：CoC的大小和Apeture的大小都是成比例的
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121211908.png)
因此联系起来之前的F-stop
F数量的计算，F/D（光圈大小）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121212042.png)

CoC的大小=F/N，因此和N有反比关系
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121212122.png)

#### Ray Tracing for Defocus Blur
先定义各种参数：
- 棱镜，焦距，物距等
- 利用棱镜的成像公式进行计算
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121212708.png)

### Depth of Field：景深
大的光圈大的COC，会更模糊
但是总归有一段距离的Focus Plane不会模糊：那么这段模糊的范围该如何定义？
如果有光经过透镜，在成像平面的一段平面内，COC足够小，不足以变得比较模糊？【比如比像素小，都可以认为是锐利的？】
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121213244.png)

所谓DOF就是某一段深度，焦距和成像的景深联系起来。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241121213512.png)

## Light Field / Lumigraph
【这个是在lecture20讲的，但是内容是本届的】
光场命名历史遗留问题，两个都可以。

### 我们能看到什么？
假设我们坐在一个屋子里看东西，如果之前有一个成像平面，把所有的信息都记录在这个平面上，和屋子里看真实场景一样的，那么就是虚拟成像。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205104436.png)

描述我们看到了什么？全光函数
#### 全光函数
描述了我们能看到的所有东西。
定义一个函数，我往任意一个方向看，可以看到什么像素？
再改进一下：灰阶-引入波长-彩色
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205104540.png)
再改进一下，扩展时间t：电影。在不同的时间显示不一样。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205104635.png)

再改进一下：人物可以移动。全息电影。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205104708.png)

换个角度，不把其当电影的函数看。那么就定义了全光函数：
- 任何时间
- 任何方向
- 任何地点
看到的内容。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205104840.png)
### Sample Plenopic Functon
光场，就是全光函数的一小部分，从其中的采样。

Ray：定义光线
- 需要起点，需要方向（类似于之前光线传播的定义）

Ray Reuse：新的定义方法
- 两点确定方向
- 2D位置
- 2D方向

光路可逆性来描述一个物体：物体在包围盒上，任何位置，向任何方向发射出去的光线。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205105242.png)
总结光场的定义：物体在任何一个位置，往任何一个方向，去的光的强度。
光场只是全光函数的一个子集：2D的位置（uv)，2D的方向（theta，phi）。

### Synthesizing novel Views
有了光场之后，可以得到物体任意一个位置看向物体的光的强度？【4维函数】
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205105635.png)

作为观测的幕布，只关心观测到的结果，不关心包围盒内部的内容。
只需要记录从外面观测的2D的方向和位置。

对于平面上任意一点，只需要关心位置即可（过点s）
那么可以使用两个平面来定义光场（之前光线的另一种定义）
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205105932.png)

### 参数化过程
uv和st其实就是光场的参数化过程。分别表示的两个平面上的点。
只需要枚举所有uv和st的可能性组合，就可以描述这个光场。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205110030.png)

例子：
从UV向着ST看，从很多个角度看到的整个世界的图。
从ST向着UV看，反过来想，UV都看向ST上的同一个点。
可以理解为看得同一个东西，从不同的角度看？一个像素上存储的irradiance。展开为radiance
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205110721.png)

光场摄像机的原理：看一个像素实际上是看穿过这个像素的各个方向的光。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205111235.png)

### 光场摄像机
先拍照，再调焦。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205111454.png)
光场摄像机，每个像素记录的是各个不同的方向。如果是传统摄像机，则记录的可能是平均的像素。把各个不同方向上的光记录下来。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205111839.png)

如何还原为简单的照片内容？都寻找一条光线的内容，平均起来。
![image.png](https://gitee.com/dontt/picgo-img-bed/raw/master/img/20241205112306.png)
