function addCart(id){
    num = $("#number").val();
    if(!num){
        num = 1;    
    }
    $.post('/shop/addCart', {'id':id, 'num':num, 'csrfmiddlewaretoken': csrftoken}, function(data){
        alert("Bạn đã thêm món này vào giỏ hàng")
    });
}