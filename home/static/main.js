// var counter=2;
// setInterval(function() {
//     document.getElementById('radio' +counter).checked = true;
//     counter++;
//     if(counter>3)
//     {
//         counter =1
//     } 
// },10000);


const $=document.querySelector.bind(document);
const $$=document.querySelectorAll.bind(document);
// XỬ LÍ VIDEO
const swiperWrapperVideo=$('.video-animal .swiper-wrapper');
const videoDisplay=$('.video-animal .video__category-place-display')
const videos={
  currentIndex:0,
  videoList: [
    {
      name:'BTS',
      link:'https://www.youtube.com/embed/kFNJTAaAYnU'
    },
    {
      name:'NCT',
      link:'https://www.youtube.com/embed/5FMI-gLo1uc'
    },
    {
      name:'BLACK PINK',
      link:'https://www.youtube.com/embed/7gIx2kEP2_0'
    },
    {
      name:'BIG BANG',
      link:'https://www.youtube.com/embed/4x9C31ECfRM'
    },
    {
      name:'EXO',
      link:'https://www.youtube.com/embed/lHrIF3UVEww'
    },
    {
      name:'SUPER JUNIOR',
      link:'https://www.youtube.com/embed/jc3XI_n_4i8'
    },
    {
      name:'TWICE',
      link:'https://www.youtube.com/embed/y9DxUmPM8pQ'
    },
    {
      name:'MOMOLAND',
      link:'https://www.youtube.com/embed/wo08FFSEqRs'
    },
  ],
  render: function() {
    const htmls=this.videoList.map((video,index) => 
      {
        return `
        <div class="swiper-slide">
            <div class="video__category-option-item ${index===this.currentIndex ? 'active':''}" data-index=${index}>
                ${video.name}
             </div>
        </div>
        `
      })
      swiperWrapperVideo.innerHTML=htmls.join('')
  },
  defineProperties: function(){
    Object.defineProperty(this,'currentVideo',{
      get:function()
      {
        return this.videoList[this.currentIndex]
      }
    })
  },
  handleEvent:function()
  {
    const _this = this;
    swiperWrapperVideo.onclick = function(e)
    {
      var videoNodeActive=$('.video__category-option-item.active');
      const videoNode=e.target.closest('.swiper-slide .video__category-option-item')
      if(videoNode)
      {
        videoNodeActive.classList.remove('active');
        _this.currentIndex=Number(videoNode.dataset.index);
        _this.loadCurrentVideo();
        videoNode.classList.add('active');
        // _this.render();
      }
    }
  },
  loadCurrentVideo: function()
  {
    videoDisplay.src=this.currentVideo.link;
  },
  start:function()
  {
    // Lắng nghe và xử lý sự kiện
    this.handleEvent();
    // Định nghĩa thuộc tính cho Object
    this.defineProperties();
    // Tải thông tin video đầu tiên vào UI
    this.loadCurrentVideo();
    // Load ra danh sách video
    this.render();
  }
}
videos.start()

// FORM ĐĂNG KÝ-ĐĂNG NHẬP
const closeModalBtns=$$('.auth-form__icon-close');
const modal=$('.modal')

const registerAuthForm=$('.auth-form__register')
const loginAuthForm=$('.auth-form__login')

const openRegisterBtns=$$('.btn__open-register-form')
const openLoginBtns=$$('.btn__open-login-form')


for(const closeModalBtn of closeModalBtns) 
{
  closeModalBtn.onclick=function()
  {
    modal.classList.remove('open');
    loginAuthForm.classList.remove('open');
    registerAuthForm.classList.remove('open');
  }
}
for(const openLoginBtn of openLoginBtns) 
{
  openLoginBtn.onclick=function()
  {
    modal.classList.add('open');
    loginAuthForm.classList.add('open');
    registerAuthForm.classList.remove('open');
  }
}
for(const openRegisterBtn of openRegisterBtns) 
{
  openRegisterBtn.onclick=function()
  {
    modal.classList.add('open');
    loginAuthForm.classList.remove('open');
    registerAuthForm.classList.add('open');
  }
}