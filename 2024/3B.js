#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 3B.js
//-------------------------------------------------------------------------------------------------------------
import ReadFile from './libs/read_file.js';

const rf = new ReadFile('./data/3.text');
rf.data((d) => {
    console.log("DATA:");
    console.log("---");
    Object.keys(d).forEach((k) => {
        console.log(k + ": " + d[k]);
    });
    console.log("---");
    
    let b = 1;
    let s = 0;
    let o = [];
    d.forEach((e) => {
        e.match(/(mul\([0-9]+\,[0-9]+\))|(don't\(\))|(do\(\))/g).forEach((m) => {
            console.log(m);
            m = m.split('(');
            m[1] = m[1].replace(')', '');
            if (m[0] === "don't") b = 0;
            if (m[0] === "do") b = 1;
            if (b > 0 && m[0] === "mul") {
                o = m[1].split(',');
                s += o[0] * o[1] * b;
            }
        });
        console.log("---");
    });
    console.log(s);
});
