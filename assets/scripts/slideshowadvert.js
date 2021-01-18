
var slideIndexadvert,slidesadvert,dotsadvert,captionTextadvert;
function initGalleryadvert(){
    slideIndexadvert = 0;
    slidesadvert=document.getElementsByClassName("imageHolderadvert");
    slidesadvert[slideIndexadvert].style.opacity=1;

    captionTextadvert=document.querySelector(".captionTextadvertHolderadvert .captionTextadvertadvert");
    captionTextadvert.innerText=slidesadvert[slideIndexadvert].querySelector(".captionTextadvert").innerText;

    //disable currentadvertPrevBtn if slide count is one
    if(slidesadvert.length<2){
        var currentPrevBtnsadvert=document.querySelector(".leftArrowadvert,.rightArrowadvert");
        currentPrevBtnsadvert.style.display="none";
        for (i = 0; i < currentPrevBtnsadvert.length; i++) {
            currentPrevBtnsadvert[i].style.display="none";
        }
    }

    //add dotsadvert
    dotsadvert=[];
    var dotsadvertContainer=document.getElementById("dotsadvertContaineradvert"),i;
    for (i = 0; i < slidesadvert.length; i++) {
        var dotadvert=document.createElement("span");
        dotadvert.classList.add("dotsadvert");
        dotsadvertContainer.append(dot);
        dotadvert.setAttribute("onclick","moveSlide("+i+")");
        dotsadvert.push(dot);
    }
    dotsadvert[slideIndexadvert].classList.add("active");
}
initGalleryadvert();
function plusSlidesadvert(n) {
    moveSlide(slideIndexadvert+n);
}
function moveSlideadvert(n){
    var i;
    var currentadvert,currentadvert;
    var moveSlideAnimClass={
          forCurrent:"",
          forNext:""
    };
    var slideTextAnimClass;
    if(n>slideIndexadvert) {
        if(n >= slidesadvert.length){n=0;}
        moveSlideAnimClass.forCurrent="moveLeftCurrentSlideadvert";
        moveSlideAnimClass.forNext="moveLeftNextSlideadvert";
        slideTextAnimClass="slideTextFromTopadvert";
    }else if(n<slideIndexadvert){
        if(n<0){n=slidesadvert.length-1;}
        moveSlideAnimClass.forCurrent="moveRightCurrentSlideadvert";
        moveSlideAnimClass.forNext="moveRightPrevSlideadvert";
        slideTextAnimClass="slideTextFromBottomadvert";
    }

    if(n!=slideIndexadvert){
        currentadvert = slidesadvert[n];
        currentadvert=slidesadvert[slideIndexadvert];
        for (i = 0; i < slidesadvert.length; i++) {
            slidesadvert[i].className = "imageHolderadvert";
            slidesadvert[i].style.opacity=0;
            dotsadvert[i].classList.remove("active");
        }
        currentadvert.classList.add(moveSlideAnimClass.forCurrent);
        currentadvert.classList.add(moveSlideAnimClass.forNext);
        dotsadvert[n].classList.add("active");
        slideIndexadvert=n;
        captionTextadvert.style.display="none";
        captionTextadvert.className="captionTextadvertadvert "+slideTextAnimClass;
        captionTextadvert.innerText=slidesadvert[n].querySelector(".captionTextadvertadvert").innerText;
        captionTextadvert.style.display="block";
    }

}
var timeradvert=null;
function setTimeradvert(){
    timeradvert=setInterval(function () {
        plusSlidesadvert(1) ;
    },3000);
}
setTimeradvert();
function playPauseSlidesadvert() {
    var playPauseBtnadvert=document.getElementById("playPauseadvert");
    if(timeradvert==null){
        setTimeradvert();
        playPauseBtnadvert.style.backgroundPositionY="0px"
    }else{
        clearInterval(timeradvert);
        timeradvert=null;
        playPauseBtnadvert.style.backgroundPositionY="-33px"
    }
}