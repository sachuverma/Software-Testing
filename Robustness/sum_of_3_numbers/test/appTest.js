const assert = require("chai").assert;
const my_sum = require("../app").my_sum;

describe("App", function () {
  it("a=5, b=5, c=5", function () {
    result = my_sum(5, 5, 5);
    assert.equal(result, 15);
  });

  it("a=0, b=5, c=5", function () {
    result = my_sum(0, 5, 5);
    assert.equal(result, "Out of Range");
  });

  it("a=1, b=5, c=5", function () {
    result = my_sum(1, 5, 5);
    assert.equal(result, 11);
  });

  it("a=2, b=5, c=5", function () {
    result = my_sum(2, 5, 5);
    assert.equal(result, 12);
  });

  it("a=16, b=5, c=5", function () {
    result = my_sum(16, 5, 5);
    assert.equal(result, "Out of Range");
  });

  it("a=15, b=5, c=5", function () {
    result = my_sum(15, 5, 5);
    assert.equal(result, 25);
  });

  it("a=14, b=5, c=5", function () {
    result = my_sum(14, 5, 5);
    assert.equal(result, 24);
  });

  it("a=5, b=1, c=5", function () {
    result = my_sum(5, 1, 5);
    assert.equal(result, "Out of Range");
  });

  it("a=5, b=2, c=5", function () {
    result = my_sum(5, 2, 5);
    assert.equal(result, 12);
  });

  it("a=5, b=3, c=5", function () {
    result = my_sum(5, 3, 5);
    assert.equal(result, 13);
  });

  it("a=5, b=21, c=5", function () {
    result = my_sum(5, 21, 5);
    assert.equal(result, "Out of Range");
  });

  it("a=5, b=20, c=5", function () {
    result = my_sum(5, 20, 5);
    assert.equal(result, 30);
  });

  it("a=5, b=19, c=5", function () {
    result = my_sum(5, 19, 5);
    assert.equal(result, 29);
  });

  it("a=5, b=5, c=2", function () {
    result = my_sum(5, 5, 2);
    assert.equal(result, "Out of Range");
  });

  it("a=5, b=5, c=3", function () {
    result = my_sum(5, 5, 3);
    assert.equal(result, 13);
  });

  it("a=5, b=5, c=4", function () {
    result = my_sum(5, 5, 4);
    assert.equal(result, 14);
  });

  it("a=5, b=5, c=26", function () {
    result = my_sum(5, 5, 26);
    assert.equal(result, "Out of Range");
  });

  it("a=5, b=5, c=25", function () {
    result = my_sum(5, 5, 25);
    assert.equal(result, 35);
  });

  it("a=5, b=5, c=24", function () {
    result = my_sum(5, 5, 24);
    assert.equal(result, 34);
  });
});
