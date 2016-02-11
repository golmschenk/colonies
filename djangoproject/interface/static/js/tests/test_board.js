var assert = require('assert');

var Board = require('../board.js').Board;


describe('Board', function() {
    'use strict';
    describe('#clicks', function () {
        it('should be incrementable', function () {
            var board = new Board();
            assert.equal(board.clicks, 0);
            board.clicks += 1;
            assert.equal(board.clicks, 1);
        });
    });
});
