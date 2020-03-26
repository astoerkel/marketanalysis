import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ]
)

app.layout = html.Div(
    html.Div([
        html.Div(

            [
                html.H2(children='Market Insights and Candidate Pipeline',
                        className='six columns',
                        style={'marginBottom': 50, 'marginTop': 25, 'font-family': 'Helvetica Neue',
                               'color': '#50a864'})
            ]
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.H4('LinkedIn & ATS Data ')

                    ],
                    className='twelve columns',
                    style={'margin-top': '50', 'marginBottom': 50, 'font-family': 'Helvetica Neue',
                           'color': '#50a864'}
                ),
            ], className="row"
        ),

        html.Div(
            [
                dcc.Tabs([
                    dcc.Tab(label='Candidate Pipeline', children=[
                        html.Div('Choose Candidate Source:', style={'marginBottom': 0, 'marginTop': 100}),
                        dcc.Checklist(
                            id='Source',
                            options=[
                                {'label': 'Internal', 'value': 'int'},
                                {'label': 'External', 'value': 'ext'}
                            ],
                            value=['int', 'ext'],
                            labelStyle={'display': 'inline-block'},
                            style={'marginBottom': 25, 'marginTop': 0}
                        ),

                        html.Div([
                            dcc.Graph(
                                id="candidate_pipeline",
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [4, 1, 2],
                                         'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [2, 4, 5],
                                         'type': 'bar', 'name': u'Montréal'},
                                    ],
                                    'layout': {
                                        'title': {'text': 'Pipeline 1'}
                                    }
                                },
                                className='six columns',
                                style={'marginBottom': 50, 'marginTop': 25}
                            ),
                            dcc.Graph(
                                id="candidate_pipeline_poland",
                                figure={
                                    'data': [
                                        {'x': [1, 2, 3], 'y': [1, 4, 1],
                                         'type': 'bar', 'name': 'SF'},
                                        {'x': [1, 2, 3], 'y': [1, 2, 3],
                                         'type': 'bar', 'name': u'Montréal'},
                                    ],
                                    'layout': {
                                        'title': {'text': 'Pipeline 2'}
                                    }

                                },
                                className='six columns'
                            ),
                            html.Hr()
                        ]),
                        html.Hr(),
                        html.Center(
                            html.Div([
                                html.Div([
                                    html.Br(),
                                    html.Hr(),

                                    dcc.Graph(
                                        id="linkedinpool",
                                        figure={
                                            'data': [
                                                {'x': ['Product Expertise', 'Seniority', 'Industry',
                                                       'Currently in Poland', 'Open to Opportunities'],
                                                 'y': [1762118, 837922, 176304, 139, 20], 'type': 'bar',
                                                 'mode': "lines+markers+text", 'textinfo': 'value',
                                                 'textposition': 'outside',
                                                 'hoverinfo': '', 'name': 'Candidates on LinkedIn',
                                                 "marker": {"color": "#c7d456"}, 'width': 0.5}
                                            ],
                                            'layout': go.Layout(
                                                bargap=0.01,
                                                bargroupgap=0.03,
                                                barmode="group",
                                                showlegend=True,
                                                height=500
                                            )
                                        },
                                        className='twelve columns'
                                    )
                                ])
                            ])

                        )
                    ]),

                    dcc.Tab(label='LinkedIn InMail Stats', children=[
                        html.Br(),
                        dcc.Graph(
                            id="linkedin_inmail_stats",
                            figure={
                                'data': [
                                    {'x': ['InMails Sent', 'Accepted', 'Declined', 'No Response'], 'y': [1, 4, 1, 5],
                                     'type': 'bar', 'name': 'SF'},
                                    {'x': ['InMails Sent', 'Accepted', 'Declined', 'No Response'], 'y': [1, 2, 3, 6],
                                     'type': 'bar', 'name': u'Montréal'},
                                ],
                                'layout': {
                                    'title': {'text': 'InMail Stats'}
                                }

                            },
                            className='six columns'
                        )

                    ]),
                    dcc.Tab(label='Data ', children=[
                        html.Br(),
                        html.Center([
                            html.H5(children='Pipeline 1'),
                            html.Br(),
                            dcc.Input(id='Role', type='text', placeholder='Role Name', persistence=True),
                            dcc.Input(id='ReviewInt', type='number', placeholder='Review Int', persistence=True),
                            dcc.Input(id='ReviewExt', type='number', placeholder='Review Ext', persistence=True),
                            dcc.Input(id='ScreenInt', type='number', placeholder='Screen Int', persistence=True),
                            dcc.Input(id='ScreenExt', type='number', placeholder='Screen Ext', persistence=True),
                            html.Br(),
                            dcc.Input(id='CaseInt', type='number', placeholder='Case Int', persistence=True),
                            dcc.Input(id='CaseExt', type='number', placeholder='Case Ext', persistence=True),
                            dcc.Input(id='FinalInt', type='number', placeholder='Final Int', persistence=True),
                            dcc.Input(id='FinalExt', type='number', placeholder='Final Ext', persistence=True),
                            dcc.Input(id='OfferInt', type='number', placeholder='Offer Int', persistence=True),
                            dcc.Input(id='OfferExt', type='number', placeholder='Offer Ext', persistence=True),
                            html.Br(),
                            html.Br(),
                            html.Hr(),
                            html.Br(),
                            html.H5(children='Pipeline 2'),
                            html.Br(),
                            dcc.Input(id='Role1', type='text', placeholder='Role Name', persistence=True),
                            dcc.Input(id='ReviewInt1', type='number', placeholder='Review Int', persistence=True),
                            dcc.Input(id='ReviewExt1', type='number', placeholder='Review Ext', persistence=True),
                            dcc.Input(id='ScreenInt1', type='number', placeholder='Screen Int', persistence=True),
                            dcc.Input(id='ScreenExt1', type='number', placeholder='Screen Ext', persistence=True),
                            html.Br(),
                            dcc.Input(id='CaseInt1', type='number', placeholder='Case Int', persistence=True),
                            dcc.Input(id='CaseExt1', type='number', placeholder='Case Ext', persistence=True),
                            dcc.Input(id='FinalInt1', type='number', placeholder='Final Int', persistence=True),
                            dcc.Input(id='FinalExt1', type='number', placeholder='Final Ext', persistence=True),
                            dcc.Input(id='OfferInt1', type='number', placeholder='Offer Int', persistence=True),
                            dcc.Input(id='OfferExt1', type='number', placeholder='Offer Ext', persistence=True),
                            html.Br(),
                            html.Br(),
                            html.Hr(),
                            html.Br(),
                            html.H5(children='LinkedIn Stats'),
                            html.Br(),
                            dcc.Input(id='Criteria1', value='Criteria 1', type='text', placeholder='Criteria 1',
                                      persistence=True),
                            dcc.Input(id='Criteria2', value='Criteria 2', type='text', placeholder='Criteria 2',
                                      persistence=True),
                            dcc.Input(id='Criteria3', value='Criteria 3', type='text', placeholder='Criteria 3',
                                      persistence=True),
                            dcc.Input(id='Criteria4', value='Criteria 4', type='text', placeholder='Criteria 4',
                                      persistence=True),
                            dcc.Input(id='Criteria5', value='Criteria 5', type='text', placeholder='Criteria 5',
                                      persistence=True),
                            html.Br(),
                            dcc.Input(id='Pool1', type='number', placeholder='No of Profiles', persistence=True),
                            dcc.Input(id='Pool2', type='number', placeholder='No of Profiles', persistence=True),
                            dcc.Input(id='Pool3', type='number', placeholder='No of Profiles', persistence=True),
                            dcc.Input(id='Pool4', type='number', placeholder='No of Profiles', persistence=True),
                            dcc.Input(id='Pool5', type='number', placeholder='No of Profiles', persistence=True),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Hr(),
                            html.Br(),
                            html.H5(children='LinkedIn Inmails'),
                            html.Br(),
                            dcc.Input(id='Sent', type='number', placeholder='Sent', persistence=True),
                            dcc.Input(id='Accepted', type='number', placeholder='Accepted', persistence=True),
                            dcc.Input(id='Declined', type='number', placeholder='Declined', persistence=True),
                            dcc.Input(id='Noresponse', type='number', placeholder='No Response', persistence=True)
                        ])
                    ]),
                ])
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)


@app.callback(
    dash.dependencies.Output('linkedin_inmail_stats', 'figure'),
    [dash.dependencies.Input('Sent', 'value'),
     dash.dependencies.Input('Accepted', 'value'),
     dash.dependencies.Input('Declined', 'value'),
     dash.dependencies.Input('Noresponse', 'value')])
def update_image_src(Sent, Accepted, Declined, Noresponse):
    data = []

    figure = {
        'data': [
            {'x': ['InMails Sent', 'Accepted', 'Declined', 'No Response'], 'y': [Sent, Accepted, Declined, Noresponse],
             'type': 'bar', 'width': [0.4, 0.4, 0.4, 0.4, 0.4], 'text': [Sent, Accepted, Declined, Noresponse],
             'textposition': 'outside', 'name': 'LinkedIn InMails',
             'mode': 'markers+text',
             "marker": {"color": "#b5fca9", 'size': 12}}],
        'layout':
            go.Layout(

                bargroupgap=0.03,
                barmode="group",
                showlegend=True,
                title=go.layout.Title(text='LinkedIn InMails'),
                height=500

            )
    }
    return figure


@app.callback(
    dash.dependencies.Output('linkedinpool', 'figure'),
    [dash.dependencies.Input('Criteria1', 'value'),
     dash.dependencies.Input('Criteria2', 'value'),
     dash.dependencies.Input('Criteria3', 'value'),
     dash.dependencies.Input('Criteria4', 'value'),
     dash.dependencies.Input('Criteria5', 'value'),
     dash.dependencies.Input('Pool1', 'value'),
     dash.dependencies.Input('Pool2', 'value'),
     dash.dependencies.Input('Pool3', 'value'),
     dash.dependencies.Input('Pool4', 'value'),
     dash.dependencies.Input('Role1', 'value'),
     dash.dependencies.Input('Pool5', 'value')])
def update_image_src(Criteria1, Criteria2, Criteria3, Criteria4, Criteria5, Pool1, Pool2, Pool3, Pool4, Role1, Pool5):
    data = []

    figure = {
        'data': [
            {'x': [Criteria1, Criteria2, Criteria3, Criteria4, Criteria5], 'y': [Pool1, Pool2, Pool3, Pool4, Pool5],
             'type': 'bar', 'width': [0.4, 0.4, 0.4, 0.4, 0.4], 'text': [Pool1, Pool2, Pool3, Pool4, Pool5],
             'textposition': 'outside', 'texttemplate': '%{text:.2s}', 'name': 'LinkedIn Pool', 'mode': 'markers+text',
             "marker": {"color": "#b5fca9", 'size': 12}}],
        'layout':
            go.Layout(
                bargap=0.01,
                bargroupgap=0.03,
                barmode="group",
                showlegend=True,
                title=go.layout.Title(text='LinkedIn Pool'),
                height=500

            )
    }
    return figure


@app.callback(
    dash.dependencies.Output('candidate_pipeline', 'figure'),
    [dash.dependencies.Input('Source', 'value'),
     dash.dependencies.Input('ReviewInt1', 'value'),
     dash.dependencies.Input('ReviewExt1', 'value'),
     dash.dependencies.Input('ScreenInt1', 'value'),
     dash.dependencies.Input('ScreenExt1', 'value'),
     dash.dependencies.Input('CaseInt1', 'value'),
     dash.dependencies.Input('CaseExt1', 'value'),
     dash.dependencies.Input('FinalInt1', 'value'),
     dash.dependencies.Input('FinalExt1', 'value'),
     dash.dependencies.Input('OfferInt1', 'value'),
     dash.dependencies.Input('Role1', 'value'),
     dash.dependencies.Input('OfferExt1', 'value')])
def update_image_src(selector, reviewint1, reviewext1, screenint1, screenext1, caseint1, caseext1, finalint1, finalext1,
                     offerint1, role1, offerext1):
    data = []
    if 'int' in selector:
        data.append({'x': ['Review', 'Screen', 'HM Interview', 'Case & Panel Interview', 'Offer'],
                     'y': [reviewint1, screenint1, caseint1, finalint1, offerint1], 'type': 'bar',
                     'name': 'Internal Candidates', "marker": {"color": "#50a864"}})
    if 'ext' in selector:
        data.append({'x': ['Review', 'Screen', 'HM Interview', 'Case & Panel Interview', 'Offer'],
                     'y': [reviewext1, screenext1, caseext1, finalext1, offerext1], 'type': 'bar',
                     'name': u'External Candidates', "marker": {"color": "#b5fca9"}})
    figure = {
        'data': data,
        'layout': {
            'title': role1,
            'xaxis': dict(
                title='Stages',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'

                )),
            'yaxis': dict(
                title='Candidates in Process',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


@app.callback(
    dash.dependencies.Output('candidate_pipeline_poland', 'figure'),
    [dash.dependencies.Input('Source', 'value'),
     dash.dependencies.Input('ReviewInt', 'value'),
     dash.dependencies.Input('ReviewExt', 'value'),
     dash.dependencies.Input('ScreenInt', 'value'),
     dash.dependencies.Input('ScreenExt', 'value'),
     dash.dependencies.Input('CaseInt', 'value'),
     dash.dependencies.Input('CaseExt', 'value'),
     dash.dependencies.Input('FinalInt', 'value'),
     dash.dependencies.Input('FinalExt', 'value'),
     dash.dependencies.Input('OfferInt', 'value'),
     dash.dependencies.Input('Role', 'value'),
     dash.dependencies.Input('OfferExt', 'value')])
def update_image_src(selector, reviewint, reviewext, screenint, screenext, caseint, caseext, finalint, finalext,
                     offerint, role, offerext):
    data = []
    if 'int' in selector:
        data.append({'x': ['Review', 'Screen', 'HM Interview', 'Case & Panel Interview', 'Offer'],
                     'y': [reviewint, screenint, caseint, finalint, offerint], 'type': 'bar',
                     'name': 'Internal Candidates', "marker": {"color": "#50a864"}})
    if 'ext' in selector:
        data.append({'x': ['Review', 'Screen', 'HM Interview', 'Case & Panel Interview', 'Offer'],
                     'y': [reviewext, screenext, caseext, finalext, offerext], 'type': 'bar',
                     'name': u'External Candidates', "marker": {"color": "#b5fca9"}})

    figure = {
        'data': data,
        'layout': {
            'title': {'text': role},
            'xaxis': dict(
                title='Stages',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='Candidates in Process',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
