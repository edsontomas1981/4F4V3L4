function excluiProposta(id) {
    proposta = document.getElementById('excluir')
    proposta.value = id
}

function mes(strMes){
    let mes
}

function separaData(data) {
     mes 

}

function alteraProposta(id) {
    let valor = document.getElementById("valor")
    let obs = document.getElementById("obs")
    let datIni = document.getElementById("prevInicio")
    let prazo = document.getElementById("prazo")
    let data =document.getElementById("datIni" + id).value
    console.log(typeof(data))

    valor.value = document.getElementById("valor" + id).value
    obs.value = document.getElementById("obs" + id).value
    prazo.value = document.getElementById("prazo" + id).value
    datIni.value = Date.parse(data)
    console.log(Date.parse(data))
    proposta = document.getElementById('alterar')
    proposta.value = id
}