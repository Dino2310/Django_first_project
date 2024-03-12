
let input = document.querySelector("#coment_in")

function change_name_button_comments(){

    document.querySelector("#form_com").innerHTML = input.value?
    'Отправить комментарий...' :
    'Просмотреть все комментарии к посту'  
}


input.addEventListener("input", change_name_button_comments)
input.required = ''