const $=document.querySelector.bind(document);
const $$=document.querySelectorAll.bind(document);

var donateInputFill=$('.donate__input-fill')
var priceList=$$('.donate__price-item')

for (const priceItem of priceList)
{
    priceItem.onclick = function() {
        donateInputFill.value =priceItem.innerText.replace(/[^0-9]/g,'');
    }
}