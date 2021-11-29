const $=document.querySelector.bind(document);
const $$=document.querySelectorAll.bind(document);

var animalList=$$('.category__item')
var animalActive=$('.category__item.active')
var modal=$('.modal')
animalList[0].classList.add('active');

var animalModalList=$$('.animal-main')
animalModalList[0].classList.add('active');

var closeModalBtns=$$('.close-modal-btn');
closeModalBtns.forEach(function(closeModalBtn)
{
    closeModalBtn.onclick=function()
    {
        modal.classList.remove('active')
        document.body.style.overflowY = 'hidden';
        document.body.style.height = 'auto';
    }
})

animalList.forEach(function(animalItem,index)
{
    const animalModalItem=animalModalList[index];
    animalItem.onclick=function()
    {
        var animalActive=$('.category__item.active')
        var animalModalItemActive=$('.animal-main.active')

        animalActive.classList.remove('active');
        animalModalItemActive.classList.remove('active');

        animalModalItem.classList.add('active');
        this.classList.add('active');

        modal.classList.add('active');

        document.body.style.overflowY = 'hidden';
        document.body.style.height = '100vh';

    }
})

