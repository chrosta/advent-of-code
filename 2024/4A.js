#! /usr/bin/node
//-------------------------------------------------------------------------------------------------------------
// 4A.js
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
    let f = [];
    let s = 0;

    let r = 0;
    let c = 0;
    let g = 0;
    let l = "";
    do {
        l = "";
        r += g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                c += 1;
            }
        } while (r < d.length);
        console.log(l);
        f.push(l);
        g += 1;
        r = 0;
        c = 0;
    } while (g < d.length);
    console.log("---");

    r = 0;
    c = 0;
    g = 0;
    l = "";
    do {
        l = "";
        c += g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                r += 1;
                c += 1;
            }
        } while (r < d.length);
        console.log(l);
        f.push(l);
        g += 1;
        r = 0;
        c = 0;
    } while (g < d.length);
    console.log("---");

    r = 0;
    c = 0;
    g = 1;
    l = "";
    do {
        l = "";
        r += g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                r += 1;
                c += 1;
            }
        } while (r < d.length);
        console.log(l);
        f.push(l);
        g += 1;
        r = 0;
        c = 0;
    } while (g < d.length);
    console.log("---");

    r = d.length - 1;
    c = 0;
    g = 0;
    l = "";
    do {
        l = "";
        c += g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                r -= 1;
                c += 1;
            }
        } while (r >= 0);
        console.log(l);
        f.push(l);
        g += 1;
        r = d.length - 1;
        c = 0;
    } while (g < d.length);
    console.log("---");

    r = d.length - 1;
    c = 0;
    g = 1;
    l = "";
    do {
        l = "";
        r -= g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                r -= 1;
                c += 1;
            }
        } while (r >= 0);
        console.log(l);
        f.push(l);
        g += 1;
        r = d.length - 1;
        c = 0;
    } while (g < d.length);
    console.log("---");

    r = 0;
    c = 0;
    g = 0;
    l = "";
    do {
        l = ""
        c += g;
        do {
            if (d[r][c] === undefined) {
                break;
            } else {
                l += d[r][c];
                r += 1;
            }
        } while (r < d.length);
        console.log(l);
        f.push(l);
        g += 1;
        r = 0;
        c = 0;
    } while (g < d.length);
    console.log("---");
    console.log(f);
    console.log("===");

    f.forEach((g) => {
        console.log(g);
        try {
            s += g.match(/(?=(XMAS))|(?=(SAMX))/g).length;
        } catch (e) {}
    });

    console.log("===");
    console.log(s);
});

