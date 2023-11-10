// Redirect to pages
function sign_in() {
    window.location.href = '/es/sign-in';
}
function sign_up() {
    window.location.href = '/es/sign-up';
}
// User profile list
var userProfile = document.getElementById('userProfile');
var userList = document.getElementById('userList');

if(userProfile !== null){
userProfile.addEventListener('click', function (event) {
    if (userList.style.display === 'block') {
        userList.style.display = 'none';
    } else {
        userList.style.display = 'block';
    }

    event.stopPropagation(); // Prevent the document click event from immediately closing the list
    });
    // Hide the user list when clicking outside of it
    document.addEventListener('click', function (event) {
    var isClickInside = userProfile.contains(event.target);
    if (!isClickInside) {
        userList.style.display = 'none';
    }
});

}

const cards = document.querySelectorAll('.card');
const popup = document.getElementById('popup');
const popupTitle = document.getElementById('popup-title');
const popupDescription = document.getElementById('popup-description');
const closePopup = document.getElementById('close-popup');
const imgPopup = document.getElementById('popup-img');
const inputPopup = document.getElementById('input-popup');

cards.forEach(card => {
    card.addEventListener('click', () => {
        const index = card.getAttribute('data-index');
        const title = card.getAttribute('data-title');
        const descripcion = card.getAttribute('data-descripcion');
        const img = card.getAttribute('data-img');
        if (index !== null){
            imgPopup.src = `/static/img/publicaciones/${img}`;
            popupTitle.textContent = `${title}`;
            popupDescription.textContent = `${descripcion}`;
            inputPopup.setAttribute('value', `${index}`);
            popup.style.display = 'flex';
        }
        });
    });
    if(closePopup !== null){
        closePopup.addEventListener('click', () => {
            popup.style.display = 'none';
        });
    }
    
console.log("ESTO FUNCIONA")

// Pop-up if user not logged in
const likeButton = document.querySelectorAll(".like-button-popup");
const unlikeButton = document.querySelectorAll(".unlike-button-popup");
const sendButton = document.querySelectorAll(".send-button-popup");
const popupLogin = document.getElementById("popup-login");
const closeLogPopup = document.getElementById('close-login-popup');


// Función para mostrar el pop-up de inicio de sesión
function showLoginPopup() {
    popupLogin.style.display = "block";
}

// Agregar eventos a los botones
likeButton.forEach(button => {
    button.addEventListener("click", showLoginPopup);
});

unlikeButton.forEach(button => {
    button.addEventListener("click", showLoginPopup);
});

sendButton.forEach(button => {
    button.addEventListener("click", showLoginPopup);
});

closeLogPopup.addEventListener('click', () => {
    popupLogin.style.display = 'none';
});


