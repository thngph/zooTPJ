// const $=document.querySelector.bind(document);
// const $$=document.querySelectorAll.bind(document);
$(document).ready(function(){
   $('#comment').click(function(){
      var input=$('#input').val();
      $('.box').append(input + '<br>')
      $('#input').val('');
      $('.box-container').slideDown();
   });
   $('#cancel').click(function(){
      $('#input').val('');
   });
   $('delete').click(function(){
      $('.box').text('');
      $('.box-container').slideUp();
   });
});
// var i = 1;
//   $('textarea').keyup(function(e) {

//    if (e.keyCode == 13) {

//     var html = $(this).val();

//     var newHTML = "<div class='list_"+i+"'><p class='html_"+i+"'>"+html+"</p><a href='#' class='remove' number='"+i+"'>Xóa</a><a href='#' class='edit' thutu='"+i+"'>Sửa</a><div class='like'><a href='#' class='wlike'>Like</a></div></div>"

//     $('#list').append(newHTML);

//     $('.list_'+i).css({

//      "min-height": "60px",

//      "background": "#EBEBEB",

//      "line-height": "30px",

//      "padding-left": "50px",

//     })

//     $(this).val("");

//     i++;

//    }

//  });
//  $('.remove').live("click",function() {

//    var c = $(this).attr("number");

//    $('.list_'+c).remove();

// });
// $('.edit').live("click",function() {

//    var d = $(this).attr("thutu");

//    var comment = $(".html_"+d).html();

//    var new_comment = "<input type='text' class='input_"+d+"' value='"+comment+"'/>";

//    $('.html_'+d).html(new_comment);

//    $('.input_'+d).live("keyup",function(e){

//     if(e.keyCode == 13) {

//      var text = $(this).val();

//      $('.html_'+d).html(text);

//     }

//    })

// });
// $('.wlike').live("click",function() {

//    $(this).html("Unlike?");

//    $(this).parent().append("<span>Bạn đã thích nội dung này</span>");

//    $(this).live("click",function() {

//     var b = "<a href='#' class='wlike'>Like</a>";

//     $('span').remove();

//     $(this).parent().append(b);

//     $(this).remove();

//    })

// });