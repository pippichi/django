$(function () {
    $("img").onclick(function(){

        console.log("click");
        // $(this).src = '/app/getcode/';
        $(this).attr("src","/app/getcode/?t="+Math.random());
    })
})