<template>
    <div id='choropleth'>
        <div id='selectSection'>
            <select name="category" id="category" style="display:none">
                <option value="ESTJ_A">ESTJ-A</option>
                <option value="ESFJ_A">ESFJ-A</option>
                <option value="INFP_T">INFP-T</option>
                <option value="ESFJ_T">ESFJ-T</option>
                <option value="ENFP_T">ENFP-T</option>
                <option value="ENFP_A">ENFP-A</option>
                <option value="ESTJ_T">ESTJ-T</option>
                <option value="ISFJ_T">ISFJ-T</option>
                <option value="ENFJ_A">ENFJ-A</option>
                <option value="ESTP_A">ESTP-A</option>
                <option value="ISTJ_A">ISTJ-A</option>
                <option value="INTP_T">INTP-T</option>
                <option value="INFJ_T">INFJ-T</option>
                <option value="ISFP_T">ISFP-T</option>
                <option value="ENTJ_A">ENTJ-A</option>
                <option value="ESTP_T">ESTP-T</option>
                <option value="ISTJ_T">ISTJ-T</option>
                <option value="ESFP_T">ESFP-T</option>
                <option value="ENTP_A">ENTP-A</option>
                <option value="ESFP_A">ESFP-A</option>
                <option value="INTJ_T">INTJ-T</option>
                <option value="ISFJ_A">ISFJ-A</option>
                <option value="INTP_A">INTP-A</option>
                <option value="ENTP_T">ENTP-T</option>
                <option value="ISTP_T">ISTP-T</option>
                <option value="ENTJ_T">ENTJ-T</option>
                <option value="ISTP_A">ISTP-A</option>
                <option value="INFP_A">INFP-A</option>
                <option value="ENFJ_T">ENFJ-T</option>
                <option value="INTJ_A">INTJ-A</option>
                <option value="ISFP_A">ISFP-A</option>
                <option value="INFJ_A">INFJ-A</option>
            </select>
            <button @click="onGenerate">生成</button>
        </div>
        <div id="choropleth-graph"></div>
        <div id="tooltip"></div>
    </div>
</template>

<script>
import * as d3 from 'd3';
import dataModule from './js/global.data.js';  // 确保路径正确

var svg, g;
var projection;
var zoom;
var path;
var width = 1200,
    height = 600;
var tooltip;
var rawData = [],
    data = [];
var dataMap = new Map();
var color;

function procData(category) {
    data = rawData.map(d => ({
        name: d.Country,
        value: d[category]
    }));
    for (let i = 0; i < data.length; i++) {
        dataMap.set(data[i].name, data[i].value);
    }
}

var mouseMove = function(e) {
    tooltip
        .style('left', (e.pageX + 15) + 'px')
        .style('top', (e.pageY - 35) + 'px');
};

function zoomed(event) {
    const { transform } = event;
    g.attr("transform", transform);
    g.attr("stroke-width", 1 / transform.k);
}

export default {
    name: 'ChoroplethMap',
    created() {

    },
    mounted() {
        // The svg
        svg = d3.select('#choropleth-graph')
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            .on('mousemove', mouseMove);

        tooltip = d3.select('#tooltip')
            .style('display', 'none');

        projection = d3.geoMercator()
            .scale(160)
            .center([0, 20])
            .translate([width / 2, height / 2]);

        path = d3.geoPath(projection);
        
        zoom = d3.zoom()
            .scaleExtent([1, 8])
            .on("zoom", zoomed);

        // 初始化数据
        dataModule.loadData(() => {
            rawData = dataModule.getChoroplethData();
        });
    },
    methods: {
        draw() {
            // 消除全部地图会闪动
            d3.select("#choropleth-graph").selectAll("g").remove();

            let mouseOver = function(e) {
                d3.selectAll(".Country")
                    .transition()
                    .duration(200)
                    .style("opacity", .5);
                d3.select(e.toElement)
                    .transition()
                    .duration(200)
                    .style("opacity", 1)
                    .style("stroke", "#808080")
                    .style("fill","rgb(244,164,96)")
                tooltip.style('display', 'block');
                let cid = e.toElement.id;

				let country = rawData.find(function(item) {
                    return item.Country == cid;
                });
                if (typeof(country) === 'undefined') {
                    country = {
                        name: cid,
                        value: 0,
                        ESTJ_A: 0,
                        ESFJ_A: 0,
                        INFP_T: 0,
                        ESFJ_T: 0,
                        ENFP_T: 0,
                        ENFP_A: 0,
                        ESTJ_T: 0,
                        ISFJ_T: 0,
                        ENFJ_A: 0,
                        ESTP_A: 0,
                        ISTJ_A: 0,
                        INTP_T: 0,
                        INFJ_T: 0,
                        ISFP_T: 0,
                        ENTJ_A: 0,
                        ESTP_T: 0,
                        ISTJ_T: 0,
                        ESFP_T: 0,
                        ENTP_A: 0,
                        ESFP_A: 0,
                        INTJ_T: 0,
                        ISFJ_A: 0,
                        INTP_A: 0,
                        ENTP_T: 0,
                        ISTP_T: 0,
                        ENTJ_T: 0,
                        ISTP_A: 0,
                        INFP_A: 0,
                        ENFJ_T: 0,
                        INTJ_A: 0,
                        ISFP_A: 0,
                        INFJ_A: 0
                    };
                }
                let text = `${country.Country}\n`;
                let personalitiesType = [];
                for (let key in country ) {
                    if (key !== 'Country') {
                        personalitiesType.push({
                            type: key,
                            value: country[key]*100
                        });
                    }
                }
                personalitiesType.sort(function(a, b) {
                    return b.value - a.value;
                });
                let topThreePersonType = personalitiesType.slice(0, 3);
                topThreePersonType.forEach((personalitiesType,index)=>{
                    text += `${index+1}. ${personalitiesType.type}: ${personalitiesType.value}%\n`;
                })
                tooltip.text(text);
            };

            let mouseLeave = function(e) {
                d3.selectAll(".Country")
                    .transition()
                    .duration(200)
                    .style("opacity", .5)
                    .style("fill",null)        
                    .style("stroke", "#808080");
                e.fromElement.style.setProperty('stroke', 'transparent');
                tooltip.style('display', 'none');
            };

            d3.json("world.geojson").then(function(topo) {
                //等比例
                color = d3.scaleSequential()
                    .domain(d3.extent(Array.from(dataMap.values())))
                    .interpolator(d3.interpolateYlGnBu)
                    .unknown("#ccc");
                // 7挡阈值
                color = d3.scaleThreshold()
                    .range(d3.schemeOranges[7]);
                g = svg.append("g");
                g
                    .selectAll("path")
                    .data(topo.features)
                    .enter()
                    .append("path")
                    .attr("d", path)
                    .attr("fill", function(d) {
                        d.total = dataMap.get(d.properties.name) || 0;
                        return color(d.total);
                    })
                    .style("stroke", "#808080")
                    .attr("class", "Country")
                    .attr("id", d => d.properties.name)
                    .style("opacity", 1)
                    .on("mouseover", mouseOver)
                    .on("mouseleave", mouseLeave);
                
                svg.call(zoom);
            });
        },
        onGenerate() {
            let category = d3.select(this.$el)
                .select('#category').node().value;
            procData(category);
            this.draw();
        }
    }
};
</script>

<style>
#tooltip {
    color: white;
    background-color: black;
    padding: .5em;
    border-radius: 3px;
    position: absolute;
    font-size: 0.9375rem;
    white-space: pre-line;
    text-align: left;
}
#choropleth {
    text-align: center;
}
</style>
