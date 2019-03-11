function stopsongdetail(){                                    
    $.each($('.playsongdetail'), function () {
        this.pause();
        this.currentTime = 0;
    });
};