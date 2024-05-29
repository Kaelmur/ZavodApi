let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'http://localhost:63342/FrontEnd/login.html?_ijt=hcedr16umiuuc1sec0qm6gom0t&_ij_reload=RELOAD_ON_SAVE'
})

let pricesUrl = 'http://127.0.0.1:8000/prices/'

document.getElementById('add-price-form').addEventListener('submit', function(e) {
    e.preventDefault();

    let fraction = document.getElementById('fraction').value;
    let price = document.getElementById('price').value;
    let token = localStorage.getItem('token')

    let data = {
        fraction: fraction,
        price: price
    };

    fetch(`${pricesUrl}add/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            getPrices()
            alert(data.message);
        } else if (data.detail) {
            alert('Error: ' + data.detail);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to add price');
    });
});

let getPrices = () => {
    let token = localStorage.getItem('token')
    fetch(pricesUrl, {
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        }
    })
        .then(response => response.json())
        .then(data => {
            buildPrices(data)
        })
}

let buildPrices = (prices) => {
    let pricesWrapper = document.getElementById('prices-wrapper')
    pricesWrapper.innerHTML = ''
    for (let i = 0; prices.length > i; i++){
        let price = prices[i]

        let pricesCard = `
            <div>
                <p>${price.fraction} - ${price.price}</p>
            </div>
        `
        pricesWrapper.innerHTML += pricesCard
    }
}

getPrices()
