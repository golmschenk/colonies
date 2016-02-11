function Board() {
    'use strict';

    this.clicks = 0;
}

// Make this available for testing by Mocha.
if(typeof exports !== 'undefined') {
    exports.Board = Board;
}
