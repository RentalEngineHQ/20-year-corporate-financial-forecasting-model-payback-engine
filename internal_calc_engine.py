def calculate_system_metrics(net_income, depreciation, change_in_working_capital, capex):
    operating_cash_flow = float(net_income) + float(depreciation) - float(change_in_working_capital)
    free_cash_flow = operating_cash_flow - float(capex)
    return operating_cash_flow, free_cash_flow
