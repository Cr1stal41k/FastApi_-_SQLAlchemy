data_value = {
  "inputs": [
    {
      "name": "24-2000:TI56.T",
      "points": [
        {
          "d": "2023-02-20T02:33:44",
          "v": 372.76608
        },
        {
          "d": "2023-02-20T03:34:49",
          "v": 372.80273
        },
        {
          "d": "2023-02-20T04:32:59",
          "v": 372.43652
        }
      ]
    },
    {
      "name": "24-2000:FI3110.F",
      "points": [
        {
          "d": "2023-02-20T02:37:42.13238",
          "v": 98999.06789
        },
        {
          "d": "2023-02-20T03:38:28.065364",
          "v": 99315.40678
        },
        {
          "d": "2023-02-20T04:39:13.739708",
          "v": 98948.80312
        }
      ]
    }
  ],
  "outputs": [
    {
      "name": "FI0111.F:CalcFact",
      "points": [
        {
          "d": "2023-02-20T04:39:13.739708",
          "v": 9848.60529
        },
        {
          "d": "2023-02-20T03:38:28.065364",
          "v": 9848.60529
        },
        {
          "d": "2023-02-20T02:37:42.13238",
          "v": 9848.60529
        }
      ]
    }
  ]
}

inputs = data_value['inputs']
outputs = data_value['outputs']
print(inputs)
points_inputs = inputs[1]['points']
grafana_value = []
print(points_inputs)

result_form = {
    'name': '',
    'd': '',
    'v': ''
}

for model in inputs:
    result_form.update(name=model['name'])
    grafana_value.append(result_form)
print(grafana_value)


# for model in inputs:
#     form = {}
#     form['name'] = (model['name'])
#     grafana_value.append(form)
#     print(model)
#     # for i in model:
#     #     form['d'] = i['points']
#     #     grafana_value.append(form)
# print(grafana_value)


# for i in range(0, len(inputs)):
#     result_form = {
#         'name': '',
#         'd': '',
#         'v': ''
#     }
#     result_form.update(name=inputs[i]['name'])
#     for a in range(0, len(inputs[i]['points'])):
#         result_form.update(d=inputs[i]['points'][a]['d'])
#         result_form.update(v=inputs[i]['points'][a]['v'])
#         grafana_value.append(result_form)
#
# for i in range(0, len(outputs)):
#     result_form = {
#         'name': '',
#         'd': '',
#         'v': ''
#     }
#     result_form.update(name=outputs[i]['name'])
#     for a in range(0, len(outputs[i]['points'])):
#         result_form.update(d=outputs[i]['points'][a]['d'])
#         result_form.update(v=outputs[i]['points'][a]['v'])
#         grafana_value.append(result_form)
# print(grafana_value)