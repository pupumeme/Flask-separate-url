function clickToggle(value){
    var boxState=document.querySelector("input[value="+value+"]").checked
    if(boxState) {
      alert(value+" open")
    } else {
      alert(value+" close") 
    } 
} 