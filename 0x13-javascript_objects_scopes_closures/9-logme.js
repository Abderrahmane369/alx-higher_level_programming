#!/usr/bin/node

exports.logMe = ((item) => {
  let _ = 0;
  return function (item) {
    console.log(`${_}: ${item}`);
    _++;

    return _;
  };
})();
