const $=document.querySelector.bind(document);
const $$=document.querySelectorAll.bind(document);

const categoryWrap =$('.category__wrap');

var categoryItem=$('.category__item')

const moreBtn=$('.category__more')

const categoryItems=$$('.category__item')

const animal={
    currentIndex:0,
    animalList: [
        {
            name:'Nai',
            link:'./assets/animal-assets/image/nai.jpeg'
        },
        {
            name:'Cáo',
            link:'./assets/animal-assets/image/cao.jpeg'
        },
        {
            name:'Gấu',
            link:'./assets/animal-assets/image/gau.jpeg'
        },
        {
            name:'Công',
            link:'./assets/animal-assets/image/cong.jpeg'
        },
        {
            name:'Hươu Sao',
            link:'./assets/animal-assets/image/huousao.jpg'
        },
        {
            name:'Khỉ Đột',
            link:'./assets/animal-assets/image/khidot.jpg'
        },
        {
            name:'Rùa',
            link:'./assets/animal-assets/image/rua.jpeg'
        },
        {
            name:'Vẹt',
            link:'./assets/animal-assets/image/vet.jpeg'
        },
        {
            name:'Nhím',
            link:'./assets/animal-assets/image/nhim.jpeg'
        },
        {
            name:'Voi',
            link:'./assets/animal-assets/image/voi.jpeg'
        },
        {
            name:'Sóc',
            link:'./assets/animal-assets/image/soc.jpeg'
        },
        {
            name:'Sư tử',
            link:'./assets/animal-assets/image/sutu.jpeg'
        },
    ],
    render: function() {
        const htmls=this.animalList.map((animalItem,index) => 
        {
          return `
            <div class="col l-3 m-6 category__item">
                <a href="" class="category__item-wrap">
                    <div class="category__item-img" style="background-image: url(${animalItem.link});"></div>
                    <div class="category__item-name">
                        ${animalItem.name}
                    </div>
                </a>
            </div>
          `
        })
        categoryWrap.innerHTML=htmls.join('')
    },
    // defineProperties: function(){
    //   Object.defineProperty(this,'currentVideo',{
    //     get:function()
    //     {
    //       return this.videoList[this.currentIndex]
    //     }
    //   })
    // },
    handleEvent:function()
    {
        const _this = this;
        var lineNumber=2;
        var categoryItem=$('.category__item')
        var lineNumberMax=Math.ceil(_this.animalList.length/3);
        var categoryItemHeight=categoryItem.clientHeight+20;
        categoryWrap.style.height = categoryItemHeight*lineNumber +'px';

        window.addEventListener('resize', function(event)
        {
            var newWidth = window.innerWidth;
            var newHeight = window.innerHeight; 
        });
        
        window.addEventListener("resize", () => 
        {
            var categoryItem=$('.category__item');
            categoryItemHeight=categoryItem.clientHeight+20;
            if(lineNumber==lineNumberMax)
            {
                categoryWrap.style.height = 'auto';
            }
            else
            {
                categoryWrap.style.height = categoryItemHeight*lineNumber +'px';
            }
        });
        
        moreBtn.onclick = function()
        {
            if(lineNumber<lineNumberMax)
            {
                lineNumber=lineNumberMax;             
                categoryWrap.style.height = 'auto';
            }
            else
            {
                lineNumber=2;
                categoryWrap.style.height = categoryItemHeight*lineNumber +'px';
            }
            if(lineNumber==lineNumberMax)
            {
                moreBtn.innerText='THU GỌN'
            }
            if(lineNumber==2)
            {
                moreBtn.innerText='XEM THÊM'
            }
}
    },
    // loadCurrentVideo: function()
    // {
    //     videoDisplay.src=this.currentVideo.link;
    // },
    start:function()
    {
        // Lắng nghe và xử lý sự kiện
        this.render();
        this.handleEvent();
        // Định nghĩa thuộc tính cho Object
        // this.defineProperties();
        // Tải thông tin video đầu tiên vào UI
        // this.loadCurrentAnimal();
        // Load ra danh sách video
    }
  }
animal.start()

