#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 4B.js
//-------------------------------------------------------------------------------------------------------------
import ReadFile from './libs/read_file.js';

const rf = new ReadFile('./data/4.text');
rf.data((d) => {
    console.log("DATA:");
    console.log("---");
    Object.keys(d).forEach((k) => {
        console.log(k + ": " + d[k].split(''));
    });
    console.log("---");

    let s = 0;
    let a = '';
    let b = '';
    for (let r = 0; r < d.length; r++) {
        for (let c = 0; c < d[r].length; c++) {
            if (d[r][c] === 'A') {
                try {
                    a = d[r-1][c-1] + "A" + d[r+1][c+1];
                    b = d[r-1][c+1] + "A" + d[r+1][c-1];
                } catch (e) {}
                if (a.includes('undefined') || b.includes('undefined')) {
                    continue;
                } else {
                    if (a === "MAS" || a === "SAM") {
                        if (b === "MAS" || b === "SAM") {
                            console.log(r + "," + c + ": " + a + ", " + b);
                            s++;
                        }
                    }
                }
            }
        }
    }

    console.log("===");
    console.log(s);
});

