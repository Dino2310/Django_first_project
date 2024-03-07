
# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 1050

def _get_part_text(text, start, lenght):
    minLen = min(start+lenght+1 ,len(text))
    if minLen==len(text): return(text[start:], len(text[start:]))
    text=text[start:minLen]
    while text[-1] in '.,?!:;':
        text=text[:-1]
    while not text[-1] in '.,?!:;':
        text=text[:-1]
        
    return (text, len(text))
    
    
                                 
                                




# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    text= open(path,encoding='utf-8').read()
    while (answer := _get_part_text(text,sum(map(len,book.values())),PAGE_SIZE)[0]):
        book[len(book)+1]=answer[0].lstrip()
            
        


prepare_book("book.txt")
for i in book.items():
    print(*i)
            
              
              