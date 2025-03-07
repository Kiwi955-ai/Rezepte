


function createDiv(img_name,name,spalte){
    let div = document.createElement('div');

    let link = document.createElement('a');
    link.href = "#"; 
    link.target = "_blank";

    let img = document.createElement('img');
    img.src = "img/Mozzarella-Sticks.jpg";
    img.alt = "Mozzarella-Sticks"; 

    let text = document.createElement('p');
    text.textContent = "Super Mozzarella-Sticks";

    link.appendChild(img);  
    div.appendChild(link);  
    div.appendChild(text);  
    spalte.appendChild(div);
}

const spalte1 = document.querySelector('.Spalte1')
const spalte2 = document.querySelector('.Spalte2')
const spalte3 = document.querySelector('.Spalte3')
createDiv("asd","ghj",spalte1)
createDiv("asd","ghj",spalte1)
createDiv("asd","ghj",spalte2)