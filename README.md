# HighRiskPort
总结一些渗透中值得关注的默认端口。程序调用nmap扫描特定的敏感端口，当然你也可以把命令提取出来直接nmap

命令：

    nmap -sT -sV -p 21,22,23,80,81,389,443,512,873,1433,1521,2601,2604,3128,3306,3389,4440,6082,6379,7001,8000,8008,8080,8081,8090,8099,8088,8888,9000,9060,9080,9090,9200,11211,27017,28017,50000,50070,U:161 --max-hostgroup 10 --max-parallelism 10 --max-rtt-timeout 1000ms --host-timeout 800s --max-scan-delay 2000ms

详细列表：

    21  ftp  主要看是否支持匿名，也可以跑弱口令
    22  ssh  SSH远程登录协议
    23  telnet   telnet终端仿真协议
    80  web  常见web漏洞以及是否为一些管理后台
    389 LDAP存在匿名访问
    443  openssl  心脏滴血以及一些web漏洞测试
    512 rexec可远程执行shell命令，或实现暴力破解
    873  rsync  主要看是否支持匿名，也可以跑弱口令
    1433 SQl server
    2082/2083 cpanel主机管理系统登陆 （国外用较多）
    2222  DA虚拟主机管理系统登陆 （国外用较多）
    2375 Docker Remote API未授权访问
    2601,2604 zebra路由，默认密码zebra
    3128 squid代理默认端口，如果没设置口令很可能就直接漫游内网了
    3306 MySQL 能够外联数据库
    3312/3311  kangle主机管理系统登陆
    3389 RDP 远程桌面看看能不能弱口令
    4440 rundeck  参考WooYun: 借用新浪某服务成功漫游新浪内网
    6082  varnish  参考WooYun: Varnish HTTP accelerator CLI 未授权访问易导致网站被直接篡改或者作为代理进入内网
    6379  redis 一般无认证，可直接访问
    7001 weblogic的console口
    7778 Kloxo主机控制面板登录
    8000-9090  都是一些常见的web端口，有些运维喜欢把管理后台开在这些非80的端口上
    8000 jdwp java debug模式，可命令执行getshell
    9000 fast-cgi对外可以getshell
    9060 websphere管理端口
    9080
    9200  elasticsearch  参考WooYun: 多玩某服务器ElasticSearch命令执行漏洞
    10000 Virtualmin/Webmin 服务器虚拟主机管理系统
    11211  memcache  未授权访问
    27017  mongodb  未授权访问
    28017  mongodb统计页面
    50000  SAP命令执行
    50030 hadoop hive 10000
    50070  hadoop默认端口
    udp/161 snmp协议 默认community为public
