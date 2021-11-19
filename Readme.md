# team8-Citation network-based paper retrieval engine



## 项目说明

### Project3:  基于引文网络的论文检索引擎

引文网络是由文献间引用和被引用的关系构成的集合。该网络中的节点是文献，边代表了文献间的引用关系。

#### 数据处理模块

+ Semantic Scholar上从2000年以后的英文论文，大小为**120G**。以`sample.jsonl`为例，每行为一条数据，包括论文标题、论文引用和被引关系等字段。完整数据请在确认选题后找助教拷贝

##### 要求

+ 使用大规模数据处理技术，例如Spark
+ 构建**引文网络**来计算论文重要性分数
    + 使用的算法必须说明原理
    + 基于引文网络的重要性分数必须作为一个字段保存进MongoDB数据库

#### 检索模块

+ 搭建Elasticsearch实现从某一个或若干字段检索
+ 再**结合**引文网络重要性分数对检索结果进行调整，对比二者，期望引文网络重要性分数对搜索结果有所改善，能结合**具体案例**分析说明
+ 当选中一篇论文后，能够以该节点为中心展示引文网络子图
    + 应当包括之前和之后的节点
    + 应根据节点互相引用的关系、节点重要性筛选出一定数量的节点用于展示
    + 应提供引文网络子图的节点和边的信息，并和展示模块商量好接口定义

#### 展示模块

- 设计并实现一个学术论文搜索引擎网站，包括三个页面

    - 首页/搜索页
    - 检索结果列表页，要求：
        - 可以显示ES基础检索结果列表
        - 可以显示基于引文网络重要性分数改善后的检索结果列表

    + 论文详情页面：

        + 基于选中的论文，可视化一个**引文网络子图**，可以参考https://www.connectedpapers.com/。根据重要性分数，节点的大小或颜色应该有所区分

        <div align="center">
          <img src="imgs/5.png"/>
        </div>

- 推荐使用Python Django（[https://www.djangoproject.com](https://www.djangoproject.com/)）库来实现

#### 提交内容

+ 一个MongoDB数据库，包含引文网络重要性字段
+ 引文网络的统计信息，节点数、边数、最大出入度等
+ 展示基于引文网络的论文检索引擎的检索结果，并能结合**具体案例**说明基于引文网络的重要性分数对检索结果的改善
+ 展示引文网络子图的可视化效果



## 项目配置

### 服务器信息

* 系统：Ubuntu 18.04 LTS
* ip：10.108.17.104


* ssh port：22


* ps：本服务器为校园网内网服务器，请于校园网环境使用


### 账户信息

### 1. root

账号：root

密码：000000

### 2. test

账号：test

密码：test

### 文件结构

#### 1. 用户个人空间

每个账户创建后，均会在`/home`路径下创建个人存储空间，路径为`/home/username`

ps：请将个人数据存放在该路径下

#### 2. 引文原始数据

已经将助教给出的引文原始数据存放于`/home/data`路径下

#### 3 服务器存储结构

| 目录  | 大小 | 挂载点    | 硬盘 |
| ----- | ---- | --------- | ---- |
| EFI   | 500M | /dev/sda1 | SSD  |
| /boot | 500M | /dev/sda2 | SSD  |
| /swap | 16G  | /dev/sda3 | SSD  |
| /     | 105G | /dev/sda4 | SSD  |
| /home | 3T   | /dev/sdb  | HDD  |

ps：请将大型数据存储在`/home`路径下，`/`路径容量不大



## 项目环境

### ES

* version: v7.15
* ip: 10.108.17.104
* port: 9200

### MongoDB

* version: v3.6.3
* ip: 10.108.17.104
* port: 27017
* 数据文件位置： `/home/db/data`
* 日志文件位置：`/home/db/log`

### · Python环境

个人Python环境请使用`miniconda`进行创建和配置，尽量不要使用sudo安装，以免污染他人环境。



## 常用命令

### 1. 校园网登入、登出

脚本路径`/home/public`

```shell
cd /home/public
# 登入命令：
bash weblogin 学号 密码
# 登出命令：
bash weblogout 学号 密码
```

### 2. MongoDB

```shell
# 登入root用户
su
# 进入MongoDB的tmux环境
tmux a -t mongodb
# 启动MongoDB服务
service mongodb start
# 停止MongoDB服务
service mongodb stop
# 重启MongoDB服务
service mongodb restart
# 进入MongoDB
mongo
# 查看所有database
show dbs
# 查看所有collections
show collections
# 创建database
use db_name
# 创建集合
db.createCollection("collection_name")
# 删除集合
db.collection_name.drop()
```

### 3. ES

```shell
# 登入lsh用户
su lsh
# 进入ES的tmux环境
tmux a -t es
```



## 提交说明

请在`project3-team8`中创建个人分支，将所有修改提交到个人分支中，确定无误后再合并至主分支，以避免污染主分支，并且方便出现问题后进行回滚操作。

