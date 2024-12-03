#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 3A.js
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
    
    let s = 0;
    let o = [];
    d.forEach((e) => {
        e.match(/mul\([0-9]+\,[0-9]+\)/g).forEach((m) => {
            console.log(m);
            m.match(/[0-9\,]+/g).forEach((n) => {
                o = n.split(',');
                s += o[0] * o[1];
            });
        });
        console.log("---");
    });
    console.log(s);
});
