let section1cl4=document.querySelectorAll('.singleServicescoll-4')[0];
let mediumDiv=document.createElement('div');
mediumDiv.className='medium-logo';
section1cl4.appendChild(mediumDiv);
let imgs=['img/4.jpg','img/5.jpg','img/6.jpg','img/7.jpg']
for(i=0;i<imgs.length;i++){
let section1c4Div=document.createElement('div');
section1c4Div.className='allup-logo';
let section1c4DivImg=document.createElement('img');
section1c4DivImg.setAttribute('src',imgs[i]);
section1c4Div.appendChild(section1c4DivImg);
mediumDiv.appendChild(section1c4Div);
section1c4Div.style.height=400+'px';}


let aboutbtnLeft=document.querySelectorAll('.singleServices-btn')[0]
aboutbtnLeft.addEventListener('click',Run1)
a=-3;
b=-384;
let allup_logo=document.querySelector('.medium-logo');
function Run1(){
    if(a<-3){
        a=a-b;
        allup_logo.style.left=a+'px';}
        else{
            a=a+(b*3)
        }
        allup_logo.style.left=a+'px'; 
}
let aboutbtnRight=document.querySelectorAll('.singleServices-btn')[1];
let interval=setInterval(Run2,3000)
a=-3;
b=-384;
function Run2(){
    if(a>= -771){
    a=a+b;
    allup_logo.style.left=a+'px';
function stop(){
    clearInterval(interval)
}
aboutbtnRight.addEventListener('click',stop)
aboutbtnLeft.addEventListener('click',stop)
}else{
    a=a-(b*3);
}
    allup_logo.style.left=a+'px';
}
aboutbtnRight.addEventListener('click',Run2)


let li1=document.querySelectorAll('.li')[1]
let allP=document.querySelectorAll('.all-p')[0]
var liInterval=setInterval(Begin1,200)
z1=300;
function Begin1(){
    if(z1>0){
    z1=z1-300
    allP.style.top=z1+'px'}
}

let allp=document.querySelectorAll('.all-p')[1]
var liInterval=setInterval(Begin2,200)
z2=300;
function Begin2(){
    if(z2>0){
    z2=z2-300
    allp.style.top=z2+'px'}
    }
function Clear(){
    clearInterval(liInterval)
}
li1.addEventListener('click',Begin1)
li1.addEventListener('click',Begin2)
li1.addEventListener('click',Clear)

let serviceUl=document.querySelectorAll('ul')[1]
console.log(serviceUl)
let li2=document.querySelectorAll('.li')[2]
console.log(li2)
li2.addEventListener('mouseover',function(){
    serviceUl.style.display="block"
})
li2.addEventListener('mouseout',function(){
    serviceUl.style.display="none"})

