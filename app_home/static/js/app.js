const toggle = document.getElementsByClassName("toggle")[0];
const menuDashboard = document.getElementsByClassName("menu-dashboard")[0];
const iconoMenu = toggle.getElementsByClassName("bx bx-menu")[0];
const enlacesMenu = document.getElementsByClassName("enlace")[0];

toggle.addEventListener("click", () => {
    menuDashboard.classList.toggle("open")

    if (iconoMenu.classList.contains("bx-menu")) {
        iconoMenu.classList.replace("bx-menu", "bx-x")
    } else {
        iconoMenu.classList.replace("bx-x", "bx-menu")
    }
})

enlacesMenu.forEach(enlace => {
    enlace.addEventListener("click", () => {
        menuDashboard.classList.add("open")
        iconoMenu.classList.replace("bx-menu", "bx-x")
    })
})