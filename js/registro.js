const nombre = document.getElementById("nombreregistro")
const email = document.getElementById("emailregistro")
const password = document.getElementById("contrasenaregistro")
const tipoR = document.getElementById("tiporol")
const form = document.getElementById("submit")

form.addEventListener("buttonregistro", e => {
    e.preventDefault();
    if (nombre.value.length < 4) {
        alert("Nombre muy corto");
    }
})