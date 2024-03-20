
let input = document.querySelector("#coment_in")
document.querySelector(".ch_false").input.required = ''
function change_name_button_comments(){

    document.querySelector("#form_com").innerHTML = input.value?
    'Отправить комментарий...' :
    'Просмотреть все комментарии к посту'  
}



if (input){
input.addEventListener("input", change_name_button_comments)
input.required = ''}