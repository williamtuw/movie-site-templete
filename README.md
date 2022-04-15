# 大纲
## 基本要素


## 网页部分

    - 内容网址: aiziyou.xx/page/1
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


    - 开发源码
        - debug 带调式代码 带注释
        - release 删除调试代码和注释等
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
    - 部署
        - 注意查看编码是否一致，是否需要指定代码encoding
    - 推广

## 重要部分

    - 推广
        - 爬虫发布
        - QQ wechat社交推广
        - 用户推广
        - 搜索引擎
    - 收费
        - 廉价
        - 方式待定(安全第一)
            - 网卡联盟
            - 微信
            - 支付宝
                - selenium+chrome查询 过程10s 有待优化
            - 赞助


    - 支付成功后回到主页

    - 支付detect
        - selenium 和 chromedriver
        - 无法察觉的爬虫工具 100% 模拟人为操作
    - 安全第一
        - 不透露任何身份信息


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
    -  is_login>_<
    - 注销与admin>_<
        - - 后台登陆和前台同一个sid>_<
    - session的删除观察>_<

    - session add_to admin>_<
    - admin list_display显示>_<
         - 自定义字段>_<
    - stime->create_time>_<
    - DateField 的显示>_<
        - USE_L10N =False
        - DATE_FORMAT = "Y-m-d"
        - DATETIME_FORMAT = "Y-m-d H:i:s"

    - js中的变量@_@ -> >_<
        - 通过html获取>_<
        - js是否可以放在html中进行render!!!

    - render 传入context >_<
    - 一页10个case>_<

    - delopy_css>_<   user_css优化 >_<


    - 将数据导入页面中>_<
    - 导入第一批数据>_<
    - 比对数据和原网站数据>_<
    - 每日更新数据库 >_<以后再说
    - 后台无法改动数据 >_<成功解决
        - 问题来源与python3.7 此版本不稳定
        -  建议目前使用python3.6稳定版本
    - user_info 显示vip_state>_<



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

            - staticcollection
            - setting
                - DEBUG = FASLE ALLOWED_HOST 设置
                - 其他setting设置
            - 参看https://code.ziqiangxuetang.com/django/django-deploy.html
         - 由于ubantu有三个python版本所以要指定用哪一个


- 此项目90% 完成
    - 最后步骤
        - 域名(简单)
        - 服务器
        - 域名备案（主要难题）
    - 项目优化
        - 搭建自己的图片和视频服务器








