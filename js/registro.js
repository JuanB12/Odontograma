const nombre = document.getElementById("nombreregistro")
const email = document.getElementById("emailregistro")
const password = document.getElementById("contrasenaregistro")
const tipoR = document.getElementById("tiporol")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e => {
    e.preventDefault();
    let warnings = ""
    if (nombre.value.length< 6) {
        alert("Nombre muy corto");
    }
})