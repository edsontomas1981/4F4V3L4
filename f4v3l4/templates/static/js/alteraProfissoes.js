function altProfissao(idExcProf){
    
    var id = document.getElementById('alteraProfId');
    var categoria = document.getElementById('alteraCategoria');
    var titulo = document.getElementById('alteraTitulo');
    var sobre = document.getElementById('alteraSobre');


    id.value = idExcProf;
    categoria.value = document.getElementById('categoria'+idExcProf).textContent;
    titulo.value = document.getElementById('titulo'+idExcProf).textContent;
    sobre.value = document.getElementById('sobre'+idExcProf).textContent;
}

console.log('teste')