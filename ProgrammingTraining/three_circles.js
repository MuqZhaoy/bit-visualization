// section 1 base
// step1 selection
console.log("hi")
var circle = d3.selectAll("circle");

circle.style("fill", "steelblue");
circle.attr("r", 20);

// step2 binding
circle.data([32, 57, 112]);
circle.attr("r", function(d) { return Math.sqrt(d); });

circle.attr("cx", function(d, i) { return i * 100 + 30; });


// section 2 enter & exit
// step1 enter
var svg = d3.select("svg")
var circle = svg.selectAll("circle")
    .data([32, 57, 112, 293, 359, 743]);
var circleEnter = circle.enter().append("circle");

// step2 change attr
circleEnter.attr("cy", 60);
circleEnter.attr("r", function(d) { return Math.sqrt(d); });
circleEnter.attr("cx", function(d, i) { return i * 100 + 30; });

// step3 exit
circle = svg.selectAll("circle")
    .data([32, 57]);
circle.exit().remove();
