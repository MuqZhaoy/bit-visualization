import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 读取数据
df = pd.read_csv('E:\\MuqZhaoy\\bit-visualization\\treemap\\csv\\ENFJ.csv')

# 初始化 Dash 应用程序
app = dash.Dash(__name__)

# 创建初始树图
fig = px.treemap(df, path=['MBTI', 'Level1', 'Level2', 'level3'], values='Value', title='MBTI Personality Emotions Analysis')

# 定义应用程序布局
app.layout = html.Div([
    html.H1('MBTI Personality Emotions Analysis'),
    dcc.Graph(id='treemap', figure=fig)
])

# 回调函数更新图表
@app.callback(
    Output('treemap', 'figure'),
    [Input('treemap', 'clickData')]
)
def update_treemap(clickData):
    if clickData:
        clicked_path = clickData['points'][0]['label'].split('/')
        if len(clicked_path) == 1:
            filtered_df = df[df['MBTI'] == clicked_path[0]]
            return px.treemap(filtered_df, path=['Level1', 'Level2', 'level3'], values='Value', title=f"{clicked_path[0]} Emotions")
        elif len(clicked_path) == 2:
            filtered_df = df[(df['MBTI'] == clicked_path[0]) & (df['Level1'] == clicked_path[1])]
            return px.treemap(filtered_df, path=['Level2', 'level3'], values='Value', title=f"{clicked_path[0]} - {clicked_path[1]} Emotions")
        elif len(clicked_path) == 3:
            filtered_df = df[(df['MBTI'] == clicked_path[0]) & (df['Level1'] == clicked_path[1]) & (df['Level2'] == clicked_path[2])]
            return px.treemap(filtered_df, path=['level3'], values='Value', title=f"{clicked_path[0]} - {clicked_path[1]} - {clicked_path[2]} Emotions")
    return px.treemap(df, path=['MBTI', 'Level1', 'Level2', 'Level3'], values='Value', title='MBTI Personality Emotions Analysis')

if __name__ == '__main__':
    app.run_server(debug=True)
