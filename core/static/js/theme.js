document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    const currentTheme = localStorage.getItem("theme") || "light";

    // Устанавливаем начальную тему
    document.documentElement.setAttribute("data-theme", currentTheme);
    themeToggle.innerHTML = currentTheme === "dark" ? "☀️" : "🌙";

    // Обработчик переключения темы
    themeToggle.addEventListener("click", () => {
        const newTheme = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        themeToggle.innerHTML = newTheme === "dark" ? "☀️" : "🌙";
    });
});