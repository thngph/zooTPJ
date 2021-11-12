var counter = 2;
setInterval(function () {
  document.getElementById("radio" + counter).checked = true;
  counter++;
  if (counter > 3) {
    counter = 1;
  }
}, 10000);

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);
// XỬ LÍ VIDEO
const swiperWrapperVideo = $(".video-animal .swiper-wrapper");
const videoDisplay = $(".video-animal .video__category-place-display");
const videos = {
  currentIndex: 0,
  videoList: [
    {
      name: "Khỉ",
      link: "https://www.youtube.com/embed/LHpzjBydyGA",
    },
    {
      name: "Ngựa vằn",
      link: "https://www.youtube.com/embed/pI4KUIGrj9Y",
    },
    {
      name: "Công",
      link: "https://www.youtube.com/embed/fCx7VMnU6VY",
    },
    {
      name: "Gấu",
      link: "https://www.youtube.com/embed/q0BYoCNDK8w",
    },
    {
      name: "Hươu cao cổ",
      link: "https://www.youtube.com/embed/nItG4ExlTaY",
    },
    {
      name: "Hồng hạc",
      link: "https://www.youtube.com/embed/0YM9Hz0q4Fk",
    },
    {
      name: "Sóc",
      link: "https://www.youtube.com/embed/HEj-L6wmngA",
    },
    {
      name: "Nai",
      link: "hhttps://www.youtube.com/embed/xAxay2axNR8",
    },
    {
      name: "Rùa",
      link: "https://www.youtube.com/embed/d4A0DwrVj6E",
    },
    {
      name: "Chim cánh cụt",
      link: "https://www.youtube.com/embed/rBqYxevAbWM",
    },
  ],
  render: function () {
    const htmls = this.videoList.map((video, index) => {
      return `
          <div class="swiper-slide">
              <div class="video__category-option-item ${
                index === this.currentIndex ? "active" : ""
              }" data-index=${index}>
                  ${video.name}
              </div>
          </div>
          `;
    });
    swiperWrapperVideo.innerHTML = htmls.join("");
  },
  defineProperties: function () {
    Object.defineProperty(this, "currentVideo", {
      get: function () {
        return this.videoList[this.currentIndex];
      },
    });
  },
  handleEvent: function () {
    const _this = this;
    swiperWrapperVideo.onclick = function (e) {
      var videoNodeActive = $(".video__category-option-item.active");
      const videoNode = e.target.closest(
        ".swiper-slide .video__category-option-item"
      );
      if (videoNode) {
        videoNodeActive.classList.remove("active");
        _this.currentIndex = Number(videoNode.dataset.index);
        _this.loadCurrentVideo();
        videoNode.classList.add("active");
        // _this.render();
      }
    };
  },
  loadCurrentVideo: function () {
    videoDisplay.src = this.currentVideo.link;
  },
  start: function () {
    // Lắng nghe và xử lý sự kiện
    this.handleEvent();
    // Định nghĩa thuộc tính cho Object
    this.defineProperties();
    // Tải thông tin video đầu tiên vào UI
    this.loadCurrentVideo();
    // Load ra danh sách video
    this.render();
  },
};
videos.start();

// FORM ĐĂNG KÝ-ĐĂNG NHẬP
const closeModalBtns = $$(".auth-form__icon-close");
const modal = $(".modal");
const authForms = $$(".auth-form");
const userForm = $(".user");
const registerAuthForm = $(".auth-form__register");
const loginAuthForm = $(".auth-form__login");
const closeUserFormBtn = $(".user-close-btn");
const openRegisterBtns = $$(".btn__open-register-form");
const openLoginBtns = $$(".btn__open-login-form");

const openUserInfo = $(".header__user-subnav-info");

function closeModal() {
  modal.classList.remove("open");
  loginAuthForm.classList.remove("open");
  registerAuthForm.classList.remove("open");
  userForm.classList.remove("open");
}

for (const closeModalBtn of closeModalBtns) {
  closeModalBtn.onclick = function () {
      closeModal();
  };
}
// Mở form đăng nhập
openLoginBtns.forEach(function (openLoginBtn) {
  openLoginBtn.onclick = function () {
    modal.classList.add("open");
    loginAuthForm.classList.add("open");
    registerAuthForm.classList.remove("open");
  };
})
// Mở form đăng kí
openRegisterBtns.forEach(function (openRegisterBtn) {
  openRegisterBtn.onclick = function () 
  {
    modal.classList.add("open");
    loginAuthForm.classList.remove("open");
    registerAuthForm.classList.add("open");
  };
})

modal.addEventListener("click", closeModal);

authForms.forEach(function(authForm) 
{
    authForm.onclick = function(event)
    {
      event.stopPropagation()
    }
}
)
// TAB USER FORM
var openUserForm=function()
{
  modal.classList.add("open");
  userForm.classList.add("open");
}
if(openUserInfo)
{
    openUserInfo.addEventListener("click", openUserForm);
}

const userOptionItems = $$(".user__option-item");
const userTabWrapItems = $$(".user__tab-wrap-item");

userOptionItems.forEach(function (userOptionItem, index) {
  const userTabWrapItem = userTabWrapItems[index];
  userOptionItem.onclick = function () {
    var userTabWrapItemActive = document.querySelector(
      ".user__tab-wrap-item.active"
    );
    var userOptionItemActive = document.querySelector(
      ".user__option-item.active"
    );

    userTabWrapItemActive.classList.remove("active");
    userOptionItemActive.classList.remove("active");

    userTabWrapItem.classList.add("active");
    this.classList.add("active");
  };
});
// Đóng form user
if(closeUserFormBtn)
{
  closeUserFormBtn.addEventListener("click", closeModal);
}

// Chống nổi bọt
if(userForm)
{
  userForm.addEventListener("click", function (event) {
    event.stopPropagation();
  });
}

