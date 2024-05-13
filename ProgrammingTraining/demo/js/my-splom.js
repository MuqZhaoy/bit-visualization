// Refer to https://observablehq.com/@d3/brushable-scatterplot-matrix
d3.csv('./data/Iris.csv', d3.autoType) // https://github.com/d3/d3-dsv#autoType
  .then(function(data) {
    console.log('data: ', data)

    let columns = data.columns.filter(d => d !== 'Species')

    let width = 964
    let padding = 20
    let size = (width - (columns.length + 1) * padding) / columns.length + padding

    let x = columns.map(c => d3.scaleLinear()
        .domain(d3.extent(data, d => d[c]))
        .rangeRound([padding / 2, size - padding / 2]))

    let y = x.map(x => x.copy().range([size - padding / 2, padding / 2]))

    let z = d3.scaleOrdinal()
        .domain(data.map(d => d['Species']))
        .range(d3.schemeCategory10)

    // handle xAixis
    let xAxis = (g)=>{
      const axis = d3.axisBottom()
          .ticks(6)
          .tickSize(size * columns.length);
      return g.selectAll("g").data(x).join("g")
          .attr("transform", (d, i) => `translate(${i * size},0)`)
          .each(function(d) { return d3.select(this).call(axis.scale(d)); })
          .call(g => g.select(".domain").remove())
          .call(g => {
            g.selectAll(".tick line").attr("stroke", "#ddd")
              .attr('y1', size * columns.length)
          });
    }

    // handle yAixis
    let yAxis = (g)=>{
      const axis = d3.axisLeft()
          .ticks(6)
          .tickSize(-size * columns.length);
      return g.selectAll("g").data(y).join("g")
          .attr("transform", (d, i) => `translate(0,${i * size})`)
          .each(function(d) { return d3.select(this).call(axis.scale(d)); })
          .call(g => g.select(".domain").remove())
          .call(g => {
            g.selectAll(".tick line").attr("stroke", "#ddd")
              .attr('x2', 0)
          });
    }

    const svg = d3.select("svg")
        .attr("viewBox", [-padding, 0, width, width]);

    svg.append("style")
        .text(`circle.hidden { fill: #000; fill-opacity: 1; r: 1px; }`);

    let g_xAxis = svg.append("g")
        .attr('class', 'xAxis')
        .call(xAxis);

    let g_yAxis = svg.append("g")
        .attr('class', 'yAxis')
        .call(yAxis);


    const cell = svg.append("g")
      .attr('class', 'gCell')
      .selectAll("g")
      .data(d3.cross(d3.range(columns.length), d3.range(columns.length)))
      .join("g")
        .attr("transform", ([i, j]) => 'translate(' + i * size +',' + j * size +')');

    // show rect border
    cell.append("rect")
        .attr("fill", "none")
        .attr("stroke", "#aaa")
        .attr("x", padding / 2 + 0.5)
        .attr("y", padding / 2 + 0.5)
        .attr("width", size - padding)
        .attr("height", size - padding);

    let t_duration = 1000

    // draw circles in each cell
    cell.each(function([i, j]) {
      d3.select(this).selectAll("circle")
        .data(data)
        .join("circle")
        .attr('cx', size/2)
        .attr('cy', size/2)
        .transition().duration(t_duration)
          .attr("cx", function (d) {
            return x[i](d[columns[i]])
          })
          .attr("cy", d => y[j](d[columns[j]]))
    });

    // animation to draw grid lines
    g_xAxis
        .transition().duration(t_duration + 50)
        .on('end', function() { // https://github.com/d3/d3-transition/blob/v1.2.0/README.md#control-flow
          d3.select(this).selectAll('.tick line')
            .transition().duration(t_duration * 2)
            .attr('y1', 0)
        })
    g_yAxis
        .transition().duration(t_duration+ 50)
        .on('end', function() {
          d3.select(this).selectAll('.tick line')
            .transition().duration(t_duration * 2)
            .attr('x2', size * columns.length)
        })

    svg.append("g")
        .style("font", "bold 10px sans-serif")
        .style("pointer-events", "none")
      .selectAll("text")
      .data(columns)
      .join("text")
        .attr("transform", (d, i) => `translate(${i * size},${i * size})`)
        .attr("x", padding)
        .attr("y", padding)
        .attr("dy", ".71em")
        .text(d => d);

    const circle = cell.selectAll("circle")
        .attr("r", 3.5)
        .attr("fill-opacity", 0.7)
        .attr("fill", d => z(d['Species']));
    
    // brush
    cell.call(brush, circle);
    function brush(cell, circle) {
      const brush = d3.brush()
          .extent([[padding / 2, padding / 2], [size - padding / 2, size - padding / 2]])
          .on("start", brushstarted)
          .on("brush", brushed)
          .on("end", brushended);

      cell.call(brush);

      let brushCell;

      // Clear the previously-active brush, if any.
      function brushstarted() {
        if (brushCell !== this) {
          d3.select(brushCell).call(brush.move, null);
          brushCell = this;
        }
      }

      // Highlight the selected circles.
      function brushed([i, j]) {
        if (d3.event.selection === null) return;
        const [[x0, y0], [x1, y1]] = d3.event.selection; 
        circle.classed("hidden", d => {
          return x0 > x[i](d[columns[i]])
              || x1 < x[i](d[columns[i]])
              || y0 > y[j](d[columns[j]])
              || y1 < y[j](d[columns[j]]);
        });
      }

      // If the brush is empty, select all circles.
      function brushended([i, j]) {
        if (d3.event.selection !== null) {
          const [[x0, y0], [x1, y1]] = d3.event.selection;
          
          // print and save the selected data
          let selected_data = data.filter(d => {
            // todo[1]
          });
          console.log("selected-data", selected_data);

          // use the selected data to draw a bar chart
          draw_barchart(selected_data)
          return;
        }
        circle.classed("hidden", false);
      }
    }
})

function draw_barchart(selected_data) {
  var barchartSvg = d3.select('#barchart-svg')
  // todo[2]
}
