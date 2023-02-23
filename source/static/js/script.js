textarea = document.querySelector('textarea');
  if(textarea){
    textarea.addEventListener('input', autoResize, false);
    textarea.addEventListener('click', autoResize, false);
  }
        
    function autoResize() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    }


function checkbox_delete() {
  // Get the checkbox
  var checkBox = document.getElementById("btn-checkbox");
  // Get the output text
  var text = document.getElementById("checkbox-button");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
}
