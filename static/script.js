// Apply saved theme when page loads
window.onload = function () {

    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }

}

// Toggle Dark Mode
function toggleDarkMode() {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    }
    else {
        localStorage.setItem("theme", "light");
    }

}