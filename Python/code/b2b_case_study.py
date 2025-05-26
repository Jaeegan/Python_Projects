# -*- coding: utf-8 -*-
"""
    ABC Company operates an e-commerce platform and processes thousands of orders daily. To deliver these orders, ABC has partnered with several courier companies in India, which charge them based on the weight of the products and the distance between the warehouse and the customer’s delivery address. ABC wants to check if the fees charged by the courier companies for each order are correct.

    ABC has internal data split across three reports: Website Order Report, Master SKU, and Warehouse PIN for all India Pincode mappings. In addition, they receive billing data from courier companies.

    The website order report includes order IDs and products (SKUs) for each order. The SKU master provides the gross weight of each product, which is needed to calculate the total weight of each order. Courier company invoices contain information such as AWB number, order ID, shipment weight, warehouse pickup PIN, customer delivery PIN, delivery area, the charge per shipment and type of shipment.

    ABC wants to compare the total weight of each order calculated using the SKU master with the weight stated by the courier company in their invoice. The weight should be rounded up to the nearest multiple of 0.5 kg to determine the weight of the tile. The warehouse PIN to all India Pincode mappings is used to determine the delivery area, which should be compared to the area reported by the courier company.

    In addition, ABC must apply the logic of calculating charges based on the slab weight, delivery area and type of shipment listed on the courier company’s invoice. The courier fee rate card provides a fixed fee and an additional fee for each weight plate and PIN. The total charge per shipment should be calculated by adding the fixed charge and any additional charges based on plate weight.

    Credits to resources by Aman Kharwal.
    Url: https://statso.io/b2b-ecommerce-fraud-case-study/

Author:
    Joshua Gan - 04.07.2023
"""

import pandas as pd

courier_rates = pd.read_csv("~/Developer/Data/b2b/Courier Company - Rates.csv")
invoice = pd.read_csv("~/Developer/Data/b2b/Invoice.csv")
order_rpt = pd.read_csv("~/Developer/Data/b2b/Order Report.csv")
pincodes = pd.read_csv("~/Developer/Data/b2b/pincodes.csv")
sku_master = pd.read_csv("~/Developer/Data/b2b/SKU Master.csv")

# Check for missing values
print("Courier Company - Rates: \n", courier_rates.isna().sum(), sep="")
print("\nInvoice: \n", invoice.isna().sum(), sep="")
print("\nOrder Report: \n", order_rpt.isna().sum(), sep="")
print("\nPincodes: \n", pincodes.isna().sum(), sep="")
print("\nSKU Master: \n", sku_master.isna().sum(), sep="")

# Drop columns missing values
order_rpt.drop(columns=["Unnamed: 3", "Unnamed: 4"], inplace=True)
pincodes.drop(columns=["Unnamed: 3", "Unnamed: 4"], inplace=True)
sku_master.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], inplace=True)

# Merge order report and sku master
order_sku = order_rpt.merge(sku_master, on="SKU")
order_sku["Total Weight (kg)"] = order_sku["Order Qty"] * order_sku["Weight (g)"] / 1000

order_sku.rename(columns={"ExternOrderNo": "Order ID"}, inplace=True)
order_sku.drop(columns=["Order Qty", "Weight (g)"], inplace=True)
print(order_sku.head())

# Merge invoice and pincodes
pin = pincodes.drop_duplicates(subset="Customer Pincode")
inv = invoice[["Order ID", "Customer Pincode", "Type of Shipment"]]
inv_pin = inv.merge(pin, on="Customer Pincode")
print(inv_pin.head())

# Merge inv_pin and order_sku
abc_order_list = order_sku.merge(inv_pin, on="Order ID")
print(abc_order_list.head())


# Calculate weight slabs
def weight_slab(weight):
    i = round(weight % 1, 1)
    if i == 0:
        return weight
    elif i > 0.5:
        return int(weight) + 1
    else:
        return int(weight) + 0.5


# Expected weight slab for order (by SKU Master)
abc_order_list["Weight Slab (kg)"] = abc_order_list["Total Weight (kg)"].apply(
    weight_slab
)
# Actual weight slab charged for order
invoice["Weight Slab Charged"] = invoice["Charged Weight"].apply(weight_slab)

# Calculate charges based on the slab weight, delivery area, and type of shipment
total_expected_charge = []

for _, row in abc_order_list.iterrows():
    fwd_category = "fwd_" + row["Zone"]
    fwd_fixed = courier_rates.at[0, fwd_category + "_fixed"]
    fwd_additional = courier_rates.at[0, fwd_category + "_additional"]
    rto_category = "rto_" + row["Zone"]
    rto_fixed = courier_rates.at[0, rto_category + "_fixed"]
    rto_additional = courier_rates.at[0, rto_category + "_additional"]

    weight_slab = row["Weight Slab (kg)"]

    if row["Type of Shipment"] == "Forward charges":
        additional_weight = max(0, (weight_slab - 0.5) / 0.5)
        total_expected_charge.append(fwd_fixed + additional_weight * fwd_additional)
    elif row["Type of Shipment"] == "Forward and RTO charges":
        additional_weight = max(0, (weight_slab - 0.5) / 0.5)
        total_expected_charge.append(
            fwd_fixed
            + rto_fixed
            + additional_weight * (fwd_additional + rto_additional)
        )
    else:
        total_expected_charge.append(0)

abc_order_list["Expected Charge"] = total_expected_charge
print(abc_order_list.head())

# Merge ABC order list with Invoice
invoice_sub = invoice[
    [
        "AWB Code",
        "Order ID",
        "Charged Weight",
        "Zone",
        "Billing Amount (Rs.)",
        "Weight Slab Charged",
    ]
]
abc_order_inv = abc_order_list.merge(
    invoice_sub, on="Order ID", suffixes=["_ABC", "_Inv"]
)
print(abc_order_inv)

df_diff = abc_order_inv
df_diff["Difference (Rs.)"] = (
    df_diff["Billing Amount (Rs.)"] - df_diff["Expected Charge"]
)

df_new = df_diff[["Order ID", "Difference (Rs.)", "Expected Charge"]]
print(df_new.head())

# Calculate the total orders in each category
total_correctly_charged = len(df_new[df_new["Difference (Rs.)"] == 0])
total_overcharged = len(df_new[df_new["Difference (Rs.)"] > 0])
total_undercharged = len(df_new[df_new["Difference (Rs.)"] < 0])

# Calculate the total amount in each category
amt_overcharged = df_new[df_new["Difference (Rs.)"] > 0]["Difference (Rs.)"].sum()
amt_undercharged = df_new[df_new["Difference (Rs.)"] < 0]["Difference (Rs.)"].sum()
amt_correctly_charged = df_new[df_new["Difference (Rs.)"] == 0]["Expected Charge"].sum()

# Create a new DataFrame for the summary
summary_data = {
    "Description": [
        "Total Orders where ABC has been correctly charged",
        "Total Orders where ABC has been overcharged",
        "Total Orders where ABC has been undercharged",
    ],
    "Count": [total_correctly_charged, total_overcharged, total_undercharged],
    "Amount (Rs.)": [amt_correctly_charged, amt_overcharged, amt_undercharged],
}

df_summary = pd.DataFrame(summary_data)
print(df_summary)
