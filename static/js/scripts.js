$(function(){
    $('.projects .content-project').on('click', function(){
        $('#modal').modal;
        var ruta_imagen = ($(this).find('img').attr('src'));
        console.log(ruta_imagen)
        $('#imagen-modal').attr('src',ruta_imagen);
    });
    $('#modal').on('click', function(){
        $('#modal').modal('hide');
    })
    })