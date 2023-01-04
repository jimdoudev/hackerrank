function repeatedString(s, n) {
    let counter1 = 0;
    let counter2 = 0;    
    let t = Math.floor(n/s.length);
    let rem = n%s.length;
    
    for(let i=0; i<s.length;i++) {
        if (s[i] == "a") {
            counter1 ++;
        }
    }
    
    let mainStr = t*counter1;
    
    let remStr = s.substring(0,rem);
    
    for(let i=0; i<remStr.length;i++) {
        if (remStr[i] == "a") {
            counter2 ++;
        }
    }
    
    return mainStr + counter2
}

console.log(repeatedString("aba", 10))