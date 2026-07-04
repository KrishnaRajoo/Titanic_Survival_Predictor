document.addEventListener("DOMContentLoaded", function () {

    const card = document.querySelector(".card");

    if (card) {
        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 100);
    }

    const form = document.querySelector("form");
    const button = document.querySelector(".btn");

    if (form && button) {
        form.addEventListener("submit", function () {
            button.innerHTML = "Predicting...";
            button.disabled = true;
        });
    }

    const result = document.querySelector(".result");

    if (result) {
        result.style.opacity = "0";

        setTimeout(() => {
            result.style.transition = "0.5s";
            result.style.opacity = "1";
        }, 200);
    }

});