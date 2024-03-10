let a = document.querySelector('.image-div')

setInterval(
    () => { a.style.color = 'red' }, 500
)
setInterval(
    () => { a.style.color = 'black' }, 1000
)

let input = document.querySelector("#coment_in")
input.addEventListener("input",()=>{
    console.log("Событие");
    if (input.value){
        document.querySelector("#form_com").innerHTML = 'Отправить комментарий...'
    }
    else{
        document.querySelector("#form_com").innerHTML = 'Просмотреть все комментарии к посту'
    }
})
