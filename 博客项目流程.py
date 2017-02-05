"""
1, 准备 model
    博客 Model, User
        id
        username
        password
        created_time
    博客 Model， Blog
        id
        title
        content
        created_time
    博客 Model, Comment
        id
        username
        content
        created_time
        blog_id
2, 写出操作场景的文档(你要对这些数据做什么操作, 这是最重要的一步)
    有一个页面用户登录、注册页面
        有登录和注册的功能
    有一个个人用户页面
        显示用户的个人信息
    有一个基础页面，用来给其他页面继承
        如果是登录用户，显示
            首页， 个人主页
        非登录用户，
            首页， 登录注册
        首页重定向博客主页
    有一个主页，可看到所有博客的标题和时间
        主页有链接转到发表博客页面
        主页可以点博客标题进入博客详细页面
    发表博客页面有一个表单可以发表博客
    博客的详细页面，可以看到如下数据
        标题，作者，内容，时间
        所有评论的列表
        有一个输入框，可以输入评论和用户名
        输入之后，页面刷新，可以看到最新评论

3, 根据文档, 写好 CRUD 和其他操作(比如验证用户注册合法性的函数)
    User.new()
    User.validate_login()
    User.validate_register()
    Blog.all()
    Blog.new()
    Comment.all() by blog_id
    Comment.new()
4, 画 html 页面
5, 写路由函数来连接整个功能
6, 美化页面
"""