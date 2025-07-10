var output = document.querySelector('.output');
output.innerHTML = '';

for (var i = 10; i >= 0; i--){
    var para = document.createElement('p');

    if (i === 10){
        para.textContent = "countdown 10";
    }else if ( i === 0){
        para.textContent = "blast off!";
    }else {
        para.textContent = i;
    }

    output.appendChild(para)
}



