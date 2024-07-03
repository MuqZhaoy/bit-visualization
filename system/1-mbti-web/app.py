# -*- coding: utf-8 -*-


from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__)

@app.route('/')
def index():
    
    
    # 读取数据
    df = pd.read_csv("resources/mbti_dimensions.csv")

    # 创建世界地图
    fig = px.choropleth(df, locations='Country', locationmode='country names',
                        color='E', hover_name='Country',
                        color_continuous_scale=px.colors.sequential.Oranges)
    graph_html_map_e = fig.to_html(full_html=False)

    fig = px.choropleth(df, locations='Country', locationmode='country names',
                        color='P', hover_name='Country',
                        color_continuous_scale=px.colors.sequential.Blues)
    graph_html_map_p = fig.to_html(full_html=False)

    fig = px.choropleth(df, locations='Country', locationmode='country names',
                        color='S', hover_name='Country',
                        color_continuous_scale=px.colors.sequential.Greens)
    graph_html_map_s = fig.to_html(full_html=False)

    fig = px.choropleth(df, locations='Country', locationmode='country names',
                        color='F', hover_name='Country',
                        color_continuous_scale=px.colors.sequential.Reds)
    graph_html_map_f = fig.to_html(full_html=False)


    # 数据
    types = ["ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "ESFP", "ESTJ", "ESTP",
            "INFJ", "INFP", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"]
    sizes = [1333, 4630, 1561, 4566, 298, 271, 261, 562, 10289, 12422, 7237, 8650, 1120, 1678, 1360, 2150]

    # 日本传统色卡颜色代码（可根据需要添加更多颜色）
    colors = [
    '#E60026', '#F68B1F', '#9B1B30', '#A22041', '#990000', '#F75C2F', '#E83929', '#F1908C',  # 红色调
    '#0F4C81', '#3A5BDB', '#165E83', '#265DAB', '#81C7D4', '#2792C3', '#4A5EAA', '#282828'   # 蓝色调
    ]

    # 创建树图
    fig = go.Figure(go.Treemap(
    labels=types,
    parents=[''] * len(types),
    values=sizes,
    marker=dict(
        colors=colors,
        line=dict(width=1, color='black')
    )))
    graph_html_rose = fig.to_html(full_html = False);


   # 定义颜色
    colors = [
        ['#E60026', '#0F4C81'], ['#9B1B30', '#165E83'], ['#990000', '#81C7D4'], ['#E83929', '#4A5EAA'],  # 第一组，红蓝搭配
        ['#F68B1F', '#3A5BDB'], ['#A22041', '#265DAB'], ['#F75C2F', '#2792C3'], ['#F1908C', '#4A5EAA'] ,  # 第二组，红蓝搭配
        ['#E60026', '#0F4C81'], ['#9B1B30', '#165E83'], ['#990000', '#81C7D4'], ['#E83929', '#4A5EAA'],  # 第三组，重复第一组
        ['#F68B1F', '#3A5BDB'], ['#A22041', '#265DAB'], ['#F75C2F', '#2792C3'], ['#F1908C', '#4A5EAA']    # 第四组，重复第二组
    ]


    # 定义类型和数据
    types = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
            'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']
    positive = [7028, 24129, 7400, 22189, 1557, 1482, 1321, 2809,
                29918, 17112, 23191, 22762, 5781, 9243, 6468, 10298]
    passive = [4037, 14733, 5857, 17197, 857, 1000, 911, 2121,
            19714, 11638, 18566, 19535, 3536, 5774, 4719, 8353]

    # 创建子图
    fig = make_subplots(rows=4, cols=4, subplot_titles=types, specs=[[{'type': 'domain'}]*4]*4)

    for i in range(4):
        for j in range(4):
            index = i * 4 + j
            fig.add_trace(go.Pie(labels=['Positive', 'Passive'],
                                values=[positive[index], passive[index]],
                                hole=0.3,
                                marker=dict(colors=colors[index])),
                        row=i+1, col=j+1)

    # 设置布局
    fig.update_layout(
        height=800,
        width=800,
        showlegend=False
    )

    graph_html_circle = fig.to_html(full_html=False)

    # 数据
    types = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']
    rates = [1.740896705, 1.637751985, 1.26344545, 1.290283189, 1.8168028, 1.482, 1.450054885, 1.324375295, 1.517601704, 1.470355731, 1.249111279, 1.165190683, 1.63489819, 1.600796675, 1.370629371, 1.232850473]

    # 创建南丁格尔玫瑰图
    fig = go.Figure(go.Barpolar(
        r=rates,
        theta=types,
        marker=dict(
            color=rates,
            colorscale='Viridis'
        )
    ))

    # 设置布局
    fig.update_layout(
        polar=dict(
            radialaxis=dict(showticklabels=False, ticks=''),
        ),
        showlegend=False
    )

    # 生成HTML
    graph_html_nightingale = fig.to_html(full_html=False)

    # 数据准备
    data = {
        'word': [
            "like", "think", "people", "really", "know", "get", "feel", "infp", "love",
            "want", "time", "good", "always", "things", "could", "even", "say",
            "something", "see", "never", "lot", "someone", "way", "make", "find",
            "go", "ca", "going", "me.", "pretty", ":)", "actually", "first", "need",
            "life", "got", "thing", "still", "type", "many", "well", "right", "sure",
            "thought", "person", "sometimes", "i...", "kind", "take", "maybe", "friends",
            "little", "probably", "try", "read", "best", "around", "the...", "...", "makes",
            "me,", "though", "friend", "look", "ever", "thank", "back", "might", "since",
            "work", "feeling", "two", "usually", "seems", "quite", "infps", "years",
            "every", "different", "long", "hard", "said", "trying", "to...", "world",
            "used", "made", "definitely", "seem", "come", "may", "and...", "everyone",
            "understand", "bit", "new", "last", "it,", "anything", "better"
        ],
        'frequency': [
            13985, 10182, 8377, 7776, 6649, 6061, 5932, 4675, 4665, 4035, 3825, 3795,
            3672, 3454, 3431, 3364, 3329, 3316, 3306, 3192, 3188, 3019, 2963, 2953,
            2775, 2735, 2708, 2531, 2517, 2457, 2454, 2313, 2276, 2172, 2139, 2120,
            2113, 2105, 2092, 2076, 2075, 1976, 1965, 1947, 1885, 1880, 1869, 1857,
            1838, 1835, 1833, 1799, 1787, 1784, 1747, 1734, 1723, 1668, 1664, 1653,
            1630, 1625, 1592, 1567, 1560, 1558, 1557, 1552, 1551, 1544, 1540, 1530,
            1528, 1525, 1524, 1496, 1494, 1482, 1452, 1443, 1438, 1434, 1413, 1413,
            1400, 1388, 1384, 1357, 1340, 1335, 1324, 1324, 1323, 1319, 1313, 1308,
            1306, 1305, 1266, 1259
        ]
    }

    df = pd.DataFrame(data)

    # 创建词云
    fig = px.treemap(df, path=[px.Constant('all'), 'word'], values='frequency',
                    color='frequency', hover_data=['word'],
                    color_continuous_scale='Viridis',
    )

    # 调整布局
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    # 生成HTML
    graph_html_wordcloud = fig.to_html(full_html=False)


    # 最后渲染
    return render_template('index.html', graph_html_map_e=graph_html_map_e, graph_html_map_p = graph_html_map_p, graph_html_map_f = graph_html_map_f, graph_html_map_s = graph_html_map_s,
                           graph_html_rose = graph_html_rose,graph_html_circle=graph_html_circle,graph_html_nightingale = graph_html_nightingale,graph_html_wordcloud=graph_html_wordcloud)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
