function clickToggle(value){
  var boxState=document.querySelector("input[value="+value+"]").checked
  if(boxState) {
    post_to_url('/infos', {'led': "open "+value});
  } else {
    post_to_url('/infos', {'led': "close "+value});
  } 
} 
//post  function
function post_to_url(path, params, method="post") {
  var form = document.createElement("form");
  form.setAttribute("method", method);
  form.setAttribute("action", path);

  for(var key in params) {
      var hiddenField = document.createElement("input");
      hiddenField.setAttribute("type", "hidden");
      hiddenField.setAttribute("name", key);
      hiddenField.setAttribute("value", params[key]);

      form.appendChild(hiddenField);
  }

  document.body.appendChild(form);    // Not entirely sure if this is necessary
  form.submit();
}