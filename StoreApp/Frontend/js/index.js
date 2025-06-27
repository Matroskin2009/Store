let button_drop = document.querySelectorAll(".buttonDrop");
let button_close = document.querySelectorAll(".close");
let slider_item_1 = document.getElementById('item1');
let slider_item_2 = document.getElementById('item2');
let slider_item_3 = document.getElementById('item3');
let sliders = [slider_item_1, slider_item_2, slider_item_3];
let current_index = 0;


let button_drop_hide = function () {
    button_drop.forEach((element) => {
        element.nextElementSibling.style.display = "none";
    });
};

function is_press_drop(element) {
    return element.closest(".dropClass") !== null;
}

button_drop.forEach((element) => {
    element.addEventListener("click", (e) => {
        e.stopPropagation();
        button_drop_hide();
        e.currentTarget.nextElementSibling.style.display = "block";
        e.currentTarget.nextElementSibling.style.transform = `translateY(${e.currentTarget.scrollHeight}px)`;
    });
});

document.addEventListener('click', (e) => {
    if (!is_press_drop(e.target)) {
        button_drop_hide();
    }
});

//сreate slider
function show_slide(index) {
    sliders.forEach(element => {
        element.classList.remove('active');
    });

    sliders[index].classList.add('active');
}

function next_slide() {
    current_index = (current_index + 1) % sliders.length;
    show_slide(current_index);
}

show_slide(current_index);

setInterval(next_slide, 3000);


button_close.forEach((element) => {
    element.addEventListener('click', (e) => {
        button_drop_hide()
    })
})