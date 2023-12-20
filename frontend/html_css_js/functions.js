function add(a, b) {
    console.log(a + b);
}

greater = function (a, b) {
    if (a > b) {
        console.log(a);
    }
    else {
        console.log(b);
    }
}

check_equal = (a, b) => {
    console.log(a == b)
}

(() => {
    console.log(!(10 >= 20));
})()

add(1, 3);
greater(10, 20);
check_equal(10, '10')
