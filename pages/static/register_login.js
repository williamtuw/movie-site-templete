window.onload = function () {
$("#register-btn").click(registerFormSubmit);
$("#login-btn").click(loginFormSubmit);
pageTypeInit();
}


function login(uname,pwd,csrfmiddlewaretoken,url){
console.log(uname,pwd,csrfmiddlewaretoken);

$.ajax({timeout:4000,type:"POST",url:url,data:{uname:uname,pwd:pwd,csrfmiddlewaretoken:csrfmiddlewaretoken},
success:function(data){
if(!data.result){
//登录成功
if(data.redirect != ""){
window.location.href = data.redirect
}
else{window.history.go(-1);
}

}
else{
//登录失败
$(".login-pwd-error-message").text("用户名或密码错误!");}
}});
}
function loginFormSubmit(){
var url = $("input[name='login-url']").val();
//console.log("登录",$("#page-type-flag").attr("class"));
if($("#page-type-flag").attr("class") == "login"){

$("#register-form p").text("");
var pwd_re = /^[\w\.\*_]{6,16}$/;
var uname_re = /^[\u4e00-\u9fa5A-Za-z0-9-_]{1,20}$/;
if(!pwd_re.test($("input[name='login-pwd']").val())){
$(".login-pwd-error-message").text("密码不符合规则!");
$("input[name='login-pwd']").val("");}
else if(!uname_re.test($("input[name='login-uname']").val())){
$(".login-uname-error-message").text("用户名不符合要求!");
$("input[name='login-uname']").val("");}
else{
login($("input[name='login-uname']").val(),$("input[name='login-pwd']").val(),$("input[name='csrfmiddlewaretoken']").val(),url);
}
}
else{
window.location.href = url;
}
}

function registerFormSubmit(){
var url = $("input[name='register-url']").val();
var login_url = $("input[name='login-url']").val();

//console.log("register",$("#page-type-flag").attr("class"));
if($("#page-type-flag").attr("class") == "register"){
$("#register-form p").text("");
var pwd_re = /^[\w\.\*_]{6,16}$/;
var uname_re = /^[\u4e00-\u9fa5A-Za-z0-9-_]{1,20}$/;
var email_re =  /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
if(!pwd_re.test($("input[name='userpwd']").val())){
$(".pwd-error-message").text("密码不符合规则!");
$("input[name='userpwd']").val("");}
else if($("input[name='userpwd']").val() != $("input[name='checkpwd']").val()){
$(".cpwd-error-message").text("确认密码错误!");
$("input[name='checkpwd']").val("");}
else if(!uname_re.test($("input[name='uname']").val())){
$(".uname-error-message").text("用户名不符合要求!");
$("input[name='uname']").val("");}
//判断邮箱是否有效
else if(!email_re.test($("input[name='uemail']").val()) || ($("input[name='uemail']").val().length>32)){
$(".uemail-error-message").text("请输入有效的邮箱地址!");
$("input[name='umeail']").val("");
}
//判断用户名是否被注册
else{
console.log($("input[name='uname']").val(),$("input[name='userpwd']").val(),$("input[name='uemail']").val(),$("input[name='csrfmiddlewaretoken']").val());
$.ajax({timeout:4000,type:"POST",url:url,data:{uname:$("input[name='uname']").val(),pwd:$("input[name='userpwd']").val(),uemail:$("input[name='uemail']").val(),csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
success:function(data){
if(!data.result){
//注册成功 自动登录 提示消息 转到用户信息界面
login($("input[name='uname']").val(),$("input[name='userpwd']").val(),$("input[name='csrfmiddlewaretoken']").val(),login_url);
alert("注册成功,已自动登录");
}
else{
//注册失败 用户名已经被注册
$(".uname-error-message").text("该用户名已被注册!");}
}});
}
}
else{
window.location.href = url;
}}

function pageTypeInit(){
if($("#page-type-flag").attr("class") == "login"){
$("title").text("登录");
$(".title-line .tit").text("登录")
$(".register-input").css("display","none");
$("#login-btn").css("float","left");
$("#register-btn").css({"float":"right","background":"#ccc"});
}
else{
$("title").text("注册");
$(".title-line .tit").text("注册")
$(".login-input").css("display","none");
$("#register-btn").css("float","left");
$("#login-btn").css({"float":"right","background":"#ccc"});
}}



