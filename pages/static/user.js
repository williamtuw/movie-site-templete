window.onload = function () {
pageTypeInit();
$(".info_edit_tab").click(onTabClick);
$(".cpwd_edit_tab").click(onTabClick);
$(".vip_serve_tab").click(onTabClick);
$(".collection_tab").click(onTabClick);

$("#info_edit_btn").click(onBtnClick);
$("#cpwd_edit_btn").click(onBtnClick);
$("#vip_serve_btn").click(onBtnClick);
}

function pageTypeInit(){
var serve_type = $("#user-sever-tab").text();

if(serve_type == ""){
$("#user-sever-tab").text("info_edit");
serve_type = "info_edit";}

$("."+serve_type).css({"display":"block"});
$("."+serve_type+"_tab").css({"background":"#fff"});

}

function onTabClick(e){
if(e.target.id != $("#user-sever-tab").text()){
$("."+$("#user-sever-tab").text()).css({"display":"none"});
$("."+$("#user-sever-tab").text()+"_tab").css({"background":"#f4f4f4"});
$("#user-sever-tab").text(e.target.id);
$("."+$("#user-sever-tab").text()).css({"display":"block"});
$("."+$("#user-sever-tab").text()+"_tab").css({"background":"#fff"});
}
}
function onBtnClick(e){
if(e.target.id=="vip_serve_btn"){

}
else if(e.target.id=="info_edit_btn"){
$("#info-change-form p").text("");
var uname_re = /^[\u4e00-\u9fa5A-Za-z0-9-_]{1,20}$/;
var email_re =  /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
if(!uname_re.test($("input[name='uname']").val())){
$("p[class='uname-error-message']").text("非法昵称!");
}
else if(!email_re.test($("input[name='user-email']").val())){
$("p[class='user-email-error-message']").text("请输入有效的邮箱地址!");
}
else{
var url = $("#info-change-form").attr("action")
$.ajax({timeout:4000,type:"POST",url:url,data:{uname:$("input[name='uname']").val(),uemail:$("input[name='user-email']").val(),csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
success:function(data){
if(!data.result){
//$("p[class='user-email-error-message']").text("资料修改成功!");
alert("资料修改成功!");
window.location.href = url;
}
else{
$("p[class='user-email-error-message']").text("资料修改失败!用户名已经被使用");
}
}});
}

}
else if(e.target.id=="cpwd_edit_btn"){
$("#cpwd-form p").text("");
var pwd_re = /^[\w\.\*_]{6,16}$/;
if(!pwd_re.test($("input[name='userpwd']").val())){
$("p[class='userpwd-error-message']").text("密码不符合规则!");
}
else if($("input[name='userpwd']").val() != $("input[name='checkpwd']").val()){
$("p[class='checkpwd-error-message']").text("确定新密码错误!");
}
else{
var url = $("#cpwd-form").attr("action")
$.ajax({timeout:4000,type:"POST",url:url,data:{pwd:$("input[name='userpwd']").val(),csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
success:function(data){
if(!data.result){
$("p[class='checkpwd-error-message']").text("密码修改成功");
}
else{
$("p[class='checkpwd-error-message']").text("密码修改失败");
}
}});
}

}
}
//功能测试   页面改动