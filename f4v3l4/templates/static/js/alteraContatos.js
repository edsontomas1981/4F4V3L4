function altContato(id){

    var varAltTipo = 'tipo'+id ;
    var varAltCont = 'contato'+id ;

    var alteraTipo = document.getElementById(varAltTipo)
    var alteracontato = document.getElementById(varAltCont)
    var tipo = document.getElementById('alteraTipo')
    var contato = document.getElementById('alteraContato')
    var idContato = document.getElementById("idContato")
    tipo.value = alteraTipo.textContent
    contato.value = alteracontato.textContent
    idContato.value = id    
    }
