cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
  count_of_active_nodes = 0
  for _ in config["active_nodes"]:
    count_of_active_nodes+=1;
  utilization = (count_of_active_nodes/config["total_max_slots"])*100
  print(f'''
  Cluster: {config['cluster_name']}
  Active Nodes: {count_of_active_nodes}
  Total Capacity: {config['total_max_slots']}
  Utilization: {utilization}%''')


# Execute the audit tool
calculate_capacity(cluster_config)
