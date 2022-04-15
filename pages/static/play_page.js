window.onload = function () {
window.onresize = winSizeChanged;
}

function winSizeChanged()
{
//console.log($(window).width(),$(window).height());
if($(window).width() >= 960){
$(".main-content").css("width","960px");
$(".video-title").css({"width":"920px"});
}
else{
$(".main-content").css("width","100%");
$(".video-title").css({"width":String($(".main-content").width()-40)+"px"});
}
}