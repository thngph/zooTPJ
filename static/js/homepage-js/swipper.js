var swiper = new Swiper(".mySwiper", {
  direction: "vertical",
  slidesPerView: 5,
  spaceBetween: 10,
  mousewheel: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  loop:true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});