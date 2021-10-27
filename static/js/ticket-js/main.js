const $=document.querySelector.bind(document);
const $$=document.querySelectorAll.bind(document);

var kidQuantity=$('.ticket__form-quantity-input-kid');
var adultQuantity=$('.ticket__form-quantity-input-adult');
var date=$('.ticket__form-date-input');
var kidQuantityTicket=$('.ticket-total-number-kid');
var adultQuantityTicket=$('.ticket-total-number-adult');
var dateTicket=$('.ticket-total__part-date-desc')
var totalPriceTicket=$('.total__price')
var price=0;
const monthNames = ["Tháng 1","Tháng 2","Tháng 3","Tháng 4","Tháng 5","Tháng 6","Tháng 7","Tháng 8","Tháng 9","Tháng 10","Tháng 11","Tháng 12",];
const daysOfWeekNames = ["Chủ nhật","Thứ hai", "Thứ ba", "Thứ tư","Thứ năm","Thứ sáu","Thứ bảy" ];
kidQuantity.oninput = function()
{
    kidQuantityTicket.innerText = kidQuantity.value + ' trẻ em'
    price=adultQuantity.value *10 + kidQuantity.value *5;
    totalPriceTicket.innerText='Tổng tiền: ' +price + '$'
}
adultQuantity.oninput = function()
{
    adultQuantityTicket.innerText = adultQuantity.value + ' người lớn'
    price=adultQuantity.value *10 + kidQuantity.value *5;
    totalPriceTicket.innerText='Tổng tiền: ' +price + '$'
}
date.oninput=function()
{
    datetest=new Date(date.value)
    dateTicket.innerText=daysOfWeekNames[datetest.getDay()] + ", "+datetest.getDate()+" "+ monthNames[datetest.getMonth()]+" "+ datetest.getFullYear()
}

// SET MIN CHO LÀ NGÀY HÔM NAY
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
var yyyy = today.getFullYear();
if(dd<10){
  dd='0'+dd
} 
if(mm<10){
  mm='0'+mm
} 
today = yyyy+'-'+mm+'-'+dd;
date.setAttribute("min", today);