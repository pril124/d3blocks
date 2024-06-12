from d3blocks import D3Blocks
import pandas as pd

# Initialize
d3 = D3Blocks(verbose="info", chart="tree", frame=False)


# df = d3.import_example("energy")

# level = [
#     1,
#     1,
#     1,
#     1,
#     2,
#     2,
#     2,
#     2,
#     3,
#     4,
#     2,
#     3,
#     3,
#     3,
#     3,
#     3,
#     3,
#     3,
#     4,
#     5,
#     3,
#     3,
#     3,
#     4,
#     4,
#     4,
#     4,
#     4,
#     3,
#     4,
#     3,
#     4,
#     3,
#     4,
#     3,
#     2,
#     3,
#     4,
#     2,
#     2,
#     2,
#     2,
#     3,
#     3,
#     3,
#     3,
# ]


# source = [
#     "Notes (02/28/2024)",
#     "Notes (02/28/2024)",
#     "Notes (02/28/2024)",
#     "Notes (02/28/2024)",
#     "Client Goals and Objectives",
#     "Client Goals and Objectives",
#     "Client Goals and Objectives",
#     "Estate Planning",
#     "Superannuation",
#     "Wills",
#     "Assets and Liabilities",
#     "Assets",
#     "Assets",
#     "Assets",
#     "Assets",
#     "Assets",
#     "Australian Superannuation",
#     "Australian Superannuation",
#     "Inheritor",
#     "Lori",
#     "Investments Portfolio Discussion",
#     "Investments Portfolio Discussion",
#     "Investments Portfolio Discussion",
#     "Portfolio Contents",
#     "Portfolio Contents",
#     "Portfolio Contents",
#     "Comments",
#     "Advice",
#     "Cars",
#     "Reviewed",
#     "Wills",
#     "Reviewed",
#     "Investment Returns",
#     "Reviewed",
#     "Investment Returns",
#     "Liabilities",
#     "Tax Deduction",
#     "Address Client's Contribution",
#     "Topic for Next Meeting",
#     "Topic for Next Meeting",
#     "Topic for Next Meeting",
#     "Topic for Next Meeting",
#     "Financial Situation",
#     "Financial Situation",
#     "Investment Portfolio",
#     "Superannuation Funds",
# ]
# target = [
#     "Client Goals and Objectives",
#     "Estate Planning",
#     "Assets and Liabilities",
#     "Topic for Next Meeting",
#     "Maintaining Income Protection Insurance",
#     "Managing Superannuation Contributions",
#     "Investment Strategies to Enhance Portfolio Returns",
#     "Superannuation",
#     "Goes to Lori",
#     "Reviewed already",
#     "Assets",
#     "Australian Superannuation",
#     "Investments Portfolio Discussion",
#     "Cars",
#     "Wills",
#     "Investment Returns",
#     "Insurance within the Superannuation",
#     "Inheritor",
#     "Lori",
#     "Has up to date nominations",
#     "Portfolio Contents",
#     "Comments",
#     "Advice",
#     "Sale of an underperforming global fund with a capital gain",
#     "Purchase of a new fund run by a business called Sage",
#     "High-interest bond fund",
#     "Portfolio has built up cash from ongoing contributions",
#     "Maintain a Cash Balance of $10,000.00 plus any additional Contributions",
#     "Reviewed",
#     "Satisfactory",
#     "Reviewed",
#     "Satisfactory",
#     "Reviewed",
#     "Satisfactory",
#     "14% up to the end of February from the Previous Year",
#     "Tax Deduction",
#     "Address Client's Contribution",
#     "June",
#     "Financial Situation",
#     "Upcoming expenses",
#     "Investment Portfolio",
#     "Superannuation Funds",
#     "The client's father's well-being",
#     "Financial Implications following the passing of their mother.",
#     "Changes that may be required.",
#     "Balance in Australian Super",
# ]

# list_of_nodes = list(zip(source, target, level))
# print(list_of_nodes)

list_of_nodes = [
    ("Notes (02/28/2024)", "Client Goals and Objectives", 1),
    ("Notes (02/28/2024)", "Estate Planning", 1),
    ("Notes (02/28/2024)", "Assets and Liabilities", 1),
    ("Notes (02/28/2024)", "Topic for Next Meeting", 1),
    ("Client Goals and Objectives", "Maintaining Income Protection Insurance", 2),
    ("Client Goals and Objectives", "Managing Superannuation Contributions", 2),
    (
        "Client Goals and Objectives",
        "Investment Strategies to Enhance Portfolio Returns",
        2,
    ),
    ("Estate Planning", "Superannuation", 2),
    ("Superannuation", "Goes to Lori", 3),
    ("Wills", "Reviewed already", 4),
    ("Assets and Liabilities", "Assets", 2),
    ("Assets and Liabilities", "Liabilities", 2),
    ("Assets", "Australian Superannuation", 3),
    ("Assets", "Investments Portfolio Discussion", 3),
    ("Assets", "Cars", 3),
    ("Assets", "Wills", 3),
    ("Assets", "Investment Returns", 3),
    ("Australian Superannuation", "Insurance within the Superannuation", 4),
    ("Australian Superannuation", "Inheritor", 4),
    ("Inheritor", "Lori", 5),
    ("Lori", "Has up to date nominations", 5),
    ("Investments Portfolio Discussion", "Portfolio Contents", 4),
    ("Investments Portfolio Discussion", "Comments", 4),
    ("Investments Portfolio Discussion", "Advice", 4),
    (
        "Portfolio Contents",
        "Sale of an underperforming global fund with a capital gain",
        5,
    ),
    ("Portfolio Contents", "Purchase of a new fund run by a business called Sage", 5),
    ("Portfolio Contents", "High-interest bond fund", 5),
    ("Comments", "Portfolio has built up cash from ongoing contributions", 5),
    (
        "Advice",
        "Maintain a Cash Balance of $10,000.00 plus any additional Contributions",
        5,
    ),
    ("Cars", "Cars - Reviewed", 4),
    ("Cars - Reviewed", "Cars - Satisfactory", 5),
    ("Wills", "Wills - Reviewed", 4),
    ("Wills - Reviewed", "Wills - Satisfactory", 5),
    ("Investment Returns", "Investment Returns - Reviewed", 4),
    ("Investment Returns - Reviewed", "Investment Returns - Satisfactory", 5),
    ("Investment Returns", "14% up to the end of February from the Previous Year", 5),
    ("Liabilities", "Tax Deduction", 3),
    ("Tax Deduction", "Address Client's Contribution", 4),
    ("Address Client's Contribution", "June", 4),
    ("Topic for Next Meeting", "Financial Situation", 2),
    ("Topic for Next Meeting", "Upcoming expenses", 2),
    ("Topic for Next Meeting", "Investment Portfolio", 2),
    ("Topic for Next Meeting", "Superannuation Funds", 2),
    ("Financial Situation", "The client's father's well-being", 3),
    (
        "Financial Situation",
        "Financial Implications following the passing of their mother.",
        3,
    ),
    ("Investment Portfolio", "Changes that may be required.", 3),
    ("Superannuation Funds", "Balance in Australian Super", 3),
]

# data = {"source": source, "target": target, "level": level}

# Create DataFrame
df = pd.DataFrame(list_of_nodes, columns=["source", "target", "level"])

# df = df[0:14]
print(df)

d3.set_node_properties(df)
print(d3.node_properties)

for idx, row in df.iterrows():
    try:
        if row["level"] == 1:
            d3.node_properties.get(row.get("source"))["color"] = "#74D3AE"
            d3.node_properties.get(row.get("source"))["size"] = 10
            d3.node_properties.get(row.get("source"))["edge_color"] = "#74D3AE"
            d3.node_properties.get(row.get("source"))["font_color"] = "red"
            d3.node_properties.get(row.get("source"))["font_size"] = 15
            d3.node_properties.get(row.get("source"))["font_family"] = "Verdana"
        elif row["level"] == 2:
            d3.node_properties.get(row.get("source"))["color"] = "#C62E65"
            d3.node_properties.get(row.get("source"))["size"] = 8
            d3.node_properties.get(row.get("source"))["edge_color"] = "#C62E65"
            d3.node_properties.get(row.get("source"))["font_size"] = 15
            d3.node_properties.get(row.get("source"))["font_family"] = "Verdana"
        elif row["level"] == 3:
            d3.node_properties.get(row.get("source"))["color"] = "#DD9787"
            d3.node_properties.get(row.get("source"))["size"] = 5
            d3.node_properties.get(row.get("source"))["edge_color"] = "#DD9787"
            d3.node_properties.get(row.get("source"))["font_size"] = 12
        else:
            d3.node_properties.get(row.get("source"))["color"] = "#EBD6AF"
            d3.node_properties.get(row.get("source"))["size"] = 5
            d3.node_properties.get(row.get("source"))["edge_color"] = "#EBD6AF"
            # d3.node_properties.get(row.get("source"))["edge_color"] = "#F6E7CB"
            d3.node_properties.get(row.get("source"))["font_size"] = 12
    except Exception as e:

        print(row["source"])

# Set edge properties
d3.set_edge_properties(df)

print(d3.edge_properties)

# Show chart
d3.show(
    hierarchy=[1, 2, 3, 4, 5, 6, 7, 8],
    filepath=r"tree.html",
    figsize=[800, 1200],
    font={"size": 15},
    margin={"top": 40, "right": 40, "bottom": 40, "left": 200},
    save_button=True,
)
