let buttonDrop = document.querySelectorAll(".buttonDrop");
let buttonClose = document.querySelectorAll(".close");
let sliderItem1 = document.getElementById('item1');
let sliderItem2 = document.getElementById('item2');
let sliderItem3 = document.getElementById('item3');
let sliders = [sliderItem1, sliderItem2, sliderItem3];
let currentIndex = 0;


let buttonDropHide = function () {
    buttonDrop.forEach((element) => {
        element.nextElementSibling.style.display = "none";
    });
};

function isPressDrop(element) {
    return element.closest(".dropClass") !== null;
}

buttonDrop.forEach((element) => {
    element.addEventListener("click", (e) => {
        e.stopPropagation();
        buttonDropHide();
        e.currentTarget.nextElementSibling.style.display = "block";
        e.currentTarget.nextElementSibling.style.transform = `translateY(${e.currentTarget.scrollHeight}px)`;
    });
});

document.addEventListener('click', (e) => {
    if (!isPressDrop(e.target)) {
        buttonDropHide();
    }
});

//сreate slider
function showSlide(index) {
    sliders.forEach(element => {
        element.classList.remove('active');
    });

    sliders[index].classList.add('active');
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % sliders.length;
    showSlide(currentIndex);
}

showSlide(currentIndex);

setInterval(nextSlide, 3000);


buttonClose.forEach((element) => {
    element.addEventListener('click', (e) => {
        buttonDropHide()
    })
})