/* ========== TYPEWRITER HOMEPAGE EFFECT ========== */
/* url - https://codepen.io/aniketkr/pen/xxEYYjW */
const typedText = document.querySelector(".typed-text");
const cursor = document.querySelector(".cursor");

const textArray = ["Product Manager", "Web Developer"];

let textArrayIndex = 0;
let charIndex = 0;

const erase = () => {
  if (charIndex > 0) {
    cursor.classList.remove('blink');
    typedText.textContent = textArray[textArrayIndex].slice(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 80);
  } else {
    cursor.classList.add('blink');
    textArrayIndex++;
    if (textArrayIndex > textArray.length - 1) {
      textArrayIndex = 0;
    }
    setTimeout(type, 1000);
  }
}

const type = () => {
  if (charIndex <= textArray[textArrayIndex].length - 1) {
    cursor.classList.remove('blink');
    typedText.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 120);
  } else {
    cursor.classList.add('blink');
    setTimeout(erase, 1000);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  type();
})

/* ========== SHOW MENU ========== */
const showMenu = (toggleId, navId) =>{
const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)
    
    if (toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show-menu')
        })
    }

    window.onscroll = () => {
        nav.classList.remove('show-menu')
    }
}

showMenu('nav-toggle', 'nav-menu')

/* ========== REMOVE MENU MOBILE ========== */
const navLink = document.querySelectorAll('.nav_link')

function linkAction() {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/* ========== SCROLL SECTIONS ACTIVE LINK ========== */
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50
        sectionId = current.getAttribute('id')

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.add('active-link')
        } else {
            document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

/* ========== CHANGE BACKGROUND HEADER ========== */
function scrollHeader() {
    const header = document.getElementById('header')
    if (this.scrollY >= 200) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/* ========== SHOW SCROLL TOP ========== */
function scrollTop() {
    const scrollTop = document.getElementById('scroll-top')
    if (this.scrollY >= 560) scrollTop.classList.add('show-scroll'); else scrollTop.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollTop)

/* ========== MIXITUP FILTER PORTFOLIO ========== */
const mixer = mixitup('.portfolio_container', {
    selectors: {
        target: '.portfolio_content'
    },
    animation: {
        duration: 400
    }
});

/* Link Active Portfolio */
const linkPortfolio = document.querySelectorAll('.portfolio_item')

function activePortfolio() {
    if (linkPortfolio) {
        linkPortfolio.forEach(l => l.classList.remove('active-portfolio'))
        this.classList.add('active-portfolio')
    }
}
linkPortfolio.forEach(l => l.addEventListener('click', activePortfolio))

/* ========== GSAP ANIMATION ========== */
gsap.from(".home_img", {opacity:0, duration:1, delay:.25, x:60})
gsap.from(".home_data", {opacity:0, duration:1, delay:.55, y:25})
gsap.from(".home_greeting .home_name, .home_profession, .home_button", {opacity:1, duration:1, delay:.8, y:25, ease:'expo.out', stagger:.2})

gsap.from(".nav_logo, .nav_toggle", { opacity: 0, duration: 1, delay: 1, y: 25, ease:'expo.out', stagger:.2 })
gsap.from(".nav_item", { opacity: 0, duration: 1, delay: 1.4, y: 25, ease:'expo.out', stagger:.2 })
gsap.from(".home_social-icon", { opacity: 0, duration: 1, delay: 1.9, y: 25, ease: 'expo.out', stagger: .2 })

/* ========== DARK/LIGHT MODE ========== */
let darkmode = document.querySelector('#darkmode');

darkmode.onclick = () => {
    if (darkmode.classList.contains('bx-moon')) {
        darkmode.classList.replace('bx-moon', 'bx-sun');
        document.body.classList.add('active');
    } else {
        darkmode.classList.replace('bx-sun', 'bx-moon');
        document.body.classList.remove('active');
    }
}

// jQuery Block
$(document).ready(function () {
/* ========== SHOW SCROLL TOP - IFTI ========== */
    let topButton = $('#back-to-top-btn');
    $(window).scroll(function () {
        if ($(window).scrollTop() > 250) {
            topButton.addClass('visible');
        } else {
            topButton.removeClass('visible');
        }
    });

/* ========== CLICK SCROLL TOP - IFTI ========== */
    topButton.on('click', function (event) {
        event.preventDefault();
        $('html, body').scrollTop(0);
    });

});