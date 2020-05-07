(function() {
    //let _ = require('lodash');
    const canvas = document.getElementById("mainCanvas");
    const ctx = canvas.getContext("2d");
    let keep_drawing = true;
    let loopy = true;
    new_canvas("VGA")



    function next_step() {
        directions = [
            [0, 1], //right
            [1, 0], //up
            [0, -1], //left
            [-1, 0], //down
            [1, 1], //up-right
            [-1, -1], //down-left
            [1, -1], //up-left
            [-1, 1], //down-right
        ]

        index = _.random(0, directions.length - 1)
        return directions[index]
    }

    function toggle_it() {
        switch (loopy) {
            case true:
                loopy = false;
                console.log("Set loopy to false")
                break;
            case false:
                loopy = true;
                console.log("Set loopy to true")
                break;
        }
    }

    function draw_frame(start_x, start_y, line_thickness, line_color, this_loopy) {
        switch (keep_drawing) {
            case true:
                let next_instruction = next_step()
                switch (this_loopy) {
                    case false:
                        distances = [0, 1, 3, 5, 10, 100, 1000]
                        distance = _.random(0, distances.length - 1)
                        for (i = 0; i <= distance; i++) {
                            ctx.beginPath();
                            ctx.moveTo(start_x, start_y); //start cursor here
                            start_x += next_instruction[0]
                            start_y += next_instruction[1]
                            ctx.lineTo(start_x, start_y);
                            ctx.stroke();

                        }
                        return [start_x, start_y]
                    case true:
                        ctx.beginPath();
                        ctx.moveTo(start_x, start_y); //start cursor here
                        start_x += next_instruction[0]
                        start_y += next_instruction[1]
                        ctx.lineTo(start_x, start_y);
                        ctx.stroke();
                        return [start_x, start_y]

                }

            case false:
                console.log("Drawing disabled!")
            default:
                console.log(keep_drawing)
                break;
        }
    }

    function draw_shape(start_x, start_y) {
        let this_loopy = loopy;
        keep_drawing = true;
        let t0 = performance.now()
        let line_color = document.querySelector("#line_color").value
        let line_thickness = document.querySelector("#line_thickness").value

        console.log("INPUTS TO STARTSHAPE:", start_x, start_y)
        let x_mid = document.querySelector("canvas").width / 2;

        let y_mid = document.querySelector("canvas").height / 2;
        let steps = document.querySelector("#draw_steps").value;
        let speed = 1000 / document.querySelector("#frame_rate").value;
        //console.log(`Milliseconds per frame: ${speed}`)

        start_x = start_x || x_mid
        start_y = start_y || y_mid
        console.log("DRAWING_SHAPE...", start_x, start_y)
        ctx.strokeStyle = line_color;
        ctx.lineWidth = line_thickness;
        for (let i = 1; i < steps; i++) {
            setTimeout(function timer() {
                console.log(start_x, start_y)
                new_pos = draw_frame(start_x, start_y, line_thickness, line_color, this_loopy)
                start_x = new_pos[0]
                start_y = new_pos[1]
            }, i * speed);
        }
        let t1 = performance.now()
        document.querySelector("#draw_time").value = t1 - t0 //milliseconds
    }

    //custom support functions START
    function clear_canvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function save_image() {
        var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream"); // here is the most important part because if you dont replace you will get a DOM 18 exception.
        window.location.href = image; // it will save locally
    }

    function new_canvas(new_res, transparent, background_color) {
        new_res = new_res || document.querySelector("#set_resolution").value;
        background_color = background_color || document.querySelector("#background_color").value;
        transparent = transparent || document.querySelector("#transparency").checked;


        resolutions = {
            "8k": [7680, 4320],
            "4k": [4096, 2160],
            "UHD": [3840, 2160],
            "FullHD": [1920, 1080],
            "VGA": [640, 480],
            "Atari2600": [160, 192]
        }

        x_y = resolutions[new_res];

        canvas.width = x_y[0]
        canvas.height = x_y[1]
        clear_canvas()
        if (transparent == false) {
            console.log("Color background")
            console.log(background_color)
            ctx.fillStyle = background_color;
            ctx.fillRect(0, 0, canvas.width, canvas.height);


        } else {
            console.log("transparent background")


        }

    }

    function getMousePosition(canvas, event) {
        let rect = canvas.getBoundingClientRect();
        console.log(rect)
        let x = event.clientX - rect.left;
        let y = event.clientY - rect.top;
        console.log(x, y)
        document.querySelector("#next_x").value = x
        document.querySelector("#next_y").value = y
        draw_shape(x, y)
    }

    canvas.addEventListener("mousedown", function(e) {
        getMousePosition(canvas, e);
    });





    //custom support functions END

    //user interface START
    document.getElementById("erase_canvas").addEventListener("click", function() {
        keep_drawing = false;
        console.log('Erase clicked')
        clear_canvas();
    });
    document.getElementById("new_canvas").addEventListener("click", function() {
        console.log('New canvas clicked')
        keep_drawing = false;
        new_canvas();
    });

    document.getElementById("generate_art").addEventListener("click", function() {
        keep_drawing = true; //lets drawing take place
        draw_shape()
    });
    document.getElementById("save_image").addEventListener("click", function() {
        console.log('Image saved')
        save_image();
    });
    document.getElementById("set_resolution").addEventListener("change", function() {
        keep_drawing = false; //stop all drawing activity
        console.log('Size set')
        let new_res = document.querySelector("#set_resolution").value
        new_canvas(new_res);

    });

    document.querySelector("#generate_from_coords").addEventListener("click", function() {
        console.log('Selected x,y')
        getMousePosition()
        let new_x = document.querySelector("#next_x").value;
        let new_y = document.querySelector("#next_y").value;
        draw_shape(new_x, new_y)
    });

    document.getElementById("loopy_toggle").addEventListener("click", function() {
        console.log('Loopy toggled')
        toggle_it()
        console.log(`Loopy is: ${loopy}`)
    });
    //user interface END





}());