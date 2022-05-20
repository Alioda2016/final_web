const checkbox = document.getElementById('auto');

let turn = false;
        // Initialize new SpeechSynthesisUtterance object
let speech = new SpeechSynthesisUtterance();
        // Set Speech Language
speech.lang = "en";

checkbox.addEventListener('change', (event) => {
  if (event.currentTarget.checked) {
    // Start Speaking
    console.log("i am here on")
    turn = true;
    //window.speechSynthesis.speak(speech);
  } else {
    console.log("i am here off")
      turn = false;
    //window.speechSynthesis.cancel();
  }
});

function GFG_Fun(){
  var executed = false;
  console.log("we are outside the if")
  if (turn == true){
    console.log("we are inside the if")
    var x = event.clientX;
    var y = event.clientY;
    el = document.elementFromPoint(x, y);
    //down.innerHTML = el.innerHTML;
    let text = String(el.textContent);
    speech.text = text;
    window.speechSynthesis.speak(speech);
    
  }
  return function() {
      if (!executed) {    
          executed = true;
          // do something
      }
  };
}

// function GFG_Fun() {
//   console.log("i am here reading")
//     if(turn == true){
//         var x = event.clientX;
//         var y = event.clientY;
//         el = document.elementFromPoint(x, y);
//         //down.innerHTML = el.innerHTML;
//         let text = String(el.textContent);
//         speech.text = text;
//         window.speechSynthesis.speak(speech);
//     }
// }
