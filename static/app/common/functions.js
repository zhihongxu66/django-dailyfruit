

function add_cart(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/cart/',
        type:'POST',
        data:{'id':id},
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function(){
            alert('success')
        },
        error:function(){
            alert('error')
        }

    })
}
















