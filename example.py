from d3blocks import D3Blocks
import pandas as pd
import numpy as np

d3 = D3Blocks(verbose="info", chart="tree", frame=False)

df = pd.read_csv("input.csv")

d3.set_node_properties(df)
print(d3.node_properties)

# for idx, row in df.iterrows():
#     try:
#         if row["level"] == np.nan:
#             d3.node_properties.get(row.get("source"))["color"] = "#74D3AE"
#             d3.node_properties.get(row.get("source"))["size"] = 10
#             d3.node_properties.get(row.get("source"))["edge_color"] = "#74D3AE"
#             d3.node_properties.get(row.get("source"))["font_color"] = "red"
#             d3.node_properties.get(row.get("source"))["font_size"] = 15
#             d3.node_properties.get(row.get("source"))["font_family"] = "Verdana"
#         elif row["level"] == 2:
#             d3.node_properties.get(row.get("source"))["color"] = "#C62E65"
#             d3.node_properties.get(row.get("source"))["size"] = 8
#             d3.node_properties.get(row.get("source"))["edge_color"] = "#C62E65"
#             d3.node_properties.get(row.get("source"))["font_size"] = 15
#             d3.node_properties.get(row.get("source"))["font_family"] = "Verdana"
#         elif row["level"] == 3:
#             d3.node_properties.get(row.get("source"))["color"] = "#DD9787"
#             d3.node_properties.get(row.get("source"))["size"] = 5
#             d3.node_properties.get(row.get("source"))["edge_color"] = "#DD9787"
#             d3.node_properties.get(row.get("source"))["font_size"] = 12
#         else:
#             d3.node_properties.get(row.get("source"))["color"] = "#EBD6AF"
#             d3.node_properties.get(row.get("source"))["size"] = 5
#             d3.node_properties.get(row.get("source"))["edge_color"] = "#EBD6AF"
#             # d3.node_properties.get(row.get("source"))["edge_color"] = "#F6E7CB"
#             d3.node_properties.get(row.get("source"))["font_size"] = 12
#     except Exception as e:
#         pass

# print(d3.node_properties)

# Set edge properties
d3.set_edge_properties(df)

print(d3.edge_properties)

# Show chart
d3.show(
    hierarchy=[1, 2, 3, 4, 5, 6, 7, 8],
    filepath=r"tree.html",
    figsize=[1000, 1500],
    font={"size": 15},
    margin={"top": 40, "right": 40, "bottom": 40, "left": 40},
)
