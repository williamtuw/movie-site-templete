window.onload = function () {
window.onresize = winSizeChanged;

}


function winSizeChanged()
{
//console.log($(window).width(),$(window).height());
if($(window).width() >= 1280){
$(".main-content").css("width","1280px");
$(".nav-pagination").css({"width":"1260px"});
}
else if($(window).width() >= 960){
$(".main-content").css("width","960px");
$(".nav-pagination").css({"width":"940px"});
}
else{
$(".main-content").css("width","640px");
$(".nav-pagination").css({"width":"620px"});
}
}