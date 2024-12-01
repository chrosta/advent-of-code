//-------------------------------------------------------------------------------------------------------------
// ReadFile.
//-------------------------------------------------------------------------------------------------------------
import fs from 'node:fs';

export default class ReadFile {

    constructor(p) {
        this.path = p;
    }

    data(c) {
        fs.readFile(this.path, 'utf8', (e, d) => {
            if (e) {
                console.error(e);
            } else {
                d = d.toString().split("\n");
                d = d.filter((l) => l.length > 0);
                c(d);
            }
        });
    }
}
