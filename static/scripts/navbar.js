$(document).ready(function () {
       //beging Nav Bar togler

       const toggler = document.querySelector('.navbarsec > .toggler'),
       navListContainer = document.querySelector('.navbarsec > .nav-list-container');
   
       /*when toggler button is clicked*/
       toggler.addEventListener(
       "click",
       () => {
           //convert hamburger to close
           toggler.classList.toggle('cross');
           //make nav visible
           navListContainer.classList.toggle('nav-active');
       },
       true
       );
   
   
       // End Navbar toglar
});