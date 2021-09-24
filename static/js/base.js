// Sidebar toggle for Navigation Menu.

const toggleBtn = document.querySelector('.sidebar-toggle');
const closeBtn = document.querySelector('.close-btn');
const sidebar = document.querySelector('.sidebar');

toggleBtn.addEventListener('click', function() {
    console.log(sidebar.classList)
        
    sidebar.classList.toggle('show-sidebar');
    
})

closeBtn.addEventListener('click', function() {
    sidebar.classList.remove('show-sidebar');
    
})




// JS for Free Delivery Banner 
// Rotating Text Credit to "Alphardex" at  
// https://codepen.io/alphardex/pen/WNNVJeZ // 

var values = document.getElementsByClassName('value');
var valueArray = [];
var currentValue = 0;

values[currentValue].style.opacity = 1;
for (var i = 0; i < values.length; i++) {
  splitLetters(values[i]);
}

function changeValue() {
  var cv = valueArray[currentValue];
  var nv = currentValue === values.length-1 ? valueArray[0] : valueArray[currentValue + 1];
  for (var i = 0; i < cv.length; i++) {
    animateLetterOut(cv, i);
  }
  
  for (var i = 0; i < nv.length; i++) {
    nv[i].className = 'letter behind';
    nv[0].parentElement.style.opacity = 1;
    animateLetterIn(nv, i);
  }
  
  currentValue = (currentValue == valueArray.length-1) ? 0 : currentValue+1;
}

function animateLetterOut(cv, i) {
  setTimeout(function() {
		cv[i].className = 'letter out';
  }, i*80);
  
}

function animateLetterIn(nv, i) {
  setTimeout(function() {
		nv[i].className = 'letter in';
  }, 340+(i*80));
}

function splitLetters(value) {
  var content = value.innerHTML;
  value.innerHTML = '';
  var letters = [];
  for (var i = 0; i < content.length; i++) {
    var letter = document.createElement('span');
    letter.className = 'letter';
    letter.innerHTML = content.charAt(i);
    value.appendChild(letter);
    letters.push(letter);
  }
  
  valueArray.push(letters);
}

changeValue();
setInterval(changeValue, 4000);


// Landing page Pop-Up to Subscribe after 2 seconds of page load.
// Activate Close X 

const popup = document.querySelector('.front-popup')
const close = document.querySelector('.close-popup')

window.onload = function(){
  setTimeout(function(){
    popup.style.display ="block"
    console.log("print me")
    // Delay popup 2secs ..
  }, 2000)
}

close.addEventListener('click', ()=> {
  popup.style.display = 'none';
  
})

