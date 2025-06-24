

if(!localStorage.getItem('counter')){
    localStorage.setItem('counter',0);
}

let counter = localStorage.getItem('counter');



function count(){
    
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter',counter)


    // setInterval(count,1000);

    // if(counter % 10 === 0){
    //     alert(`count is now ${counter}`)
    // }
}

function decount(){
    if (counter > 0){
        counter--;
        // alert(counter);
    }
    
    // document.querySelector("#counter").innerText = counter;
    document.querySelector("h1").innerHTML = counter;
    // setInterval(decount,1000);
    localStorage.setItem('counter',counter)

}



document.addEventListener('DOMContentLoaded',function(){
    
    document.querySelector("h1").innerHTML = localStorage.getItem('counter');

    document.querySelector('#btnc').addEventListener('click',count);

    document.querySelector('#btnd').onclick = decount; // Assuming you want a button for decount as well

});

