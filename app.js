document.addEventListener("DOMContentLoaded", () => {
    if (document.body.classList.contains("main-page")) {
        setInterval(createCircle, 3500); // Runs only on breathe-page
    }

    if (document.body.classList.contains("breathe-page")) {
        setInterval(updateCountdown, 1000); // Runs only on main-page
    }
});

function createCircle() {
    const circle = document.createElement("div");
    circle.classList.add("circle");

    const size = Math.random() * 200 + 20; // Circle size between 20 and 220px
    const posX = Math.random() * (window.innerWidth - size);
    const posY = Math.random() * (window.innerHeight - size);

    const colors = ["#d6cafc", "#8e7bca", "#bcabef"];
    const color = colors[Math.floor(Math.random() * colors.length)];

    circle.style.width = `${size}px`;
    circle.style.height = `${size}px`;
    circle.style.left = `${posX}px`;
    circle.style.top = `${posY}px`;
    circle.style.backgroundColor = color;

    document.body.appendChild(circle);

    setTimeout(() => {
        circle.remove();
    }, 3000);
}

const startingMinutes = 10;
let time = startingMinutes * 60;

function updateCountdown() {
    const countdownElement = document.getElementById("countdown");
    if (!countdownElement) return; // Prevent errors if element is missing

    const minutes = Math.floor(time / 60);
    let seconds = time % 60;
    countdownElement.innerHTML = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    time--;
}