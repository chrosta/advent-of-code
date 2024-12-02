#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 1B.js
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
    
    let s = 0;
    let t = 0;
    let aa = undefined;
    let bb = undefined;
    let cc = undefined;
    d.forEach((e) => {
        console.log(e);
        for (let i = -1; i < e.length; i++) {
            cc = Object.create(e).map((x) => parseInt(x));
            if (i > -1) {
                delete cc[i];
                cc = cc.filter((x) => x !== undefined);
            }
            aa = Object.create(cc).map((x) => parseInt(x)).sort((a, b) => a - b).join(',');
            bb = Object.create(cc).map((x) => parseInt(x)).sort((a, b) => a - b).reverse().join(',');
            if (cc.join(',') === aa || cc.join(',') === bb) {
                t = 0;
                cc.forEach((cc_item, cc_index, cc_array) => {
                    if (cc_index < cc_array.length-1) {
                        if (Math.abs(cc_item - cc_array[cc_index+1]) < 1 || Math.abs(cc_item - cc_array[cc_index+1]) > 3) {
                            t++;
                        }
                    }
                });
                if (t === 0) {
                    s++;
                    break;
                }
            }
        }
    });
    console.log("---");
    console.log(s);
});
