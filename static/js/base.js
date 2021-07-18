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



//Landing Page Video and Switch Button

const btn = document.querySelector('.switch-btn');
const video = document.querySelector('.video-container');

btn.addEventListener('click', function(){
    if(!btn.classList.contains('slide')){
        btn.classList.add('slide');
        video.pause();
    }
    else{
        btn.classList.remove("slide");
        video.play();
    }
    console.log("hello")
})
