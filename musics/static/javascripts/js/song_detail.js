function playsong(){
    $.each($('#controllsong'), function () {
        this.play();
    });
    $(".buttonplay").html("<button class='btn' title='Pause' onclick='pausesong();'><i class='glyphicon glyphicon-pause'></button>");
}
function pausesong(){
    $.each($('#controllsong'), function () {
        this.pause();
    });
    $(".buttonplay").html("<button class='btn' title='Play' onclick='playsong();'><i class='glyphicon glyphicon-play'></button>");
}
function repeaton(){
    $.each($('#controllsong'), function () {
        this.loop = true;
    });
    $(".buttonreqeat").html("<button class='btn' title='Repeat off' onclick='repeatoff();'><i style='color: red' class='glyphicon glyphicon-repeat'></button>");
}
function repeatoff(){
    $.each($('#controllsong'), function () {
        this.loop = false;
    });
    $(".buttonreqeat").html("<button class='btn' title='Repeat on' onclick='repeaton();'><i class='glyphicon glyphicon-repeat'></i></button>");
}
function stopsong(){
    $.each($('#controllsong'), function () {
        this.pause();
        this.currentTime = 0;
    });
    $(".buttonplay").html("<button class='btn' title='Play' onclick='playsong();'><i class='glyphicon glyphicon-play'></button>");                                      
};