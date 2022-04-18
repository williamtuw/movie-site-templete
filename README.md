# This is a movie-size templete base on Django-py
## 基本要素


## 网页部分

    - 内容网址:xxx.xx/page/1
    - 登录/注册页面
    - 播放界面
    - 用户界面
        - 用户基本信息
        - 收藏
        - 退出登录
        - 历史订单
        - 会员服务
        - 修改密码
        - 编辑资料



## 功能部分
    - 搜索
    - 标签分类 添加标签 相关视频
    - 收藏
    - 忘记密码 记住我
    - 密码保存 autocomplete
    - 我的订单

# 数据库部分
    - 将第一批数据导入数据库
         - 写一个程序每天定时更新数据库
         -

## steps
    - html css js
    - 实现功能部分
    -  页面优化
        - js动态效果
        - 根据窗口改变布局 部件大小 等
        - 移动设备优化 根据媒体实际情况优化 @media
        - 根据窗口大小进行初始化 important!

    - 代码优化
        - 改掉hardcode 习惯
        - 代码简化
        - 结构化
            - 考虑register_login.html 改用{% if is_login %}模式@_@ 如需标准化请进行此项
            - onsubmit form type return to submit
        - 可移植  可改动性


    - 网站安全 建设
        - 表单数据验证是否合法
            - 攻击者可以伪装成客户发送非法表单数据
        - 防爬虫
            - 验证码
            - ip 检测封禁
        - 身份伪造
            - 客户端un cookie 和 session uname 比较 以免伪造session
            - 给客户端设置cookie即使sid存在也要判断cookie
        - 恶意破坏
            - csrf 攻击
            - 利用sql 类型的攻击

        - 防盗资源
            - referrer 判断
            - 防止盗链
    - 测试功能 debug 日志
    
    - 推广

## 重要部分

    - 推广
        - 爬虫发布
        - QQ wechat社交推广
        - 用户推广
        - 搜索引擎
    - 收费
    
  
            - 网卡联盟
            - 微信
            - 支付宝
                - selenium+chrome查询 过程10s 有待优化
            - 赞助


# 网页结构
    - / 主页
    - /page/xxx 分页
    - /search post
    - post 转页
    - user/XXXX get 各个user tab
    - user/XXXX post 各个user tab具体业务实现
    - 播放页 x.html

# 网站管理 admin.site
    - admin
        - 网站日志记录，按时观察记录，避免成为傻子站长
        - register
        - display
        - 自定义显示字段
        - 后台管理的二次开发 后台管理自定义
            - 数据库页面跳转
        - 参考
            - https://www.cnblogs.com/wumingxiaoyao/p/6928297.html
            - django 官网

# problems
  

    - 先部署再说
        - 基础步骤
            - 买域名
            - 服务器
            - 域名解析
            - 域名绑定服务器
            - 备案
        - 安装python3.6 pip 并设置为系统默认
        - pip更新
        - 安装django 注意版本
        - 传输文件

        - 部署前准备

          
            - 参看https://code.ziqiangxuetang.com/django/django-deploy.html
       


    - 最后步骤
        - 域名(简单)
        - 服务器
        - 域名备案
  


