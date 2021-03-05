module.exports = {
  my_sum: function (a, b, c) {
    if (a <= 0 || a > 15 || b <= 1 || b > 20 || c <= 2 || c > 25)
      return "Out of Range";
    return a + b + c;
  },
};
