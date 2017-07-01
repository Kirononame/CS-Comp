var end = new Date(2017, 4, 24, 15, 15, 0, 0);
var endTime = end.getHours() + ':' + end.getMinutes();

function updateClock() {

    var now = new Date();

    time = now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds();
    
    var t = document.getElementById('time');

    if (t != null)
        t.innerHTML = 'current time ' + time + ' _ end time ' + endTime;
        
    // console.log('current time ' + time + ' _ end time ' + endTime);
    // console.log(now.getHours)
    // console.log(end.getHours)
    // console.log(now.getMinutes)
    // console.log(end.getMinutes)

    // console.log(now.getHours >= end.getHours);
    // console.log(now.getMinutes >= end.getMinutes);

    if((now.getHours() >= end.getHours()) && (now.getMinutes() >= end.getMinutes()))
        document.getElementById('all').innerHTML = 'Time Over';  
        
    else
        setTimeout(updateClock, 1000);
        

}

updateClock();