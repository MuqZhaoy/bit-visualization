import * as d3 from 'd3';

var choroplethData = [];

function loadData(choroplethDataCallback) {
    d3.csv('./mbti-countries.csv', d => ({
        Country: d.Country,
        ESTJ_A: +d['ESTJ-A'],
        ESFJ_A: +d['ESFJ-A'],
        INFP_T: +d['INFP-T'],
        ESFJ_T: +d['ESFJ-T'],
        ENFP_T: +d['ENFP-T'],
        ENFP_A: +d['ENFP-A'],
        ESTJ_T: +d['ESTJ-T'],
        ISFJ_T: +d['ISFJ-T'],
        ENFJ_A: +d['ENFJ-A'],
        ESTP_A: +d['ESTP-A'],
        ISTJ_A: +d['ISTJ-A'],
        INTP_T: +d['INTP-T'],
        INFJ_T: +d['INFJ-T'],
        ISFP_T: +d['ISFP-T'],
        ENTJ_A: +d['ENTJ-A'],
        ESTP_T: +d['ESTP-T'],
        ISTJ_T: +d['ISTJ-T'],
        ESFP_T: +d['ESFP-T'],
        ENTP_A: +d['ENTP-A'],
        ESFP_A: +d['ESFP-A'],
        INTJ_T: +d['INTJ-T'],
        ISFJ_A: +d['ISFJ-A'],
        INTP_A: +d['INTP-A'],
        ENTP_T: +d['ENTP-T'],
        ISTP_T: +d['ISTP-T'],
        ENTJ_T: +d['ENTJ-T'],
        ISTP_A: +d['ISTP-A'],
        INFP_A: +d['INFP-A'],
        ENFJ_T: +d['ENFJ-T'],
        INTJ_A: +d['INTJ-A'],
        ISFP_A: +d['ISFP-A'],
        INFJ_A: +d['INFJ-A'],
    })).then(function(d) {
        choroplethData = JSON.parse(JSON.stringify(d));
        if (typeof choroplethDataCallback === 'function') {
            choroplethDataCallback();
        }
    }).catch(error => {
        console.error("Error loading the CSV file: ", error);
    });
}

function getChoroplethData() {
    return choroplethData;
}

export default {
    loadData,
    getChoroplethData
};
