$(function() {
    var comprimido = false;

    $("#btn-comprimir").click(function() {
        if(comprimido) {
            comprimido = false;

            $("#btn-comprimir").html("&#9754;")
            $("iframe").animate({ width:'100%' }, 3000);

            setTimeout(() => {
                $("footer a").css('visibility', 'visible');
                $("footer a").css('visibility', 'visible');
            }, 3000);
        } else {
            comprimido = true;

            $("footer a").css('visibility', 'hidden');
            $("footer a").css('visibility', 'hidden');

            $("#btn-comprimir").html("&#9755;")
            $("iframe").animate({ width:'0%' }, 3000);
        }
    });
});