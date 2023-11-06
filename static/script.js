// Remember: Try to work this on script.js
function sign_in() {
    window.location.href = '/es/sign-in';
}
function sign_up() {
    window.location.href = '/es/sign-up';
}

const cards = document.querySelectorAll('.card');
const popup = document.getElementById('popup');
const popupTitle = document.getElementById('popup-title');
const popupDescription = document.getElementById('popup-description');
const closePopup = document.getElementById('close-popup');
const imgPopup = document.getElementById('popup-img');
cards.forEach(card => {
    card.addEventListener('click', () => {
        const index = card.getAttribute('data-index');
        const title = card.getAttribute('data-title');
        const descripcion = card.getAttribute('data-descripcion');
        const img = card.getAttribute('data-img');

        imgPopup.src = `/static/img/publicaciones/${img}`;
        popupTitle.textContent = `${title}`;
        popupDescription.textContent = `${descripcion}`;
        popup.style.display = 'block';
        });
    });
closePopup.addEventListener('click', () => {
            popup.style.display = 'none';
        });

