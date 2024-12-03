#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 2A.js
//-------------------------------------------------------------------------------------------------------------
import ReadFile from './libs/read_file.js';

const rf = new ReadFile('./data/2.text');
rf.data((d) => {
    console.log("DATA:");
    console.log("---");
    Object.keys(d).forEach((k) => {
        d[k] = d[k].split(' ').map((x) => parseInt(x));
        console.log(k + ": " + d[k].join(','));
    });
    console.log("---");
    
    let aa = undefined;
    let bb = undefined;
    let s = 0;
    let t = 0;
    Object.keys(d).forEach((k) => {
        aa = Object.create(d[k]).map((x) => parseInt(x)).sort((a, b) => a - b).join(',');
        bb = Object.create(d[k]).map((x) => parseInt(x)).sort((a, b) => a - b).reverse().join(',');
        if (d[k].join(',') === aa || d[k].join(',') === bb) {
            t = 0;
            Object.keys(d[k]).forEach((i) => {
                i = parseInt(i);
                if (i < d[k].length-1) {
                    if (Math.abs(d[k][i] - d[k][i+1]) < 1 || Math.abs(d[k][i] - d[k][i+1]) > 3) {
                        t++;
                    }
                }
            });
            if (t === 0) {
                s++;
            }
        }
    });
    console.log(s);
});
