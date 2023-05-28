function saveUser() {
    let endPoint = "/saveUser"
    const textEmail = document.getElementById("userEmail")
    const textPass = document.getElementById("userPass")

    axios.post(endPoint, {
        'Nombre': textEmail.value,
        'Pass': textPass.value
    })
        .then(function (response) {
            alert(response);
        })
        .cath(function (error) {
            console.log(error);
        })
}