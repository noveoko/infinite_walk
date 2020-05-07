// let magic = 0

// function spit_it() {
//     console.log("Oh yeah!");
//     console.log(magic);
//     magic += 1;
//     setTimeout(spit_it, 3000);
// }
// while (1 == 1) { spit_it() }


x = 0
y = 0

for (let i = 1; i < 10; i++) {
    setTimeout(function timer() {
        x += 1;
        y += 1;
        console.log(x, y)
    }, i * 3000);
}