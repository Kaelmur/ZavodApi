let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let formData = {
        'username': form.username.value,
        'password': form.password.value,
    }

    fetch('http://127.0.0.1:8000/api/token/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log("DATA:", data.access)
            if(data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'http://localhost:63342/FrontEnd/prices-list.html?_ijt=qpkcc16sc8lg5f5hiiqaktbjth&_ij_reload=RELOAD_ON_SAVE'
            } else {
                alert("Username Or password is invalid.")
            }
        })
})