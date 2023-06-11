let htmlTag = document.querySelector("html")
let themeSwitch = document.getElementById("themeSwitch")
let savedTheme = localStorage.getItem("theme")

// Überprüfe den gespeicherten Theme-Status und setze das Theme und den Switch
// entsptrechend
if (savedTheme === "dark") {
    themeSwitch.checked = true
    htmlTag.setAttribute("data-bs-theme", "dark")
} else {
    themeSwitch.checked = false
    htmlTag.setAttribute("data-bs-theme", "light")
}

// Füge den Change-Eventhandler zum ThemeSwitch hinzu
themeSwitch.addEventListener("change", function () {
    let newTheme = themeSwitch.checked ? "dark" : "light"

    localStorage.setItem("theme", newTheme)

    htmlTag.setAttribute("data-bs-theme", newTheme)
})
