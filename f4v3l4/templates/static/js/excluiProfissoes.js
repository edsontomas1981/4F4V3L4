function excluiProfissao(idExcProf){
    
    var id = document.getElementById('excluiProfId');
    var categoria = document.getElementById('excluiCategoria');
    var titulo = document.getElementById('excluiTitulo');

    id.value = idExcProf;
    categoria.value = document.getElementById('categoria'+idExcProf).textContent;
    titulo.value = document.getElementById('titulo'+idExcProf).textContent;
}