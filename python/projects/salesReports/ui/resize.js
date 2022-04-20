go();
window.addEventListener('resize', go);

function go(){
  document.querySelector('.width').innerText = document.documentElement.clientWidth;
  document.querySelector('.height').innerText = document.documentElement.clientHeight;

  if (document.documentElement.clientWidth < 673){
    console.log("width less than 673");
  }
}

// const heightOutput = document.querySelector("#height");
// const widthOutput = document.querySelector("#width");

// function resizeListener() {
//   heightOutput.textContent = window.innerHeight;
//   widthOutput.textContent = window.innerWidth;
// }

// window.addEventListener("resize", resizeListener);