import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Read the data
data = pd.read_csv('../emails.csv')
data = data.sample(n=50000, random_state=42)  # Using random_state for reproducibility

# Extract email addresses
def extract_emails(text):
    import re
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', str(text))

# Create a directed graph
G = nx.DiGraph()

# Process emails and add edges
for _, row in data.iterrows():
    message = row['message']
    emails = extract_emails(message)
    
    # Add edges between sender and recipients
    if len(emails) >= 2:
        sender = emails[0]
        for recipient in emails[1:]:
            if '@enron.com' in sender and '@enron.com' in recipient:
                G.add_edge(sender, recipient)

# Calculate node sizes based on degree
degrees = dict(G.degree())
node_sizes = [degrees[node] * 10 for node in G.nodes()]

# Calculate node colors based on betweenness centrality
betweenness = nx.betweenness_centrality(G)
node_colors = [betweenness[node] for node in G.nodes()]

# Create the plot
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, k=0.3, iterations=50)

# Draw the graph
nx.draw_networkx_nodes(G, pos, 
                      node_size=node_sizes,
                      node_color=node_colors,
                      cmap=plt.cm.viridis,
                      alpha=0.7)

nx.draw_networkx_edges(G, pos, 
                      edge_color='gray',
                      alpha=0.2,
                      arrowsize=5)

# Add labels for the most important nodes (top 5 by betweenness)
top_nodes = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
for node, _ in top_nodes:
    plt.annotate(node.split('@')[0], 
                xy=pos[node],
                xytext=(10, 10),
                textcoords='offset points',
                fontsize=8)

plt.title('Enron Email Network', fontsize=16)
plt.axis('off')

# Add a colorbar
sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, 
                          norm=plt.Normalize(vmin=min(node_colors), 
                                           vmax=max(node_colors)))
sm.set_array([])
plt.colorbar(sm, label='Betweenness Centrality')

# Save the plot
plt.savefig('images/enron_network.png', dpi=300, bbox_inches='tight')
plt.close() 