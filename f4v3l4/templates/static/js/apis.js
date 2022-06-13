// const response = await fetch(Url,{
//     method: 'POST',
//     body: JSON.stringify(contato),
//     headers: {
//         'Content-Type': 'application/json'
//     }
// })

// const contato = await response.json();

// function cadastrarContato(){

//     const data = {
//         "tipo": "Telefone",
//         "contato": "11969262288",
//         "usuario_fk": 1
//     };

//     var xhr = new XMLHttpRequest();

//     var dados = JSON.stringify(data);

//     xhr.open("POST", "http://127.0.0.1:8000/api/contatos/");
//     xhr.setRequestHeader('Content-Type', 'application/json');

//     xhr.addEventListener("load", function() {
//         var erroAjax = document.querySelector("#erro-ajax");

//         if (xhr.status == 200) {
//             erroAjax.classList.add("invisivel");
//             //sucesso!
//         } else {
//             erroAjax.classList.remove("invisivel");
//             //erro!
//         }
//     });

//     xhr.send(dados);

    // console.log('1 Parada');
    // fetch("http://127.0.0.1:8000/api/contatos", {
    // method: "POST",
    // headers: {
    // "Content-Type": "application/json",
    //   },
    // body: JSON.stringify(data),
    // })
    // .then((response) => response.json())
    // .then((data) => {
    // console.log("Success:", data);
    // })
    // .catch((error) => {
    // console.error("Error:", error);
    // });

    // event.preventDefault();
    // console.log("cadastrarContato");
    // let Url="127.0.0.1:8000/api/contatos/"; 
    // let tipo=document.getElementById("tipo").value;
    // let contato=document.getElementById("contato").value;
    // let usuario=document.getElementById("usuario").value;
   
    // let body={
    //     "tipo": "Telefone",
    //     "contato": "11969262288",
    //     "usuario_fk": 1
    // }
// }

