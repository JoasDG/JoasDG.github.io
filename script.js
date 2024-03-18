function redirectToPage() {
    window.location.href = "https://joasdg.github.io/vacationgenerator";
}

document.addEventListener("DOMContentLoaded", function() {
    var elementToClick = document.getElementById("projects");
    if (elementToClick) {
        elementToClick.addEventListener("click", redirectToPage);
    }
});
