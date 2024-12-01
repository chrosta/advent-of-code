#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 1A.js
//-------------------------------------------------------------------------------------------------------------
import ReadFile from './libs/read_file.js';

const rf = new ReadFile('./data/1.text');
rf.data((d) => {
    console.log("DATA:");
    console.log("---");
    Object.keys(d).forEach((k) => {
        console.log(d[k]);
    });
    console.log("---");

    let a = [];
    let b = [];
    let t = [];
    Object.keys(d).forEach((k) => {
        t = d[k].split(/\s+/);
        a.push(t[0]);
        b.push(t[1]);
    });
    a.sort();
    b.sort();
    console.log(a);
    console.log(b);
    console.log("---");
    
    let r = 0;
    let s = 0;
    Object.keys(a).forEach((i) => {
        r = Math.abs(a[i] - b[i]);
        s += r;
    });
    console.log(s);
});
