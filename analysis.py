import pandas as pd

def load_data():
    df = pd.read_csv("data/funnel_data.csv")
    return df

def overall_conversion(df):
    visitors = df['visited'].sum()
    leads = df['lead'].sum()
    customers = df['customer'].sum()

    return {
        "Visitors": visitors,
        "Leads": leads,
        "Customers": customers,
        "Visitor → Lead %": (leads / visitors) * 100,
        "Lead → Customer %": (customers / leads) * 100
    }

def channel_performance(df):
    result = df.groupby("channel").agg({
        "visited": "sum",
        "lead": "sum",
        "customer": "sum"
    })

    result["Visitor→Lead %"] = (result["lead"] / result["visited"]) * 100
    result["Lead→Customer %"] = (result["customer"] / result["lead"]) * 100

    return result

def drop_off(df):
    visitors = df['visited'].sum()
    leads = df['lead'].sum()
    customers = df['customer'].sum()

    drop_visitor_to_lead = visitors - leads
    drop_lead_to_customer = leads - customers

    return {
        "Dropped after Visit": drop_visitor_to_lead,
        "Dropped after Lead": drop_lead_to_customer
    }