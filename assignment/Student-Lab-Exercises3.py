def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
  total_billing_hours  = 30*24
  total_spend = int(instance_count) * float(hourly_rate) * float(total_billing_hours)
  if total_spend > budget_cap:
    budget_exceed = total_spend - budget_cap
    return f'REJECTED: Budget Exceeded by ${budget_exceed:.2f}!'
  else: 
    # est_cost = budget_cap-total_spend  
    return f'APPROVED: Total Estimated Cost is ${total_spend:.2f}.'
  
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.5, budget_cap=5000.00))