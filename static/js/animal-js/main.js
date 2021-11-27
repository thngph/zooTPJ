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

var categoryWrap=$('.category__wrap')
var categoryMore=$('.category__more')
setTimeout(function()
{ 
    var itemHeight=animalList[0].clientHeight;
    console.log(itemHeight)
    categoryWrap.style.height =itemHeight*2 + 20+'px'

    categoryMore.onclick=function()
    {
        categoryWrap.style.height='auto'
    }
}, 50);




// var categoryWrap =$('.category__wrap');

// var categoryItem=$('.category__item')

// const moreBtn=$('.category__more')

// var modal=$('.modal')
// const animal={
//     currentIndex:1,
//     animalList: [
//         {
//             name:'Nai',
//             desc:'Nai (tên khoa học: Rusa unicolor) hay còn gọi là hươu Sambar theo tiếng Anh (Sambar deer), là một loài thú lớn thuộc họ Hươu, phân bố ở Sri Lanka, Nepan, Ấn Độ, Trung Quốc, các nước Đông Dương. Chúng là loài hươu có kích thước lớn nhất, sống ở vùng nhiệt đới và á nhiệt đới. Nai thích đi ăn ven bờ biển, rất thích bơi lội, đùa giỡn dưới nước. Chúng chạy rất nhanh, hiện đang là loài có nguy cơ tuyệt chủng.',
//             link:'/static/image/image-animal/nai.jpeg'
//         },
//         {
//             name:'Cáo',
//             desc:'Cáo là tên gọi để chỉ một nhóm động vật, gồm có khoảng 27 loài (trong đó 12 loài thuộc về chi Vulpes hay cáo thật sự) với kích thước từ nhỏ đến trung bình, thuộc họ Chó (Canidae), với đặc trưng là có mõm dài, hẹp, đuôi rậm, mắt xếch và tai nhọn. Loài cáo phổ biến và phân bố rộng rãi nhất trong số các loài cáo là cáo đỏ (Vulpes vulpes), mặc dù các loài khác nhau cũng được tìm thấy trên gần như mọi châu lục. Sự hiện diện của các động vật ăn thịt dạng cáo trên toàn cầu đã làm cho hình tượng của chúng xuất hiện trong nhiều câu chuyện của văn hóa dân gian của nhiều dân tộc, bộ lạc hay các nhóm văn hóa khác.',
//             link:'/static/image/image-animal/cao.jpeg'
//         },
//         {
//             name:'Gấu',
//             desc:'Gấu là những loài động vật có vú ăn thịt thuộc Họ Gấu (Ursidae). Chúng được xếp vào phân bộ Dạng chó. Mặc dù chỉ có 8 loài gấu còn sinh tồn, chúng phổ biến rất rộng rãi, xuất hiện ở nhiều môi trường sống khác nhau trên khắp Bắc Bán cầu và một phần ở Nam Bán cầu. Gấu được tìm thấy trên các lục địa Bắc Mỹ, Nam Mỹ, Châu Âu và Châu Á. Trong 8 loài, gấu trắng Bắc Cực là loài lớn nhất (cũng là loài thuộc Bộ Ăn thịt lớn nhất trên cạn), cùng với gấu Kodiak - một phân loài của gấu nâu; còn gấu chó là loài nhỏ nhất.',
//             link:'/static/image/image-animal/gau.jpeg'
//         },
//         {
//             name:'Công',
//             desc: 'Công hay còn gọi cuông, nộc dung, khổng tước[1][2], là tên gọi chung của ba loài chim trong chi Pavo và Afropavo trong phân loài Pavonina của họ Phasianidae, gà lôi và đồng minh của chúng.Hai loài châu Á là công lam hoặc công Ấn Độ có nguồn gốc từ tiểu lục địa Ấn Độ, và công lục ở Đông Nam Á; Một loài châu Phi là công Congo, chỉ có nguồn gốc ở bồn địa Congo . Công trống nổi bật với tiếng kêu ầm ĩ và bộ lông lộng lẫy. Loại thứ hai đặc biệt nổi bật ở châu Á, có "đuôi" đốm mắt hoặc "chuỗi họa tiết" trên những chiếc lông mình, chúng thể hiện như một phần của nghi thức tán tỉnh.',
//             link:'/static/image/image-animal/cong.jpeg'
//         },
//         {
//             name:'Hươu Sao',
//             desc:'Hươu sao (Cervus nippon) còn được gọi là Hươu đốm hoặc Hươu Nhật Bản, là một loài hươu có nguồn gốc ở phần lớn Đông Á và được du nhập đến nhiều nơi khác trên thế giới. Trước đây được tìm thấy từ miền bắc Việt Nam ở miền nam đến vùng Viễn Đông của Nga ở miền bắc, hiện nay nó không phổ biến ở những khu vực này, ngoại trừ Nhật Bản, nơi loài này sinh sôi quá mức. Ở Nhật Bản, tên của nó bắt nguồn từ shika (鹿), từ tiếng Nhật có nghĩa là "con nai". Ở Nhật Bản, loài này được gọi là nihonjika',
//             link:'/static/image/image-animal/huousao.jpg'
//         },
//         {
//             name:'Khỉ Đột',
//             desc:'Khỉ đột (danh pháp khoa học: Gorilla) là một chi linh trưởng thuộc họ người, động vật ăn cỏ sống trong rừng rậm châu Phi, là giống lớn nhất trong bộ linh trưởng còn tồn tại. Khỉ đột được chia thành hai loài (có thể có 4 đến 5 phân loài nữa). DNA của khỉ đột giống của con người 98% -99%. Chúng có họ hàng rất gần gũi với con người chỉ sau 2 loài tinh tinh. Loài linh trưởng này có thân hình đồ sộ. Khỉ đột cao từ 1,7–2 m khi đứng thẳng và nặng từ 180–200 kg. Loài vật này thường đi bằng bốn chân dù chúng có thể đứng bằng hai chân. Gorilla sống ở những khu rừng nhiệt đới và cận nhiệt đới của châu Phi.',
//             link:'/static/image/image-animal/khidot.jpg'
//         },
//         {
//             name:'Rùa',
//             desc:'Bộ Rùa (danh pháp khoa học: Testudines) là những loài bò sát thuộc nhóm chỏm cây của siêu bộ Chelonia (hay Testudinata). Trong tiếng Việt, các loài thuộc bộ rùa được gọi bằng nhiều tên khác nhau như rùa, ba ba, giải, vích, đồi mồi...',
//             link:'/static/image/image-animal/rua.jpeg'
//         },
//         {
//             name:'Vẹt',
//             desc:'Vẹt còn được gọi là chim két hay chim kơ tia là các loài chim gồm khoảng 393 loài trong 92 chi của Bộ Vẹt Psittaciformes được tìm thấy chủ yếu ở các vùng nhiệt đới và cận nhiệt đới. Bộ này được chia thành ba siêu họ: Psittacoidea (vẹt thực sự), Cacatuoidea (vẹt mào) và Strigopoidea (vẹt New Zealand).[3] Một phần ba các loài vẹt đang bị đe dọa bởi sự tuyệt chủng, với nguy cơ tuyệt chủng tổng hợp cao hơn (Sách đỏ IUCN) so với bất kỳ nhóm chim nào khác. Vẹt thường phân bố ở các địa hình nhiệt đới với một số loài sống ở vùng ôn đới ở Nam Bán cầu. Những nơi mà chúng đa dạng nhất là ở Nam Mỹ và Australasia.',
//             link:'/static/image/image-animal/vet.jpeg'
//         },
//         {
//             name:'Nhím',
//             desc:'Nhím lông (porcupine) hay thường được gọi là Nhím là tên gọi cho một số loài động vật thuộc bộ Gặm nhấm (Rodentia). Chúng phân bố trên cả Cựu Thế giới và Tân Thế giới. Tên gọi nhím trong tiếng Việt cũng có thể đề cập đến một số loài trong bộ Nhím gai (Erinaceomorpha) hay họ Tachyglossidae của bộ Monotremata, có nhiều đặc điểm khác hẳn với Họ Nhím lông Cựu Thế giới (Hystricidae) và Họ Nhím lông Tân Thế giới (Erethizontidae), tuy nhiên trong bài này không đề cập tới các thành viên của các bộ này. Sau lợn nước và hải ly, nhím phân bố rộng thứ ba trong bộ Gặm nhấm. Phần lớn những con nhím dài 630–910 mm với chiếc đuôi dài 200–250 mm. Với khối lượng 5,4–16 kg, chúng hay cuộn tròn và chậm chạp. Nhím có nhiều màu sắc như nâu, xám và ít khi trắng.',
//             link:'/static/image/image-animal/nhim.jpeg'
//         },
//         {
//             name:'Voi',
//             desc:'Voi là động vật có vú thuộc họ Elephantidae (cận ngành) và là động vật trên cạn lớn nhất hiện nay. Ba loài hiện được công nhận: voi đồng cỏ châu Phi, voi rừng châu Phi và voi châu Á. Elephantidae là nhánh duy nhất còn sót lại của bộ Proboscidea; thành viên tuyệt chủng bao gồm voi răng mấu. Elephantidae cũng bao gồm một số nhóm hiện đã tuyệt chủng, bao gồm cả voi ma mút và voi ngà thẳng. Voi châu Phi có tai lớn và lưng lõm còn voi châu Á có tai nhỏ và lưng lồi hoặc ngang. Đặc điểm nổi bật của tất cả các loài voi bao gồm thân dài, ngà, vạt tai lớn, chân to và làn da dày nhưng nhạy cảm. Vòi voi được sử dụng để thở, đưa thức ăn và nước vào miệng và cầm nắm đồ vật.',
//             link:'/static/image/image-animal/voi.jpeg'
//         },
//         {
//             name:'Sóc',
//             desc:'Họ Sóc (Sciuridae) là một họ động vật có vú bao gồm các loài gặm nhấm cỡ nhỏ hoặc trung bình. Họ này gồm sóc cây, sóc đất, sóc chuột, macmot (gồm cả macmot châu Mỹ), sóc bay, cầy thảo nguyên, cùng các loài gặm nhấm khác. Sóc là loài bản địa ở Châu Mỹ, lục địa Á-Âu và Châu Phi, và được con người giới thiệu đến Úc.[1] Các loài sóc hóa thạch được biết đến sớm nhất có từ thế Eocen, và trong các họ gặm nhấm còn sinh tồn khác, loài sóc có họ hàng gần gũi nhất với hải ly núi và chuột sóc.',
//             link:'/static/image/image-animal/soc.jpeg'
//         },
//         {
//             name:'Sư tử',
//             desc:'Sư tử (Panthera leo), (tiếng Anh: Lion) là một trong những đại miêu trong họ Mèo và là một loài của chi Báo. Được xếp mức sắp nguy cấp trong thang sách Đỏ IUCN từ năm 1996, các quần thể loài này ở châu Phi đã bị sụt giảm khoảng 43% từ những năm đầu thập niên 1990. Trong văn hóa phương Tây, sư tử được mệnh danh là "chúa tể rừng xanh" (king of the jungle) hay "vua của muôn thú" (king of beasts). Sư tử là loài dị hình giới tính; con đực lớn hơn con cái với phạm vi trọng lượng điển hình từ 150 đến 250 kg (330 đến 550 lb) đối với con đực và 120 đến 182 kg (265 đến 400 lb) đối với con cái, là loài lớn thứ nhì họ Mèo sau hổ Đông Bắc Á. Sư tử đực có thể dễ dàng được nhận ra từ xa bởi bờm của chúng.',
//             link:'/static/image/image-animal/sutu.jpeg'
//         },
//     ],
//     render: function() {
//         const animalListHtmls=this.animalList.map((animalItem,index) => 
//         {
//           return `
//             <div class="col l-3 m-6 category__item" data-index="${index}">
//                 <div href="" class="category__item-wrap">
//                     <div class="category__item-img" style="background-image: url(${animalItem.link});"></div>
//                     <div class="category__item-name">
//                         ${animalItem.name}
//                     </div>
//                 </div>
//             </div>
//           `
//         })
//         // RENDER LẠI MODAL
//         categoryWrap.innerHTML=animalListHtmls.join('')
//         const animalMainHtmls=this.animalList.map((animalItem,index)=>
//         {
//             return `
//             <div class="animal-main ${index === this.currentIndex ? 'active': ''}">
//                 <i class="fas fa-times close-modal-btn"></i>
//                 <div class="animal-main__img-wrap">
//                     <div class="animal-main__img" style="background-image: url(${animalItem.link});"> </div>
//                 </div>
//                 <div class="animal-main__wrap-text">
//                     <div class="animal-main__name">
//                         ${animalItem.name}
//                     </div>
//                     <div class="animal-main__desc">
//                         ${animalItem.desc}
//                     </div>
//                 </div>
//             </div>
//             `
//         })
//         modal.innerHTML=animalMainHtmls.join('')
//     },
//     defineProperties: function(){
//         Object.defineProperty(this,'currentAnimal',{
//             get:function()
//             {
//             return this.animalList[this.currentIndex]
//             }
//         })
//     },
//     // Xử lý event
//     handleEvent:function()
//     {
//         const _this = this;
//         var lineNumber=2;
//         var categoryItem=$('.category__item')
//         var lineNumberMax=Math.ceil(_this.animalList.length/3);
//         var categoryItemHeight=categoryItem.clientHeight+20;
//         categoryWrap.style.height = categoryItemHeight*lineNumber +'px';

//         // Xử lý tắt MODAL
//         modal.onclick=function(e)
//         {
//             const closeBtn=e.target.closest('.close-modal-btn')
//             if(closeBtn)
//             {
//                 modal.classList.remove('active')
//             }
//         }
//         // Xử lý khi chọn con vật
//         categoryWrap.onclick=function(e)
//         {
//             const categoryItemNode=e.target.closest('.category__item')
//             if(categoryItemNode)
//             {
//                 _this.currentIndex=Number(categoryItemNode.dataset.index)
//                 _this.render();
//                 modal.classList.add('active');
//             }
//         }
//         // Chỉnh resize màn hình để responsive
//         window.addEventListener('resize', function(event)
//         {
//             var newWidth = window.innerWidth;
//             var newHeight = window.innerHeight; 
//         });
        
//         window.addEventListener("resize", () => 
//         {
//             var categoryItem=$('.category__item');
//             categoryItemHeight=categoryItem.clientHeight+20;
//             if(lineNumber==lineNumberMax)
//             {
//                 categoryWrap.style.height = 'auto';
//             }
//             else
//             {
//                 categoryWrap.style.height = categoryItemHeight*lineNumber +'px';
//             }
//         });
//         moreBtn.onclick = function()
//         {
//             if(lineNumber<lineNumberMax)
//             {
//                 lineNumber=lineNumberMax;             
//                 categoryWrap.style.height = 'auto';
//             }
//             else
//             {
//                 lineNumber=2;
//                 categoryWrap.style.height = categoryItemHeight*lineNumber +'px';
//             }
//             if(lineNumber==lineNumberMax)
//             {
//                 moreBtn.innerText='THU GỌN'
//             }
//             if(lineNumber==2)
//             {
//                 moreBtn.innerText='XEM THÊM'
//             }
// }
//     },
//     // loadCurrentVideo: function()
//     // {
//     //     videoDisplay.src=this.currentVideo.link;
//     // },
//     start:function()
//     {
//         // Lắng nghe và xử lý sự kiện
//         this.render();
//         this.handleEvent();
//         // Định nghĩa thuộc tính cho Object
//         // this.defineProperties();
//         // Tải thông tin video đầu tiên vào UI
//         // this.loadCurrentAnimal();
//         // Load ra danh sách video
//     }
//   }
// animal.start()


