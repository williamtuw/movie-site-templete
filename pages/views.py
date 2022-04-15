from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# from django.core.pathresolvers import reverse
from pages.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.sessions.models import Session
import json, time
from django.urls import reverse

# Create your views here.

def getDelopyPage(request):
    # context : keywords description title delopy_css_url logo_img_url home_url delopy_url statement
    context = {"keywords": "爱自由,电影吧,aiziyou",
               "description": "爱自由-电影吧(aiziyou.co)本站包含全网电影，给你最好的体验",
               "title": "爱自由-电影吧",
               "delopy_css_url": "/static/delopy.css",
               "logo_img_url": "/static/logo.png",
               "home_url": "/",
               "delopy_url": "aiziyou.co",
               "statement": "爱自由-电影吧(aiziyou.co)本站包含全网电影，给你最好的体验"
               }
    return render(request, 'delopy.html', context)


def home(request):
    return getPage(request, 1)


def page(request, page_id):
    return getPage(request, int(page_id))


def getHeaderContext(request):
    # header context :delopy_url is_vip logo_img_url  user_type_img user_type vip_path_url vip_path uname is_login menu_img_url search_img_url

    is_login = False
    user_type = "uvip"
    user_type_img = "/static/uvip.png"
    vip_path = "开通"
    is_vip = False
    uname = request.session.get("uname", None)
    if uname:
        user_ = User.objects.get(uname=uname)
        is_login = True
        if user_.vip_expiry + 15e8 > time.time():
            user_type, user_type_img = "vip", "/static/vip.png"
            vip_path = "续费"
            is_vip = True

    return {"delopy_url": reverse("delopy"), "logo_img_url": "/static/logo.png",
            "vip_path_url": reverse("user", args=["vip_serve"]),
            "menu_img_url": "/static/menu.png", "search_img_url": "/static/search.png",
            "is_login": is_login, "user_type": user_type,"is_vip":is_vip,
            "user_type_img": user_type_img, "vip_path": vip_path, "uname": uname
            }


def getFooterContext(request):
    # footer context :delopy_url email top_img_url aiziyou_url
    return {"delopy_url": reverse("delopy"), "email": "1786406222@qq.com", "top_img_url": "/static/top.png",
            "aiziyou_url": "aiziyou.top"}


def getPage(request, num: int):
    # context :title key_words description jquery_js_url header_css_url page_css_url canonical
    # footer_css_url page_js_url page_count search_rst
    # delopy_url case.link case.declaration case.img case.post case_list
    # home_page prev_page cur_page next_page end_page

    # 获取keyword如果没有则不筛选
    keyword = request.GET.get("kw") or ""
    params = keyword and ("?kw=" + keyword)
    # 判断是不是post 页面跳转
    if request.method == "POST":
        return HttpResponseRedirect(reverse("page", args=[request.POST.get("page")]) + params)
    videos_filter_rst = Video.objects.filter(title__icontains=keyword)

    # 从数据库获取数据

    video_count = videos_filter_rst.count()
    page_count = (video_count - 1) // 12 + 1
    if num > page_count:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    videos = videos_filter_rst[
             (0 if (video_count - 12 * num) < 0 else (video_count - 12 * num)):video_count - 12 * (num - 1)]

    search_rst = keyword and "搜索结果: 共搜索到%d篇关于 <%s> 的内容" % (video_count, keyword)

    home_page = reverse("page", args=[1]) + params
    prev_page = reverse("page", args=[num - 1]) + params
    cur_page = num
    next_page = reverse("page", args=[num + 1]) + params
    end_page = reverse("page", args=[page_count]) + params

    case_list = [{"link": reverse("play_html", args=[case.id]), "img": case.img_link,
                  "declaration": case.title, "post": case.post_time} for case in videos]
    context = {"title": "爱自由-电影吧-第" + str(num) + "页",
               "key_words": "爱自由-电影吧,aiziyou",
               "description": "爱自由-电影吧(aiziyou.co)本站包含全网电影，给你最好的体验",
               "jquery_js_url": "/static/jquery-3.3.1.min.js",
               "header_css_url": "/static/header.css",
               "page_css_url": "/static/page.css",
               "canonical": reverse("page", args=[num]),
               "footer_css_url": "/static/footer.css",
               "page_js_url": "/static/page.js",
               "delopy_url": "/delopy",
               "case_list": case_list,
               "email": "1786406222@qq.com",
               "top_img_url": "/static/top.png",
               "search_rst": search_rst,
               "page_count": page_count,
               "home_page": home_page, "prev_page": prev_page, "cur_page": cur_page, "next_page": next_page,
               "end_page": end_page
               }
    # 获取header footer context
    context.update(getHeaderContext(request))
    context.update(getFooterContext(request))

    return render(request, 'page.html', context)


def getPlayHtml(request, video_id: str):
    # context: title jquery_js_url header_css_url play_page_css_url footer_css_url play_page_js_url delopy_url
    # video.title video.class video.post video.src

    # 从数据库获取数据
    video_ = Video.objects.get(id=video_id)
    if not video_:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    try:
        user_ = User.objects.get(uname=request.session.get("uname",None))
    except (ObjectDoesNotExist,Exception):
        user_ = None


  #  video_url = (video_.video_url+"66666" if (user_.vip_expiry + 15e8)>time.time() else video_.video_url + "180") if user_ else video_.video_url + "60"
    video_url = video_.video_url

    video = {"title": video_.title, "class": "未分类", "post": video_.post_time, "src": video_url}

    context = {"title": video["title"],
               "jquery_js_url": "/static/jquery-3.3.1.min.js",
               "header_css_url": "/static/header.css",
               "play_page_css_url": "/static/play_page.css",
               "footer_css_url": "/static/footer.css",
               "play_page_js_url": "/static/play_page.js",
               "delopy_url": reverse("delopy"),
               "video": video,
               }
    # 获取header footer context
    context.update(getHeaderContext(request))
    context.update(getFooterContext(request))

    return render(request, 'play_page.html', context)


def getRgtLoginContext(title, page_type):
    # context :title jquery_js_url header_css_url register_login_css_url footer_css_url register_login_js_url page.type
    context = {"title": title, "jquery_js_url": "/static/jquery-3.3.1.min.js",
               "header_css_url": "/static/header.css", "register_login_css_url": "/static/register_login.css",
               "footer_css_url": "/static/footer.css", "register_login_js_url": "/static/register_login.js",
               "page": {"type": page_type}}
    return context


def login(request):
    if request.method == "GET":
        # 设置session login_register_times 用来确定是转到主页还是转到原网页
        login_register_times = request.session.get("login_register_times",None)
        request.session["login_register_times"] = (login_register_times+ 1) if login_register_times else 1
        # 获取login_html context
        context = getRgtLoginContext("爱自由-电影吧-登录", "login")
        # 获取header footer context
        context.update(getHeaderContext(request))
        context.update(getFooterContext(request))

        return render(request, "register_login.html", context)
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user_ = User.objects.filter(uname=uname, pwd=pwd).first()

        if user_ is not None:
            # 判断这个账号是否有session对应 如果有便删除
            if user_.is_login:
                user_.is_login = False
                for s in Session.objects.all():
                    if s.get_decoded().get("uname") == user_.uname:
                        s.delete()
                        break
            # 清除过期session
            request.session.clear_expired()
            request.session['uname'] = user_.uname
            user_.is_login = True
            user_.save()
            redirect = reverse("home") if request.session.get("login_register_times",None) > 1 else ""
            del request.session["login_register_times"]
            return HttpResponse(json.dumps({"result": 0, "redirect": redirect}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"result": -1}), content_type="application/json")


def register(request):
    if request.method == "GET":
        # 设置session login_register_times 用来确定是转到主页还是转到原网页
        login_register_times = request.session.get("login_register_times", None)
        request.session["login_register_times"] = (login_register_times + 1) if login_register_times else 1

        # 获取register_html context
        context = getRgtLoginContext("爱自由-电影吧-注册", "register")
        # 获取header footer context
        context.update(getHeaderContext(request))
        context.update(getFooterContext(request))

        return render(request, "register_login.html", context)

    elif request.method == "POST":
        try:
            User.objects.get_or_create(uname=request.POST.get("uname"), pwd=request.POST.get("pwd"),
                                       email=request.POST.get("uemail"), vip_expiry=time.time() - 15e8)
        except:
            return HttpResponse(json.dumps({"result": 1}), content_type="application/json")
        else:

            return HttpResponse(json.dumps({"result": 0}), content_type="application/json")


def user(request, tab):
    uname = request.session.get("uname", None)
    if uname is None:
        return HttpResponseRedirect(reverse("login"))

    user_serve_list = ["info_edit", "vip_serve", "cpwd_edit", "collection", ""]
    if tab not in user_serve_list:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == "GET":
        # context :title jquery_js_url header_css_url  user_css_url footer_css_url user_js_url user_type_img vip_state
        # user.email user.id user.create_time user.serve_type user.name

        user_ = User.objects.get(uname=uname)

        user_info = {"email": user_.email, "id": user_.id, "create_time": user_.create_time, "serve_type": tab,
                     "name": user_.uname}
        vip_state = "您目前不享有vip权益哦!" if (user_.vip_expiry + 15e8) < time.time() else "您的vip将在 " + time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(user_.vip_expiry + 15e8)) + " 到期"

        context = {"title": "爱自由-电影吧-用户|" + tab, "jquery_js_url": "/static/jquery-3.3.1.min.js",
                   "header_css_url": "/static/header.css", "user_css_url": "/static/user.css",
                   "footer_css_url": "/static/footer.css", "user_js_url": "/static/user.js",
                   "user": user_info, "vip_state": vip_state}

        # 获取header footer context
        context.update(getHeaderContext(request))
        context.update(getFooterContext(request))

        return render(request, 'user.html', context)
    elif request.method == "POST":
        user_ = User.objects.filter(uname=uname)
        if tab == "vip_serve":
                vip_serve_type = request.POST.get("vip-serve-type",None)
                pay_type = request.POST.get("pay-type",None)
                print("vip_serve_type",vip_serve_type,"pay_type",pay_type)
                return HttpResponseRedirect(reverse("user",args=["vip_serve"]))
        elif tab == "collection":
            pass
        elif tab == "info_edit":
            try:
                user_.update(uname=request.POST.get("uname"), email=request.POST.get("uemail"))
                request.session["uname"] = request.POST.get("uname")
            except:
                return HttpResponse(json.dumps({"result": -1}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"result": 0}), content_type="application/json")
        elif tab == "cpwd_edit":
            try:
                user_.update(pwd=request.POST.get("pwd"))
            except:
                return HttpResponse(json.dumps({"result": -1}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"result": 0}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"result": -1}), content_type="application/json")
    else :
        return HttpResponseNotFound('<h1>Page not found</h1>')

def logout(request):
    uname = request.session.get("uname", None)
    if uname is not None:
        User.objects.filter(uname=uname).update(is_login=False)
        del request.session["uname"]
    return HttpResponseRedirect(reverse("login"))
