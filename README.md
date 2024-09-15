# holdable-plotly

## USAGE
```python
import pandas as pd
import plotly.express as px
df = px.data.iris()
df.index.name="index"
df["information"] = df.apply(lambda x:pd.DataFrame([x]).to_html(),axis=1)
fig = px.scatter(df,x="sepal_length",y="sepal_width", color="species",
                 custom_data=["information"],
                 width=900,height=500)
fig.update_layout(clickmode="event+select");

import holdable_tooltips
fn = holdable_tooltips.export_html(fig,filename='output.html',show_hovercustom=True)
````

![holdable_tooltips_plotly](https://github.com/user-attachments/assets/a2aeb9bf-9354-4ced-8f52-aa2ab74952a3)
