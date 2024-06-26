# 跳板机之便捷管理所有远程内网机器-ssh&scp

## 1. 修改.ssh/config文件 - vscode易用
范例见[config](config)，将系统ssh config文件(vscode的远程配置端点击配置可自动打开此文件)进行参考修改，再远程即可  
BUAA-MC^2 同学可直接参考实时更新的[最新配置](https://raw.githubusercontent.com/Archer-Tatsu/MC-2/master/machine/IRCmachinedocker/code/config): 
配置好~/.ssh/config文件后，在powershell/bash/任何系统命令行内测试:
```
ssh 30901 
#如果需要跳转/多级跳转
ssh 30901 -J jump1,jump2,207,2080,... #每一个代号都是一个配置好的节点，不需要加Proxy参数
# 端口转发
ssh -L 9050:127.0.0.1:8000 30901 #将30901机器(若需跳板机同上)服务器自身(127.0.0.1)的8000端口转发到执行此条命令的本机的9050端口
```
如果是电脑端且安装了vscode，可以安装remote ssh插件，点击刷新后自动显示所有的remote机器-实现sftp+ssh
```
从vscode打开的话是直接加载远程机器的文件系统&终端，如果人在校外/需要跳板机，则需要在config文件对应机器的最后加上
ProxyJump jump1
表示从jump1跳到这里，其中jump1也是一个config配置好的Host。
如果需要多级跳，每一级的机器配一个ProxyJump，保证能链起来即可
```

## 2. 类linux-命令行版配置, 支持多级跳转(默认一级)
见[env.sh](env.sh)  
兼容IPAD/IOS-iSH软件(Alphine系统)，安卓-AidLux/Termux，以及WIN-WSL，MACOS等  
具体ip请根据各自情况修改配置，建议看env.sh注释  
使用实例  
```
#建议看env.sh代码及注释
#1.初始化配置(必须)
. env.sh        #使用默认1号跳板机
. env.sh 3      #使用3号跳板机
. env.sh nojump #不使用跳板机，如已经在内网中/需要多级跳板可使用此项

#2.直接连接跳板机本身(可选)
j2      #ssh连接2号跳板机
s220    #ssh连接到本身可公网直连的服务器

#3.连接内网机器(可选)
s518    #第一步中选择的跳板机/无跳板机进行内网机器ssh连接
### 多级跳板ssh[注意规则]-无视默认选择
ssh ywz@$ip518 -J $jump1,$jump2,$jump3 #跳板顺序为: jump1->jump2->jump3->ip518

#4.映射内网机器端口(可选)
# mapping函数主要用来端口映射，方便scp/sftp/打开浏览器查看面板等高级操作 搭配本机ip固定127.0.0.1进一步使用
mapping $ip518 22 9050 #将内网机器的22端口(默认ssh端口) 映射到本机的9050端口，使用默认跳板机
### 多级跳板后映射机器端口[注意规则]-无视默认选择，但至少输入一个跳板机
mapping $ip518 22 9050 $jump1 $jump2 $jump3 #端口映射多级跳转规则, jump1->jump2->jump3->ip518

#5.查看配置的内网机器ip(可选)
echo $ip518

#6.查看使用说明(可选)
help
```

## 3. mobaxterm-配置-仅限win用户
### 3.1端口映射  
<img src=".img/chuantou.png" style="zoom:30%;" /><br>  
原理参考env.sh中端口映射mapping函数，改为图形化操作：将本地端口映射到远程内网机ip+端口  

### 3.2跳板机代理ssh  
原理参考env.sh中跳板机代理ssh，改为图形化操作：编辑Session-正常填写host和用户名、端口(默认22). 填写完成后再填写跳板机配置: 下方Network Settings-Connect through ssh gateway-填入跳板机ssh映射的公网ip和端口号以及跳板机的随意一个账号即可

<br>
<br>
<br>
<br>


# [多开发/执行机器协同开发git管理参考](../中心化多机器开发推荐配置.md)
