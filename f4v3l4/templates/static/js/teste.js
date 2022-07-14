function teste(event){
    var btnClose = document.querySelector('.close-preview-js');
    var foto = document.getElementById("foto_perfil");
    var output = document.getElementById("new");
    var img= document.getElementById("file-preview-js") 
    var reader = new FileReader();
        reader.onload = function() {
        output.style.display = "block";
        btnClose.style.display = "block";
        output.style.backgroundImage = "url("+reader.result+")";
        foto.value="url("+reader.result+")";
        }
          reader.readAsDataURL(event.target.files[0]);
          console.log(img.value);
          
}
